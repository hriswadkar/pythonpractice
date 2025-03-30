f = open("./LoremIpsum.txt", "rb")
data = f.read()
print(data)

f.close()


# The same can be written using with block
print()
print()
print("The same can be written using with block")
print()
print()

with open("./LoremIpsum.txt") as f:
    print(f.read())


# Using with block, there is no need to call file.close() method    

