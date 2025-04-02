# Write a program using functions to convert Celsius to Farenheit

def CelsiusToFarenheit(degrees):
    return ((degrees * 9/5) + 32)



deg = int(input("Enter temperature in Celsius: "))

print(f"Temperature in Celsius is: {deg} ")
print("Temperature in Farenheit is: ", CelsiusToFarenheit(deg))