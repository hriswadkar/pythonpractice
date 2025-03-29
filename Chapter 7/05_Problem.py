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
