class Elevator:
    '''Represents a simple elevator'''

    def __init__(self, startFloor, startDoorsOpen,passengers):
        '''Elevator(startFloor, startDoorsOpen) -> Elevator
        Constructs an Elevator
        startFloor: int giving the starting floor
        startDoorsOpen: bool giving the starting doors 
                    (True = 'open')'''
        self.floor = startFloor  # store floor attribute
        self.doorsOpen = startDoorsOpen  # store doors attribute
        self.passengers = passengers

    def __str__(self):
        '''str(Elevator) -> str
        Returns a string giving the floor and state of the doors.'''
        answer = 'doors '         # will contain string to return
        if self.doorsOpen:        # if doors open
            answer += 'open'      # say so
        else:                     # if doors closed
            answer += 'closed'    # say that too
        answer += ', floor '      # this is in every answer
        answer += str(self.floor) # add floor number
        if self.passengers != []: #if anyone is onboard
            isOn = self.passengers [0] +" ".join (self.passengers [1:]) #returns all the passengers on board
            answer += " "+str(isOn) #to seperate between floor and passenger list and such
        else:
            answer += " No passengers"
        return answer

    def open_doors(self):
        '''Elevator.open_doors()
        Opens the doors by setting doors attribute to True.'''
        self.doorsOpen = True # set doors to open

    def close_doors(self):
        '''Elevator.close_doors()
        Closes the doors by setting doors attribute to False.'''
        self.doorsOpen = False # set doors to closed

    def go_up(self):
        '''Elevator.go_up()
        Goes up by one floor if doors are not open.'''
        if self.doorsOpen:               # if doors are open
            print('Please close doors!') # print warning
        else:                            # if doors are closed
            self.floor += 1              # increase floor by 1

    def go_down(self):
        '''Elevator.go_down()
        Goes down by one floor if doors are not open.'''
        if self.doorsOpen:               # if doors are open
            print('Please close doors!') # print warning
        else:                            # if doors are closed
            self.floor -= 1              # decrease floor by 1

    def go_to_floor(self, destination):
        '''Elevator.go_to_floor(int)
        Closes doors, moves to destination, and opens doors.'''
        if self.doorsOpen:               # if doors are open
            self.close_doors()           # close 'em
        while self.floor != destination: # if not at destination
            if self.floor < destination: # if below
                self.go_up()             # go up 1 floor
            else:                        # if above
                self.go_down()           # go down 1 floor
        self.open_doors()                # open doors

    def get_off (self, person):
        if self.doorsOpen: #if the doors are open
            del self.passengers [self.passengers.index (person)] #remove from passenger list
            return (person + " got off.")
        else:
            return "Doors are closed. Can't get off."

    def get_on (self, person):
        if not self.doorsOpen: #if the doors are closed
            return "Please open the doors first"
        else:
            self.passengers.append (person) #adds the person to passenger list
            return person + " has boarded the elevator."
#test        
e = Elevator(1,True,[])
print (e)
e.get_on ("Bob")
print (e)
e.get_on ("Kat")
print (e)
e.get_off ("Bob")
print (e)

            
