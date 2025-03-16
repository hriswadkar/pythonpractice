import numpy as np

# print all numbers divisible by 2

for i in range(0,101,2):
    if(i%2 == 0):
        print(i)

# print all numbers divisible by 3
print("print all numbers divisible by 3")
for i in range(1,101,1):
    if(i % 3 == 0):
        print(i)

print(np.arange(1.0, 10.0, 0.5))