this = ['I', 'am', 'not', 'a', 'crook']
that = ['I', 'am', 'not', 'a', 'crook']
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this == that))
print("Test 3: {0}".format(this is that))

#in the first test, although the elements are same in this & that, they are not same lists.
#in the second test, we equalized the elements of "that" with "this", thus, we basically changed the elements of this with that.
#although there's no visible difference between the first and second "that", the second one is exact same after we equalize it with "this" list.
