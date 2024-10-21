#BankingProgram

def show_balance():
    print(f"your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: $"))

    if amount < 0:
        print(f"{amount} is not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdrawn: $"))

    if amount > balance:
        print("Insufficent Funds")
        return 0
    elif amount <= 0:
        print("amount must be greater than 0")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("A. Show Balance")
    print("B. Deposit")
    print("C. Withdraw")
    print("D. Exit")

    choice = input("enter your choice: ")

    if choice == 'A':
        show_balance()
    elif choice == 'B':
        balance += deposit()
    elif choice == 'C':
        balance -= withdraw()
    elif choice == 'D':
        is_running = False
    else:
        print("your choice was invalid!, please enter a valid choice.")

print("thank you")