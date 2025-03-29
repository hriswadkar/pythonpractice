# Write a program to find if a given number is prime or not

def is_prime(num):
    ret_val = False
    if (number <= 1):
        ret_val = False
    else:
        for i in range (2, number):
            if (number % i == 0):
                ret_val = False
                break
            else:
                ret_val = True
    
    return ret_val

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a primary number")
else:
    print(f"{number} is not a primary number")


