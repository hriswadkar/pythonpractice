marks = []
for i in range(6):
    a = input(f"Enter mark of student {i+1} ")
    marks.append(a)

marks.sort()
print(marks)