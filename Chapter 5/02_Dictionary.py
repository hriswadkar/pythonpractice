a = {"Key":"Value",
     "Marks":"100",
     "List":[1,2,3]
     }

print(a.items())
print(a.keys())
print(a.values())
a.update({"Marks":99})
print(a["Marks"])