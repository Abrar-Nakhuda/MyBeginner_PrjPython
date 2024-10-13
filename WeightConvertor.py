#WeightConvertor

Weight = float(input("how much do you weigh?: "))
unit = input("Kgs or Lbs?: ").lower()

if unit == "Kgs":
    WeightLbs = round(Weight * 2.205, 2)
    print(f" you weight is {WeightLbs} in Lbs")
elif unit == "Lbs":
    WeightKgs = round(Weight / 2.205, 2)
    print(f" your weight is {WeightKgs} in Kgs")
else:
    print(f"{unit} is invalid")