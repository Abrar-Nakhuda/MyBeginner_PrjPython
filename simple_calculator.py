#simple_calculator

operator = input("choose an  operator( + - / * % // **): ") # this will decide the operation

num1 = int(input("choose your first number: ")) 
num2 = int(input("choose your second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} equals {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} equals {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} equals {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} equals {result}")
elif operator == "%":
    result = num1 % num2
    print(f"{num1} % {num2} equals {result}")
elif operator == "//":
    result = num1 // num2
    print(f"{num1} // {num2} equals {result}")
elif operator == "**":
    result = num1 ** num2
    print(f"{num1} ** {num2} equals {result}")
else:
    print(f" {operator} is an invalid operator")
