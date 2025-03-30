
with open("./10_Problem.txt", "r") as f:
    print(f.readlines())

print()
print()
print()
print("Wiping contents of the file...")
print()
print()
print()

with open("./10_Problem.txt", "w") as f:
    f.write("")



with open("./10_Problem.txt", "r") as f:
    print(f.readlines())

