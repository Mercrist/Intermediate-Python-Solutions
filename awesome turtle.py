import turtle
class SuperAwesomeTurtle(turtle.Turtle):
    '''a super awesome turtle!'''
    def __init__ (self):
        '''intitialize turtles and variables'''
        turtle.Turtle.__init__(self)
        self.go = True #keep track if we want the turtle to move or not
        self.time = 40 #set everything initially to 25 units/s
        self.forw = 1 #how mych we want to go forward
        self.speed = 0 #how fast we want to go
        self.getscreen().onkey(self.stop,'s') #stops the turtle
        self.getscreen().onkey(self.increase,'Up') #increase speed
        self.getscreen().onkey(self.decrease,'Down') #decrease speed
        self.getscreen().onkey(self.goright,'Right') #go right
        self.getscreen().onkey(self.goleft,'Left') #go left
        self.getscreen().onkey(self.terminate,'q') #completely closes the program
        self.goforward()
        
    def goforward(self):
        '''goes forward for positive values'''
        if self.go: #runs as long as go is true (as long as we want the turtle to move)
            self.forward (self.forw) #when negative it goes backwards
        self.getscreen().ontimer(self.goforward,self.time)

    def goleft (self):
        '''turns a turtle 90 degrees to the left'''
        self.left (90)
        
    def goright (self):
        '''turns a turtle 90 degrees to the right'''
        self.right (90)
    
    def increase (self):
        '''increases turtle speed by 25 units/second'''
        self.speed += 40
        self.forw +=1 #increase forward as well to increase by a full 25 units/s
        self.calculate_speed ()

    def decrease (self):
        '''increases turtle speed by 25 units/second'''
        self.speed -= 40
        self.forw -= 1
        self.calculate_speed ()
    
    def calculate_speed (self):
        '''gives us the amount of time we need to go a certain speed'''
        try:
            self.time = abs(round (1000/self.speed)) #(1000/120)*3 = 25 units/second
        except ZeroDivisionError:
            self.time = 0            

    def stop(self):
        '''stops the turtle from moving'''
        self.go = False

    def terminate (self):
        '''completely closes the program'''
        self.getscreen().bye ()
        
wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()

