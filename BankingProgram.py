#BankingProgram

def show_balance():
    print(f"your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print(f"{amount} is not a valid amount")

def withdraw():
    pass

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
        deposit()
    elif choice == 'C':
        withdraw()
    elif choice == 'D':
        is_running = False
    else:
        print("your choice was invalid!, please enter a valid choice.")

print("thank you")