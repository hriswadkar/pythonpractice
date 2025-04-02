# Dictionary Merge and Update operator

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1 | dict2

print(f"dictionary1: {dict1} ")
print(f"dictionary2: {dict2} ")
print(f"Merged Dictionary using | operator: {merged}")

print("Now using |= operator on dictionary1")
dict1 |= dict2

print(dict1)

