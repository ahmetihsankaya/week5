def dot_product(u, v):
    results = 0
    for i in range(len(u)):
        results = results + u[i] * v[i]
    return results

print(dot_product([1,1],[1,1]))
print(dot_product([1, 2], [1, 4]))
print(dot_product([1, 2, 1], [1, 4, 3]))
