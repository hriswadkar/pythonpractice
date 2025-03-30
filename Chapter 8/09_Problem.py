List = ["Harshad", "Mandar", "Rahul", "Shyam", "Kiran", "Shubham", "Aman"]

def RemoveWord(list, word):
    for item in list:
        list.remove(word)
        return list
    

print(List)

print(RemoveWord(List, "Kiran"))