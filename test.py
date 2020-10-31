from tkinter import *
import tkinter.messagebox
import random

class MineSweeperGrid (Frame): 
    '''creates a minesweeper grid'''
    def __init__(self,master,width, height, numBombs):
        '''SudokuGrid(master)
        creates a new blank Sudoku grid'''
        # initialize a new Frame
        Frame.__init__(self,master,bg='black')
        self.grid()
        
        self.numBombs = numBombs
        self.cells = {} #{(coordinates):button}
        #add the coordinates and the button to the dictionary
        for rows in range (width):
            for columns in range (height):  #NOTE to self: rows is Y and columns is X*******
                self.cells [(rows, columns)] = MineButtons (self,False) #grid them as false first and then randomly re-grid them as true 
                self.cells [(rows, columns)].grid (row= rows, column = columns)

       
        self.bombs = []  #have all the bombs here so that we dont place one in the same place (list since we only want coordinate)
        for bombs in range (numBombs): #place random bombs
            x = random.randrange (width)
            y = random.randrange (height)

            if (x,y) not in self.bombs:
                self.cells [(x,y)] = MineButtons (self, True, self.bombs, self.cells)
                self.cells [(x,y)].grid (row = x, column = y)
                self.bombs.append ((x,y))
            else:
                while (x,y) in self.bombs: #keep going until we can put it in a spot without bombs
                    x = random.randrange (width)
                    y = random.randrange (height)

                    if (x,y) not in self.bombs:
                        self.cells [(x,y)] = MineButtons (self, True, self.bombs, self.cells)
                        self.cells [(x,y)].grid (row = x, column = y)
                        self.bombs.append ((x,y))
                        break #break out of the while loop
        self.bottom = Frame(self, bg='black') #frame to hold text widget
        self.bottom.grid (row = 12 + 1, column = 0, columnspan = 10)
        
        self.bombLabel = Label(self.bottom, bg='white', font = ('Courier New', 24, \
                                       'bold'), fg = 'red3', width=2,  text = 15)
        self.bombLabel.grid ()
        
class MineButtons (MineSweeperGrid):
    '''creates a mine sweeper label/button'''
    def __init__ (self,master, isBomb, bombs = [], cells = {}): #isBomb checks whether square is a bomb or not
        #other optional parameters is to get variables from parents class
         Label.__init__(self, master, relief = RAISED,height = 1, width = 2)
         self.isBomb = isBomb
         self.bombs = bombs
         self.cells = cells
         self.bind('<Button-1>',self.expose)
         self.bind('<Button-3>',self.highlight)
         
    def expose (self,event):
        '''changes the relief/color of a clicked mine sweeper button'''
        self.focus_set ()
        if self.ifBomb (): #player clicks on a bomb and loses
            self ['text'] = '*'
            self ['bg'] = 'red'
            self.showBombs ()
            tkinter.messagebox.showerror('Minesweeper','KABOOM! You lose.',parent=self)
        else:
            self.config (relief = SUNKEN)
            self ['bg'] = 'gray'
            
    def highlight (self,event):
        '''put an asterisk over a minesweep square'''
        self.focus_set ()
        self ['text'] = '*'

        
    def ifBomb (self):
        '''tells whether a square is a bomb or not'''
        return self.isBomb

    def showBombs (self):
        '''shows where all of the bombs are located'''
        for coords in self.bombs: #user method from parent class
            self.cells [coords] ['text'] = '*'
            self.cells [coords] ['bg'] = 'red'

def play_minesweeper (width, height, numBombs):
    '''plays minesweeper with set measurements'''
    root = Tk()
    root.title('Minesweeper')
    sg = MineSweeperGrid(root,width,height, numBombs)
    root.mainloop()    
    
play_minesweeper (12,10,15)
