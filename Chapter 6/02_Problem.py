sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))

if(sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and (((sub1 + sub2 + sub3) * 100)/300) > 40):
    print("Pass")
else:
    print("Fail")