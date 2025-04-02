

with open("./log.txt") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if ("Python" in line):
        print(f"word Python found in the log at line: {lineNo}")
        break
    lineNo += 1
else:
    print("word Python not found in the log")