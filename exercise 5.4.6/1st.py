sentence = input("write a sentence\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"
count = {}
for i in sentence:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

keys = count.keys()

for i in sorted(keys):
    print(i, count[i])
