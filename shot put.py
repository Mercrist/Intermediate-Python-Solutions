from tkinter import *
import random
 
class GUIDie(Canvas):
    '''6-sided Die class for GUI'''
 
    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['red','black']*5):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1
 
    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top-1]
 
    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1,7)
        self.draw()
        return self.top 
 
    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1,1)],
                   [(0,0),(2,2)],
                   [(0,0),(1,1),(2,2)],
                   [(0,0),(0,2),(2,0),(2,2)],
                   [(0,0),(0,2),(1,1),(2,0),(2,2)],
                   [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)]]
        for location in pipList[self.top-1]:
            self.draw_pip(location,self.colorList[self.top-1])
 
    def draw_pip(self,location,color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx,centery) = (17+20*location[1],17+20*location[0])  # center
        self.create_oval(centerx-5,centery-5,centerx+5,centery+5,fill=color)
 
    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)
            
class ShotPut(Frame, GUIDie):
    '''frame and game for shot put'''

    def __init__(self,master,name):
        '''creates a new shot put game and
           initializes all the variables'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self,text=name,font=('Arial',18)).grid(columnspan=2,sticky=W)
        # set up score and rerolls
        self.attemptscoreLabel = Label(self,text='Attempt #1 Score: 0',font=('Arial',18))
        self.attemptscoreLabel.grid(row=0,column=2,columnspan=3)
        self.scoreLabel = Label(self,text='High Score: 0',font=('Arial',18))
        self.scoreLabel.grid(row=0,column=6, columnspan = 2)
        # set up all the die and buttons 
        self.dice = []
        self.columnNum = 0 #moves the roll button(s) after each click
        self.score = 0
        self.rolled = 0 #keeps track of what was rolled to prevent 1's
        self.highScore = 0 #high score
        self.round = 1 #only play up to 3 rounds
        for i in range (8):
            self.dice.append(GUIDie(self,[1,2,3,4,5,6],['red']+['black']*5))
            self.dice[i].grid(row=1,column=i)
            
        self.rollButton = Button(self,text='Roll',state=ACTIVE,\
                                             command=self.roll)
        self.rollButton.grid (row = 2, column = self.columnNum)

        self.stopButton = Button(self,text='Stop',state=DISABLED,\
                                             command=self.stop)
        self.stopButton.grid (row = 3, column = self.columnNum)
        
    def roll (self):
        '''roll the dice and get scores'''
        self.rolled = self.dice [self.columnNum].roll () #index and column numbers are the same
        if self.rolled != 1:
            self.score += self.rolled
            self.attemptscoreLabel ['text'] = "Attempt#{} Score:{}".format (self.round, self.score)
        
            if self.columnNum == 0: # if it's the first throw
                self.stopButton ['state'] = ACTIVE
                
            self.columnNum +=1 #move the buttons
            if self.columnNum  < 8: #all dice were rolled
                self.rollButton.grid (row = 2, column = self.columnNum)
                self.stopButton.grid (row = 3, column = self.columnNum)
            elif self.columnNum == 8:
                self.rollButton ['state'] = DISABLED
           
        elif self.rolled == 1:
            self.score = 0 #lose all points gained during that turn
            self.rollButton ['state'] = DISABLED #so the user can't roll anymore
            self.stopButton ['state'] = ACTIVE #make sure the user can click and go to the next round
            self.stopButton ['text'] = 'FOUL'       

    def stop (self):
        '''stop the dice and get scores and foul'''
        self.highScore += self.score #get all points then reset everything and go to next round
        self.score = 0
        self.scoreLabel ['text'] = 'High Score: '+str (self.highScore)
        self.stopButton ['text'] = 'Stop'
        self.round +=1
        if self.round < 4:
            for dice in self.dice: #erase all the dice
                dice.erase ()
            self.attemptscoreLabel ['text'] = 'Attempt #{} Score: {}'.format (self.round, self.score)
            self.columnNum = 0 #reset to the beginning
            self.rollButton ['state'] = ACTIVE
            self.stopButton ['state'] = DISABLED
            self.rollButton.grid (row = 2, column = self.columnNum)
            self.stopButton.grid (row = 3, column = self.columnNum)
            
        elif self.round == 4: #ends the game
            self.rollButton.grid_remove ()
            self.stopButton.grid_remove ()
            self.attemptscoreLabel['text'] = 'Game Over'
        
# play the game
name = input("Enter your name: ")
root = Tk()
root.title('Shot Put')
game = ShotPut(root,name)
game.mainloop()
