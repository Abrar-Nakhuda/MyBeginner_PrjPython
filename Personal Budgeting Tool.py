#Personal Budgeting Tool

#Initialize an empty dictionary to store expenses
expenses = {}

#Prompt user to enter expenses for each category
print("enter your monthly expenses ")

#Categories of expense
categories = ["rent", "Groceries", "utilities",
              "Entertainment", "Miscellaneous"]


for category in categories:
    while True:  # Loop until valid input is received
        try:
            expense = float(input(f"Enter your expense for {category}: "))
            expenses[category] = expense
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")

total_expenses = sum(expenses.values())


with open("monthly_budget.txt", "w") as file:
    file.write("Monthly Expenses:\n")
    for category, amount in expenses.items():
         file.write(f"{category}: ${amount}\n")
    file.write(f"\nTotal Monthly Expenses: ${total_expenses}\n")



#Print out the dictionary to verify
print("\nYour expenses by category:")
print(expenses)
print("\nYour Total monthly expenses:", total_expenses)
print("\nExpenses have been saved to 'monthly_budget.txt'.")

