def get_base_number(num,base):
    '''get_base_number(num,base) -> int
    returns value of num as a base number in the given base'''
    num = list (num) #convert into a list and reverse since the values of the bases are reversed
    num = num [::-1] #always start counting from last digit anyways
    index = 0 #traverse through list values
    result = 0
    for i in range (len(num)):
        result += int(num [index]) * (base**index) #for example, the last digit is just 1x2^0
        index +=1
    return result

# test cases
print(get_base_number('10011',2))  # should be 19
print(get_base_number('3202',5))   # should be 427
print(get_base_number('611023',7))
