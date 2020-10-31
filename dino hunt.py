import random

### Die class that we previously wrote ###

class Die:
    '''Die class'''

    def __init__(self,sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides,int):
            self.numSides = sides
            self.sides = list(range(1,sides+1))
        else:  # use the list/tuple provided 
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A '+str(self.numSides)+'-sided die with'+\
               str(self.get_top())+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

### end Die class ###

class DinoDie(Die):
    '''implements one die for Dino Hunt'''
    def __init__ (self, color): #override since it's a different type of die//color is to check which die to create
        if color == "green":
            self.sides = ['dino', 'dino', 'dino', 'leaf', 'leaf', 'foot']
        elif color == "yellow":
            self.sides = ['dino', 'dino', 'leaf', 'leaf', 'foot', 'foot']
        elif color == "red":
            self.sides = ['dino', 'leaf', 'leaf', 'foot', 'foot', 'foot']
        self.numSides = color #set this to color so we don't have to re-edit the Die function
        self.roll ()

    def __str__(self): #overload so the statement makes more sense
        '''str(Die) -> str
        string representation of Die'''
        return 'A '+str(self.numSides)+' Dino die with a '+\
               str(self.get_top())+' on top.'

    def roll (self): #overload roll since numSides isnt an int
        self.top = self.sides[random.randrange(0,6)]      

class DinoPlayer:
    '''implements a player of Dino Hunt'''
    def __init__ (self,name, dinos = 0, feet = 0):
        self.name = name
        self.dinos = dinos
        self.feet = feet #to keep track of all the dinos and feet

    def __str__ (self):
        '''returns a player's name'''
        return self.name
    
    def player_turn (self, die):
        '''the actions a player takes during one round of dino hunt'''
        n = 3 #represents 3 dice for the rolling function
        skip = False
        total = 0
        greenIndex = 0
        yellowIndex = 1
        redIndex = 2
        green = str(len(die [greenIndex]))
        yellow = str(len(die [yellowIndex]))
        red = str(len(die [redIndex])) #easier to modify when lists get empty
        for i in range (n):
            total += len (die [i])
        print (self.name + " it's your turn!")
        print ("You have " + str(total) + " dice remaining.")
        string =  green+" green, " + yellow+ " yellow, " + red + " red."
        print (string)
       
        while True: #keep this loop until player doesnt want to throw
            input ("\nPress enter to select dice and roll.")
            for rolls in range (3): #roll a random die, check the roll, continue
                index = random.randrange (0,n)
                try:
                    die [index][-1].roll () #roll from the remaining lists
                except IndexError:
                    if die.index ([]) == greenIndex: #when green dice are empty
                        skip = True
                        green = str(0)
                        yellow = str(len(die [yellowIndex]))
                        red = str(len(die [redIndex]))
                        string = green+" green, " + yellow+ " yellow, " + red + " red."
                    elif die.index ([]) == yellowIndex:
                        skip = True
                        yellow = str(0)
                        green = str(len(die [greenIndex]))
                        red = str(len(die [redIndex]))
                        string = green+" green, " + yellow+ " yellow, " + red + " red."
                    elif die.index ([]) == redIndex:
                        skip = True
                        red = str(0)
                        green = str(len(die [greenIndex]))
                        yellow = str(len(die [yellowIndex]))
                        string = green+" green, " + yellow+ " yellow, " + red + " red."
                    die.append(die.pop(die.index([]))) #take any empty list and move it to the end
                    n-=1
                    index = random.randrange (0,n)
                    try:
                        die [index][-1].roll () #try this again now that index has been moved
                    except IndexError: #no dice left
                        print ("All dice have been used!")
                        return (die, points)
                print ("  "+str(die [index][-1])) 

                if die [index][-1].get_top () == "foot":
                    self.feet +=1
                    if self.feet == 3: #if player gets stomped
                        print ("Too bad -- you got stomped!")
                        self.dinos = 0
                        self.feet = 0
                        points = 0
                        return (die, points) #break out of this players turn and return the dies that we have
                    del die [index][-1]
          
                elif die [index][-1].get_top () == "dino": #calculate points and do nothing if leaves
                    self.dinos +=1 
                    del die [index][-1] #remove this roll
                    
            total = 0
            for i in range (n):
                total += len (die [i])#re-update total
            print ("This turn so far: {0} dinos and {1} feet.".format (self.dinos, self.feet))
            print ("You have {} dice remaining.".format (total))
            if skip is not True: #so that it doesnt re modify them after the lists get empty
                green = str(len(die [greenIndex]))
                yellow = str(len(die [yellowIndex]))
                red = str(len(die [redIndex])) #update variables
                string =  green+" green, " + yellow+ " yellow, " + red + " red."
            print (string)
            userInput = input ("Do you want to roll again? (y/n)")
            if userInput == "n": #once the user doesnt want to roll anymore
                points = self.dinos
                self.dinos = 0 #reset values
                self.feet = 0
                return (die, points) #return a tuple with these values to unpack 
        
def play_dino_hunt(numPlayers,numRounds):
    '''play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player'''
    playerList = []
    playerPoints = []
    playerPointIndex = 0 #to cycle through all of the player points without modifying the other player index
    numGreen = [DinoDie ("green") for dice in range (6)] #will have to access by index
    numYellow = [DinoDie ("yellow") for dice in range (4)]
    numRed = [DinoDie ("red") for dice in range (3)]
    totalDie = [numGreen, numYellow, numRed]
    
    for i in range (numPlayers): #gets player names and stores them into a list
        name = input ("Player " +str (i+1)+ " please enter your name: ")
        playerList.append(DinoPlayer(name))
        playerPoints.append (0) #give a score for each player

    for rounds in range (numRounds):
        print ("\n--Round {}--\n".format (rounds+1))
        for player in range(len(playerList)): #have everyone play once and record their points    
            results = playerList [player].player_turn (totalDie) #results keeps the tuple of the dice and the points
            playerPoints [player] += results [1] #adds the points
            totalDie = results [0] #re-define the new dice
            print ("\n") #to seperate the points from the rest
            for points in range (len(playerPoints)):
                print ("{0} has {1} points.".format (playerList [playerPointIndex], playerPoints [points]))
                playerPointIndex +=1
            playerPointIndex = 0 #reset
            print ("\n")
        numGreen = [DinoDie ("green") for dice in range (6)] #reset dice
        numYellow = [DinoDie ("yellow") for dice in range (4)]
        numRed = [DinoDie ("red") for dice in range (3)]
        totalDie = [numGreen, numYellow, numRed]
        
    winnerIndex = playerPoints.index(max(playerPoints))
    print("{} wins the match with {} points!".format (playerList [winnerIndex], max(playerPoints)))
        
play_dino_hunt(2,4)
    
                         
