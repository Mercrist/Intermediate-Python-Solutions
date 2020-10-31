def catalan(n):
    '''catalan(n) -> int
    returns C_n, the nth Catalan number'''
    # base case
    catList = [1]
    # recursive step
    for k in range(1,n+1):
        total = 0
        for i in range(k):
            # sum over all pairs whose indices sum to k-1
            total += catList[i] * catList[k-1-i]
        catList.append(total)
    return catList[n]

print(catalan(30))
