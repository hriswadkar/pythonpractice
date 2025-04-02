# Write a program to find the sum of first n natural numbers using while loop

num = int(input("Enter a number: "))

counter = 1
sum = 0

while (counter <= num):
    sum += counter
    counter += 1

print(sum)

# using formula sum = (n * (n + 1) // 2)

print(f"Calculating sum of first {num} natural numbers using formula: ")

print((num * (num + 1) // 2))



def SumOfNaturalNumbers(number):
    if (number == 1):
        return 1
    elif (number == 0):
        return 0
    else:
        return number + SumOfNaturalNumbers(number - 1)
    

print(f"Calculating sum of first {num} natural numbers using recursion: ")

print("Sum is: ", SumOfNaturalNumbers(num))