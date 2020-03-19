def scalar_mult(scalar, vector):
    results = []
    for i in vector:
        results.append(scalar * i)
    return results

#print(scalar_mult(5,[1,2]))
#print(scalar_mult(3, [1, 0, -1]))
print(scalar_mult(7, [3, 0, 5, 11, 2]))