dictionary = {"apples": 15, "bananas": 35, "grapes": 12}
dictionary["oranges"] = 20
print(len(dictionary))
print("grapes" in dictionary)
#dictionary["pears"]
dictionary.get("pears", 0)
fruits = list(dictionary.keys())
del dictionary["apples"]
print("apples" in dictionary)