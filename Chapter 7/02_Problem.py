# Write a program to great all the people whose name start with 'S'. Names are given in the list

list = ["Harshad", "Sunil", "Anil", "Sanjay", "Sachin", "Rahul"]

for name in list:
    if (name.lower().startswith("s")):
        print(f"Hello, {name}")