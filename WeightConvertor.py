#WeightConvertor

print("weight Convertor")
Weight = float(input("how much do you weigh?: "))
unit = input("Kgs or Lbs?: ").lower()

if unit == "kgs":
    WeightLbs = round(Weight * 2.205, 2)
    print(f" you weight in lbs is {WeightLbs}")
elif unit == "lbs":
    WeightKgs = round(Weight / 2.205, 2)
    print(f" your weight in Kgs is {WeightKgs}")
else:
    print(f"{unit} is invalid")