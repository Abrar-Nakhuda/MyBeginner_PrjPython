#CompoundInterestCalc

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("enter principle amount: "))
    if principle < 0:
        print("principle cannot be zero!")

while True:
    rate = float(input("enter interest rate: "))
    if rate < 0:
        print("Interest rate cannot be less than or equal to zero!")

while True:
    time = float(input("enter investment period in years: "))
    if time <= 0:
        print("time cannot be less than or equal to zero!")
    
total = round(principle * pow((1 + rate / 100), time), 2)
print(f" the total amount after {time} years with a principle of ${principle} is ${total}")