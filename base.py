import random
import tkinter as tk
from PIL import ImageTk, Image
import time

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3


symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_slots(columns, lines, bet, values):
    winnings = 0 
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            check = column[line]
            if symbol != check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

        return winnings, winning_lines

def get_slots_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        symbols_now = all_symbols[:]
        for _ in range(rows):
            value = random.choice(symbols_now)
            symbols_now.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="  |  ")
            else:
                print(column[row], end="")

        print()
     
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')

    return amount

def get_num_of_lines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if lines in range(1,4):
                break
            else:
                print('Enter a valid number of lines.')
        else:
            print('Please enter a number.')

    return lines

def get_bet():
    while True:
        bet = input(f"What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if bet in range(MIN_BET,MAX_BET+1):
                break
            else:
                print(f'Amount must be between ${MIN_BET} & ${MAX_BET}.')
        else:
            print('Please enter a number.')
    return bet

def spinner(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        tot_bet = lines*bet
        if tot_bet > balance:
            print(f"Your balance is lower than your ${tot_bet} bet. Your balance is ${(tot_bet)-balance} short")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${lines*bet}")

    print(balance, lines)

    slots = get_slots_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings, winning_lines = check_slots(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on:", *winning_lines)
    return winnings - tot_bet

def gui_starter():
    root = tk.Tk()
    root.geometry("500x500")
    root.resizable(False, False)
    root.title("Slot Machine")
    image = Image.open('Welcome.png')
    image = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    starter = tk.Button(root, text="Start Game", font=("Arial", 18), bg='yellow', fg='purple', relief='groove', height=2, bd=10)
    starter.pack(side=tk.BOTTOM)
    root.mainloop()

def main():
    gui_starter()
    # balance = deposit()
    # while True:
    #     print(f"Current Balance is ${balance}")
    #     spin = input("Press enter to play (q to quit).")
    #     if spin == 'q':
    #         break
    #     balance += spinner(balance)

    # print(f"You left with ${balance}")

main()

