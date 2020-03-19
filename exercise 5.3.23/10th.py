def replace(s, old, new):
    words = new.join(s.split(old))
    return words

print(replace("Mississippi","i","I"))

song = "I love spom! Spom is my favorite food. Spom, spom, yum!"
print(replace(song,"om","am"))
print(replace(song,"o","a"))

