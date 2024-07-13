MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


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

def main():
    balance = deposit()
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        if lines*bet > balance:
            print(f"Your balance is lower than your ${lines*bet} bet. Your balance is ${(bet*lines)-balance} short")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${lines*bet}")

    print(balance, lines)


main()