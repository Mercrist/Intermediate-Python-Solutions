values = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,
          'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,
          'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}

index = 0 #cycle through letters in words

points = 0 #sum all the points in the word
wordPoints = {} #list all the points and return the highest one

outFile = open ('wordlist.txt', 'r') #open the file for reading

for line in outFile:
    line = line.strip ('\n') 
    line = line.upper () #uppercase to match with dic
    
    if "Z" not in line and len (line) == 7:
        line = list (line) #split into a list
        for char in line: #for every character in the word use dic 
            points += values[line [index]]
            index +=1
        wordPoints.update ({''.join(line):points})#add points and reset all the variables
        points = 0
        index = 0
outFile.close() #close the file
print(max(wordPoints, key=wordPoints.get)) #prints the key with the highest value
