
f = open("./MyFile2.txt")

l = f.readlines()

print(l)

for i in range(len(l)):
    print(l[i])

f.close()

print()
print("Using While Loop")
print()

f2 = open("./MyFile2.txt")
line = f2.readline()
while(line != ""):
    print(line)
    line = f2.readline()


    