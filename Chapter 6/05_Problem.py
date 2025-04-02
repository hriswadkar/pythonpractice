names = ["Harshad", "Anuja", "Pratibha", "Sayali"]

user_name = input("Enter your name: ")

if(user_name in names):
    print(f"Your name {user_name} is in the list")
else:
    print(f"Your name {user_name} is not in the list")