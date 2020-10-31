def anagram(inputString):
    '''anagram(inputString) -> list
    returns list of all variations of the input string'''
    # base case
    if len(inputString) == 1:
        return [inputString[:]]
    # recursive step
    outputList = []  # to store different combination of strings
    for index in range(len(inputString)):
        restOfList = inputString[:index]+inputString[index+1:]
        combinations = anagram(restOfList)
        
        for tail in combinations:
            outputList.append(str(inputString[index])+tail)
    return outputList

def jumble_solve (string, files):
    '''anagram(inputString) -> string
       returns the unscrabled jumbo solution'''
    combs = anagram (string) #sees all the possible combinations of that string
    file = open (files, "r")
    file = file.readlines ()
    for words in combs:
        if words.lower () +"\n" in file: #.lower since the jumble words are in capital
            return words

print (jumble_solve("CHWAT", "wordlist.txt"))
print (jumble_solve("RAROM", "wordlist.txt"))
print (jumble_solve("CEPLIN", "wordlist.txt"))
print (jumble_solve("YAFLIM", "wordlist.txt"))
