user_name = input("Enter user name: ")

if(len(user_name) < 10):
    print(f"{user_name} should not be less than 10 characters")
else:
    print(f"{user_name} is equal to or more than 10 characters")