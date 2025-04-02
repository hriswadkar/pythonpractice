# print multiplication table of a given number using for loop

num = int(input("Enter a number: "))

for i in range(10):
    print(f"{num} * {i+1} = {num * (i+1)}")
