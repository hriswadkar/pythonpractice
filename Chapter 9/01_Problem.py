
f = open("poems.txt")
content = f.read()
if ("twinkle" in content):
    print("twinkle is present in content")
else:
    print("twinkle is not present in the content")


f.close()