import random

#Gives scores when slots in a row are matching. 
def check_slots(columns, lines, bet):
    values = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2
    }
    winnings = 0 
    winning_lines = []
    lines_dict = {}
    
    for i in range(len(columns)):
        row = columns[i]
        for x in range(len(row)):
            vertice = columns[i][x]
            if x not in lines_dict:
                lines_dict[x] = [vertice]
            else:
                lines_dict[x].append(vertice)

    for i in lines_dict:
        line_num  = i
        line = lines_dict[i]
        last = ''
        won = True
        for i in line:
            if i == line[0]:
                last = i
                continue
            else:
                won = False
        if won:
            line_winning = bet*values[line[0]]
        else:
            line_winning = 0
        winning_lines.append((line_winning, line_num))
    
    for i in range(lines):
        winnings+=winning_lines[i][0]

    return winnings

#Generates a new random array of slot symbols
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

#Prints slots to terminal
def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="  |  ")
            else:
                print(column[row], end="")

        print()

# spin = get_slots_spin()
# print_slots(spin)

# print(spin)
# print(check_slots(spin, 0, 150))

spin = [['A', 'D', 'D'], ['A', 'D', 'D'], ['A', 'D', 'C']]

print(check_slots(spin, 2, 150))