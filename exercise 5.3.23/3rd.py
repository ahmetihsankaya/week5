a = [1,2,3]
b = a[:]
b[0]=5

#in the 2nd line, we cloned the a as b. after that, changes in b will not change the a.

c=a
c[0]=10

#here, we duplicated a with c. c and a are same here and changes in c will change a too.

print(a)
print(b)
print(c)

