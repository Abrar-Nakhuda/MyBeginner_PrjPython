#ShoppingCartProgram

foods = []
costs = []
total = 0

while True:
    food = input("enter your food(x to exit): ")
    if food.lower() == "x":
        break
    else:
        price = float(input(f"enter the price of {food}: $"))
        foods.append(food)
        costs.append(price)



print("------RECEIPT------")

for food in foods:
    print(food, end = "/")

for price in costs:
    total += price
    print(price, end = " ")


print()
print(f"your total is ${total}")


print("-------------------")