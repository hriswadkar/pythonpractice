
with open("./log.txt") as f:
    content = f.read()

if ("Python" in content):
    print("word Python found in the log")
else:
    print("word Python not found in the log")