def greet_user(name):
    print("Hello, " + name)

def greet_user2 (name = "Unknown User"):
    print("Hello, " + name)

name = input("Enter your name: ")
greet_user(name)
greet_user2()
greet_user2(name)

