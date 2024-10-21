#PythonSlotMachine
import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐️']

    return [random.choice(symbols) for _ in range(3) ]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 10
        elif row[0] == '🔔':
            return bet * 12
        elif row[0] == '⭐️':
            return bet * 2
    return 0
        
def main():
    balance = 100

    print("--------------------------------")
    print("welcome to the python lottery!")
    print("Symbols:   🍒   🍉   🍋   🔔  ⭐️")
    print("--------------------------------")

    while balance > 0:
        print(f"Your current balance ${balance}")

        bet = input("place your bet amount: $")
    
        if not bet.isdigit():
            print("enter a valid amount")
            continue

        bet = int(bet)

        if bet > balance:
            print("insuffucent funds")
            continue

        if bet <= 0:
            print("Bet must be greater than zero!")

        balance -= bet

        row = spin_row()
        print("spinning---\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"you won ${payout}")
        else:
            print("sorry you lost this round, try again!")
        
        balance += payout

        play_again = input("Do you want to play again?(Y/N)?: ").upper()

        if play_again != 'Y':
            break
    
    print("-------------------------------------------")
    print(f"Game over your final balance us ${balance}")
    print("-------------------------------------------")

if __name__ == "__main__":
    main()