class Jar:
    '''creates a jar and adds all of its functionalities'''
    def __init__ (self, capacity):
        self.liters = capacity #initialize a variable to keep track of the jar's capacity
        self.rem = capacity #shows how much is remaining in the jars

    def __str__ (self): #return the jar and how many liters it holds
        left = "This " + str (self.liters) + " liter jug has " + str (self.rem) + " liters left." #shows how many liters are left 
        return left

    def set (self, amount): #set what's remaining to a determined value
        self.rem = amount

    def how_much (self): #returns the amount of liters the jar has
        return self.rem

    def maxAmount (self): #returns the amx capacity of that jar
        return self.liters

    def fill (self): #fills the jar
        if self.rem != self.liters: #if it isnt full
            self.rem = self.liters #fill it
            print ("Jar has been filled.")
        else:
            print ("Jar is already full.")

    def empty (self): #empties the jar
        if self.rem != 0: #if the jar isnt empty
            self.rem = 0
            print ("Jar is now empty.")
        else:
            print ("Jar is already empty.")

    def increase (self, amount): #increases jar capacity by that amount
        self.rem += amount

    def pour (self): #pours water into other jars (algorithm for emptying in program below/// amount is so we can use it later
        global amount #so we can reuse value
        amount = self.rem
        self.rem = 0 #empty entire jar
        return amount 

def pour (jar1, jar2): #build it again but so that we can use if with two jars
    jar1. pour () #empties the jar and gives us the amount it had
    jar2.increase (amount)

    if jar2.how_much () <= jar2.maxAmount (): #a is empty and b is full
        final = "Jar A has been poured into B. Jar A has "+ str (jar1.how_much ()) + " liters and Jar B has " + str(jar2.how_much ()) + " liters."
        return final

    else: #if jar b gets filled but jar a isn't completely empty
        jar1.set (jar2.how_much () - jar2.maxAmount ()) #sets jar 1 to what jar2 has minus the maximum amount
        jar2.set (jar2.maxAmount ()) #set it to the maximum amount

        final = "Jar A has been poured into B. Jar A has "+ str (jar1.how_much ()) + " liters and Jar B has " + str(jar2.how_much ()) + " liters."
        return final

#algorithm is:
#empty b
#pour from a to b
#fill a
#pour from a to b
#repeat        
def solve (jar1, jar2, jar2Amount): #jar2Amount is how much water we want jar2 to have
    if jar2.how_much () == jar2Amount:
        print ("Solved! Jar B now has " +str (jar2Amount) + " liters.")
        return #exit the function
    jar2.empty ()
    print (jar2)
    print (pour (jar1, jar2))
    jar1.fill ()
    print (jar1)
    print (pour (jar1, jar2))
    return solve (jar1, jar2, jar2Amount) #recursion

a = Jar (3) #initialize jars
b = Jar (5)

solve (a,b,4)
