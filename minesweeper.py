from tkinter import *
# for some reason the previous line doesn't import messagebox in Python 3.6+
from tkinter import messagebox
import random

class GridSquare(Label):
    '''represents a square in Minesweeper'''

    # colors for the various numbers in the grid
    colormap = ['','blue','darkgreen','red','purple','maroon','cyan','black','dim gray']

    def __init__(self,master):
        '''GridSquare(master) -> GridSquare
        returns a new Minesweeper grid square'''
        Label.__init__(self,master,width=2,height=1,relief=RAISED,font=('Arial',18))
        # set the status flags
        self.isBomb = False
        self.isFlagged = False
        self.isExposed = False
        # set up the mouse click listeners
        self.bind('<Button-1>',self.expose)
        self.bind('<Button-2>',self.flag)
        self.bind('<Button-3>',self.flag)

    def is_exposed(self):
        '''GridSquare.is_exposed() -> bool
        returns True if the square has been exposed'''
        return self.isExposed

    def is_bomb(self):
        '''GridSquare.is_bomb() -> bool
        returns True if the square contains a bomb'''
        return self.isBomb

    def make_bomb(self):
        '''GridSquare.make_bomb()
        puts a bomb in the grid square'''
        self.isBomb = True

    def make_exposed(self):
        '''GridSquare.make_exposed()
        sets the square's status to exposed'''
        self.isExposed = True

    def set_square(self,value,color):
        '''GridSquare.set_square(value,color)
        exposes the square with the provided value and color'''
        self.isExposed = True
        # expose the square
        self['relief'] = SUNKEN
        self['bg'] = 'gray'
        # set the value
        if value==0:
            self['text'] = ''
        else:
            self['text'] = str(value)
            self['fg'] = color
        # update the game's count of exposed squares
        self.master.decrease_exposed_count()

    def set_bomb(self):
        '''GridSquare.set_bomb()
        display a bomb that just exploded'''
        self['text'] = '*'
        self['bg'] = 'red'

    def expose_square(self,isEndGame):
        '''GridSquare.expose_square(isEndGame)
        exposes an unexposed, unflagged square
        isEndGame is True if the player has won (and this is cleaning up the board)
        isEndGame is False if the game is still in progress'''
        # only exposed squares that are still unexposed and unflagged
        if not self.isFlagged and not self.isExposed:
            if self.isBomb: # bomb
                self.set_bomb()
                if not isEndGame:
                    # player set off a bomb -- this ends the game with a loss
                    self.master.end_game(False)
            elif not isEndGame: # don't expose non-bomb squares at the end
                value = self.master.get_value(self)
                # set the square to display its value
                self.set_square(value,self.colormap[value])

    def expose(self,event):
        '''self.expose(event)
        handler for left-mouse click'''
        # expose the square just clicked on
        self.expose_square(False)

    def flag(self,event):
        '''self.flag(event)
        handler for right-mouse click
        toggles the flag on the square and adjusts the remaining bomb count
        (does nothing if the square is already exposed)'''
        if not self.isExposed:  # cannot flag/unflag unless unexposed
            if not self.isFlagged:
                # turn flag from off to on
                self['text'] = '*'
                self.master.decrease_bombcount()
            else:
                # turn flag from on to off
                self['text'] = ''
                self.master.increase_bombcount()
            # reverse the flag boolean
            self.isFlagged = not self.isFlagged

    
class Minesweeper(Frame):
    '''represents a minesweeper game'''

    def __init__(self,master,width,height,numBombs):
        '''Minesweeper(master,width,height,numBombs) -> Minesweeper
        creates a new Minesweeper game
        board size is width x height
        numbBombs is the number of bombs'''
        # initialize a Frame widget and display it
        Frame.__init__(self,master,bg='black')
        self.grid()
        # store game data
        self.width = width
        self.height = height
        # need to expose this many square to win
        self.toBeExposedCount = (width*height)-numBombs
        # create squares
        self.squares = {}  # used to store the GridSquare objects
        squareList = []  # used to pick the squares that contain bombs
        for row in range(height):
            for col in range(width):
                self.squares[(row,col)] = GridSquare(self)
                self.squares[(row,col)].grid(row=row,column=col)
                squareList.append((row,col))
        # create bombs
        for n in range(numBombs):
            # select a square, put a bomb in it
            bombsquare = random.choice(squareList)
            self.squares[bombsquare].make_bomb()
            squareList.remove(bombsquare)
        # set up control variable and label for remaining bomb count
        self.bombCount = IntVar()
        self.bombCount.set(numBombs)
        self.bombLabel = Label(self,textvariable=self.bombCount,font=('Arial',24))
        self.bombLabel.grid(row=height,column=0,columnspan=width)

    def increase_bombcount(self):
        '''Minesweeper.increase_bombcount()
        increases the remaining bomb count by 1'''
        self.bombCount.set(self.bombCount.get()+1)

    def decrease_bombcount(self):
        '''Minesweeper.decrease_bombcount()
        decreases the remaining bomb count by 1'''
        self.bombCount.set(self.bombCount.get()-1)

    def decrease_exposed_count(self):
        '''Minesweeper.decrease_exposed_count()
        decreases the exposed square count by 1
        If this count hits 0, the player has exposed all the non-bomb
          squares and has won the game'''
        self.toBeExposedCount -= 1
        # check for a win
        if self.toBeExposedCount == 0:
            self.end_game(True)

    def get_value(self,square):
        '''Minesweeper.get_value(square) -> int
        computes the number of adjacent bombs to the square
        If no bombs adjacent, also exposes all adjacent squares'''
        # don't do anything if the square is already exposed
        if square.is_exposed():
            return 0
        # find coordinates of square
        for (row,col) in self.squares.keys():
            if self.squares[(row,col)] == square:
                break
        bombCount = 0  # to store count of adjacent bombs
        # look at adjacent squares, count bombs
        for nrow in [row-1,row,row+1]:
            for ncol in [col-1,col,col+1]:
                # make sure it's in the grid, and check for a bomb
                #  if so, add 1 to the count
                if (0 <= nrow < self.height) and (0 <= ncol < self.width) \
                   and self.squares[(nrow,ncol)].is_bomb():
                    bombCount += 1
        if bombCount == 0:  # expose adjacent squares
            square.make_exposed()  # make this square exposed (to avoid infinite loop!)
            for nrow in [row-1,row,row+1]:
                for ncol in [col-1,col,col+1]:
                    # make sure it's in the grid; if so, expose it
                    if (0 <= nrow < self.height) and (0 <= ncol < self.width):
                        self.squares[(nrow,ncol)].expose_square(False)
        return bombCount

    def end_game(self,hasWon):
        '''Minesweeper.end_game(hasWon)
        performs end-of-game tasks
        hasWon is True if the player won, False if clicked on a bomb'''
        # turn off the left-button listeners
        for coord in self.squares:
            self.squares[coord].unbind('<Button-1>')
        # check if the player has won
        if hasWon:
            messagebox.showinfo('Minesweeper','Congratulations -- you won!',parent=self)
        else:
            messagebox.showerror('Minesweeper','KABOOM! You lose.',parent=self)
            # expose all the bombs
            for coord in self.squares:
                if self.squares[coord].is_bomb():
                    self.squares[coord].expose_square(True)


# main game
def play_minesweeper(width,height,numBombs):
    '''play_minesweeper(width,height,numBombs)
    starts a new game of minesweeper
    uses a width x height board with numBombs bombs'''
    root = Tk()
    root.title('Minesweeper')
    Minesweeper(root,width,height,numBombs)
    root.mainloop()

play_minesweeper(12,15,10)