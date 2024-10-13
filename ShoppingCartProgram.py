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

#for food in foods:
#    print(food)

#for price in costs:
#    total += price

for food, price in zip(foods,costs):
    print(f"{food}:    ${price:.2f}")  # Print food with its corresponding price
    total += price



print("-----------------------")
print(f"your total is ${total}")
print("-----------------------")