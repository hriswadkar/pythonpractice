# Write a program to convert inches into cms

def InchesToCms(inches):
    return inches * 2.54

inch = float(input("Enter inches: "))

print(f"Inches entered {inch}")
print("After converting to cms, value is ", InchesToCms(inch))