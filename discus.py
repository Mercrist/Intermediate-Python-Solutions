from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
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


class GUIFreezeableDie(GUIDie):
    '''a GUIDie that can be "frozen" so that it can't be rolled'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIFreezeableDie(master,[valueList,colorList]) -> GUIFreezeableDie
        creates a GUI 6-sided freeze-able die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        GUIDie.__init__(self,master,valueList,colorList)
        self.isFrozen = False  # die starts out unfrozen

    def is_frozen(self):
        '''GUIFreezeableDie.is_frozen() -> bool
        returns True if the die is frozen, False otherwise'''
        return self.isFrozen
    
    def toggle_freeze(self):
        '''GUIFreezeableDie.toggle_freeze()
        toggles the frozen status'''
        self.isFrozen = not self.isFrozen
        if self.isFrozen:
            self['bg'] = 'gray'
        else:
            self['bg'] = 'white'

    def roll(self):
        '''GuiFreezeableDie.roll()
        overloads GUIDie.roll() to not allow a roll if frozen'''
        if not self.isFrozen:
            GUIDie.roll(self)


class DecathDiscusFrame(Frame):
    '''frame for a game of Discus'''

    def __init__(self,master,name):
        '''DecathDiscusFrame(master,name) -> DecathDiscusFrame
        creates a new Discus frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self,text=name,font=('Arial',18)).grid(columnspan=2,sticky=W)
        # set up score and rerolls
        self.attemptscoreLabel = Label(self,text='Attempt #1 Score: 0',font=('Arial',18))
        self.attemptscoreLabel.grid(row=0,column=2,columnspan=3)
        self.scoreLabel = Label(self,text='High Score: 0',font=('Arial',18))
        self.scoreLabel.grid(row=0,column=5)
        # initialize game data
        self.score = 0
        self.attempt = 1
        self.numFrozen = -1
        # set up dice and freeze buttons
        self.dice = []
        self.freezeButtons = []
        for n in range(5):
            self.dice.append(GUIFreezeableDie(self,[0,2,0,4,0,6],['red','black']*3))
            self.dice[n].grid(row=1,column=n)
            self.freezeButtons.append(Button(self,text='Freeze',state=DISABLED,\
                                             command=self.dice[n].toggle_freeze))
            self.freezeButtons[n].grid(row=2,column=n)
        # set up roll/stop buttons
        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=1,column=5)
        self.stopButton = Button(self,text='Stop',state=DISABLED,command=self.stop_attempt)
        self.stopButton.grid(row=2,column=5)
        # freeze warning label
        self.messageLabel = Label(self,text='Click Roll button to start',font=('Arial',18))
        self.messageLabel.grid(row=3,column=0,columnspan=5)

    def roll(self):
        '''DecathDiscusFrame.roll()
        handler method for the roll button click'''
        currentlyFrozen = len([die for die in self.dice if die.is_frozen()])
        if currentlyFrozen <= self.numFrozen:
            # need to freeze a die before can roll
            self.messageLabel['text'] = 'You must freeze a die to reroll'
            return
        # clear label and activate stop button
        self.messageLabel['text'] = 'Click Stop button to keep'
        self.stopButton['state'] = ACTIVE
        # roll all dice
        for die in self.dice:
            die.roll()
        # check frozen dice -- adjust freeze buttons to only allow freezing
        #  on not-already-frozen scoring dice
        self.numFrozen = 0
        for n in range(5):
            if self.dice[n].is_frozen():
                self.freezeButtons[n]['state'] = DISABLED
                self.numFrozen += 1
            elif self.dice[n].get_top() == 0:
                self.freezeButtons[n]['state'] = DISABLED
            else:
                self.freezeButtons[n]['state'] = ACTIVE
        # need an unfrozen die to score to avoid a foul
        self.rollFouled = True
        for n in range(5):
            if not self.dice[n].is_frozen() and self.dice[n].get_top() > 0:
                self.rollFouled = False  # found a good die
        # foul 
        if self.rollFouled:
            self.attemptscoreLabel['text'] = 'FOULED ATTEMPT'
            self.messageLabel['text'] = 'Click FOUL button to continue'
            self.rollButton['state'] = DISABLED
            self.stopButton['text'] = 'FOUL'
            self.stopButton['state'] = ACTIVE
        else:
            attemptscore = sum([die.get_top() for die in self.dice])
            self.attemptscoreLabel['text'] = 'Attempt #{} Score: {}'.format( \
                                             self.attempt,attemptscore)
                
    def stop_attempt(self):
        '''DecathDiscusFrame.stop_attempt()
        handler method for the stop button click'''
        # check for foul
        if self.rollFouled:
            attemptscore = 0
        else:
            attemptscore = sum([die.get_top() for die in self.dice])
        if attemptscore > self.score:  # new high score
            self.score = attemptscore
            self.scoreLabel['text'] = 'High Score: '+str(self.score)
        self.messageLabel['text'] = 'Click Roll button to start'
        self.attempt += 1  # go to next attempt
        if self.attempt <= 3:  # reset dice,buttons,labels
            for n in range(5):
                self.dice[n] = (GUIFreezeableDie(self,[0,2,0,4,0,6],['red','black']*3))
                self.dice[n].grid(row=1,column=n)
                self.freezeButtons[n]['state'] = DISABLED
                self.freezeButtons[n]['command'] = self.dice[n].toggle_freeze
            self.numFrozen = -1
            self.attemptscoreLabel['text'] = 'Attempt #{} Score: 0'.format( \
                                             self.attempt)
            self.rollButton['state'] = ACTIVE
            self.stopButton['state'] = DISABLED
            self.stopButton['text'] = 'Stop'
        else:  # game over
            self.stopButton.grid_remove()
            self.rollButton.grid_remove()
            self.messageLabel.grid_remove()
            self.attemptscoreLabel['text'] = 'Game over'


# play the game
name = input("Enter your name: ")
root = Tk()
root.title('Discus')
game = DecathDiscusFrame(root,name)
game.mainloop()
