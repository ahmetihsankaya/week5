#not sure yet!

def cross_product(u, v):
    results = []
    for i in range(len(u)):
        if i == 0:
            results.append(u[1]*v[2] - u[2]*v[1])
        elif i==1:
            results.append(u[0]*v[2] - u[2]*v[0])
        else:
            results.append(u[0]*v[1] - u[1]*v[0])
    return results

print(cross_product([1,2,3],[3,2,1]))