#TemperatureConversion
print("temp convertor")
temperature = float(input("What is the temperature?: "))
unit = input("Faremheit or Celcius? (C/F): ").lower()

if unit == "c":
    temperature = round((9 * temperature) / 5 + 32, 2)
    print(f" the temperature in farenheit is {temperature}°F") # to get ° on mac its shift+option+8
elif unit == "f":
    temperature = round((temperature - 32) * 5 /9, 2)
    print(f" the temperature in celcius is {temperature}°C")
else:
    print(f"{unit} was invalid")