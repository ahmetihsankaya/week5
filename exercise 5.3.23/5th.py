def add_vector(u,v):
    results = []
    for i in range(len(u)):
        results.append(u[i] + v[i])
    return results

#print(add_vector([1, 1], [1, 1]))
#print(add_vector([1, 2], [1, 4]))
print(add_vector([1, 2, 1], [1, 4, 3]))