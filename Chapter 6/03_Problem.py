spam_text = ["Make a lot of money", "buy now", "subscribe this", "click this"]

user_input = input("Enter something: ")

if user_input in spam_text:
    print(f"spam text found")
else:
    print(f"spam text not found")