import random

MAX_BET = 100
MIN_BET = 1
MAX_LINES = 3

ROWS = 3
COLS = 3

symbol_count ={
    "A":5,
    "B":6,
    "C":6,
    "D":7
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2 
}

def check_winnings(columns,lines,bet,values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winning += values[symbol] * bet
            winning_lines.append(line + 1)

    return winning, winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
    
def deposit():
    while True:
        amount = input("How much do you want to deposite?$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("please enter amount that is greater than 0")
        else:
            print("please enter a number!!")
    return amount

def get_numebr_of_lines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on (1 -" + str(MAX_LINES) + ")?" )
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print(f"please enter amount that is 1 - {MAX_LINES}")
        else:
            print("please enter a number!!")
    return lines

def get_bet():
    while True:
        amount = input("How much do you want to bet?$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number!!")
    return amount
def spin_game(balance):
    lines = get_numebr_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You dont have enough to bet that amount. your current balance is:${balance}")
        else:
            break
    print(f"You  are betting ${bet} on {lines} lines.Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", * winning_lines)
    return winnings - total_bet
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("Press enter to play (q to quit).")
        if spin == "q":
            break
        balance += spin_game(balance)
    print(f"You left with ${balance}")
main()
