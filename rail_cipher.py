def encipher_fence(plaintext,numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    textList = list (plaintext) #maps each character to a number
    index = 0
    railNum = 0
    cipher = ""

    railLists = [] #create a list with lists for each rail

    for i in range (numRails):
        railLists.append ([])
    
    for o in range (numRails): #for each rail in the dictionary

        for p in range (len(textList)): #for each character in the sentence
            railLists [o].append (textList [index]) #append that value to the corresponding rail 
            index += numRails

            if index > (len (textList)-1): #if the index goes out of range, it's time to restart at the next rail
                railNum+=1
                index = railNum
                break #so it goes to the outer loop

    index = len(railLists)-1
    for k in range(len(railLists)): #add the strings backwards
        cipher += "".join (railLists [index])
        index -=1
        
    return cipher

def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    cipherList = list (ciphertext) #assign each char to a number and split it into the according rails
    rails = [] #list with all our rails
    divisor = numRails #variable to divide by the number of rails left to remove

    for i in range (numRails): #for each rail
        if i == numRails-1: #on the final iteration, append the whole list
            rails.append (cipherList)
            break
        
        rails.append (cipherList[:((len (cipherList)//divisor))]) #remove each rail and assign it to a list
        del cipherList[:((len (cipherList)//divisor))]
        divisor -= 1

    rails = rails [::-1] #reverse the rails into the original order
    railIndex = 0
    charIndex = 0
    originalText = ""
    for p in range (len(ciphertext)): #for each character, add the matching indexes of each list into a string
        try: #in case charIndex goes out of range
            originalText += rails [railIndex][charIndex]
        except IndexError:
            break
            
        railIndex +=1

        if railIndex >= numRails: #if it goes out of the rail range
            railIndex = 0
            charIndex +=1 #goes to next character after first char of each list is obtained

        if charIndex >= len (rails [railIndex]): #if the index is out of range, stop
            break
            
    return originalText

def decode_text(ciphertext,wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''
    outFile = open (wordfilename, 'r')
    outFile = outFile.readlines ()
    points = 0 #determine which text has the greater number of words
    maxPoints = 0
    decoded = "" #text to return
    
    for rails in range (11): #decode the text with a different rail each time
        text = decipher_fence (ciphertext, rails)
        text = text.split () #split text into individual words
        
        for word in text: #for every word, check if it's in dictionary
            if word + "\n" in outFile: #if it's in file, increase the amount of points the word has
                points +=1
                
        if points > maxPoints: #found word with highest amount of words
            maxPoints = points
            decoded = " ".join (text)
        points = 0 #reset points

    return decoded     
    outFile.close ()
    
# test cases

# enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou

# deciphering
print(decipher_fence("hsi  etTi sats.",2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s",3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print... we'll let you find out!
