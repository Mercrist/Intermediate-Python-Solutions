def permute(inputList):
    '''permute(inputList) -> list
    returns list of all permutations of inputList'''
    # base case
    if len(inputList) == 1:
        return [inputList[:]]
    # recursive step
    outputList = []  # to store permutations
    for index in range(len(inputList)):
        # construct all permutations that start with the item
        #   at location give by index
        # remove item and permute the rest
        restOfList = inputList[:index]+inputList[index+1:]
        perms = permute(restOfList)
        # add all permutations starting with inputList[index]
        #   and ending with each permuatation just generated
        for tail in perms:
            outputList.append([inputList[index]]+tail)
    return outputList

# test cases
print(permute([1,2]))
# should print [[1,2], [2,1]] in some order
print(permute([1,2,3]))
# should print [[1,2,3], [1,3,2], [2,1,3], [3,1,2], [2,3,1], [3,2,1]] in some order

