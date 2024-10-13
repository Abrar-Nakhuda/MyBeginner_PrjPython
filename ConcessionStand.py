#ConcessionStand

# dict  {key: value}
print("Movie Theator")
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("--------Menu---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------")

while True:
    food = input("select an item (x to exit)").lower()
    if food == "x":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"the total is: ${total:.2f}")