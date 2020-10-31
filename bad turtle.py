import turtle
import random

class MisbehavingTurtle(turtle.Turtle):
    '''implements a naughty turtle'''

    # need to overload the left and right operators only

    def left(self,amt):
        '''MisbehavingTurtle.left(amt)
        75% of the time turns the turtle left
        25% of the time turns the turtle right'''
        if random.random() < 0.25:
            turtle.Turtle.right(self,amt)
        else:
            turtle.Turtle.left(self,amt)

    def right(self,amt):
        '''MisbehavingTurtle.right(amt)
        75% of the time turns the turtle right
        25% of the time turns the turtle left'''
        if random.random() < 0.25:
            turtle.Turtle.left(self,amt)
        else:
            turtle.Turtle.right(self,amt)

# test case
# drawing an octagon and a square
def drawing_test(t):
    '''drawing_test(t)
     draws an octagon and square with t'''
    for i in range(8):
        t.forward(30)
        t.left(45)
    t.right(45)
    for i in range(4):
        t.forward(50)
        t.right(90)
        
# one nice turtle and one not-so-nice turtle
wn = turtle.Screen()
sugar = turtle.Turtle()
sugar.color('green')
drawing_test(sugar)
spice = MisbehavingTurtle()
spice.color('red')
drawing_test(spice)
wn.mainloop()
