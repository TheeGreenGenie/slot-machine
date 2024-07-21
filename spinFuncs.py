import random

def check_slots(columns, lines, bet):
    values = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2
    }
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

        return winnings

def get_slots_spin():
    ROWS, COLS = 3, 3
    symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
    }

    all_symbols = []
    for symbol, symbol_count in symbol_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(COLS):
        column = []
        symbols_now = all_symbols[:]
        for _ in range(ROWS):
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

spun = get_slots_spin()
print_slots(spun)

print(spun)