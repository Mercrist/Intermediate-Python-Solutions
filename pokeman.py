class Pokemon:
    '''contains all the methods and stuff to play a simple pokeman game'''
    def __init__ (self,name='',health=0,atk=0,defense=0):
        self.name = name
        self.health = health
        self.atk = atk
        self.defense = defense

    def __str__ (self):
        '''returns the pokemans stats'''
        string = self.name + " (HP: " + str(self.health) +")" + "\n" + \
                 "ATK: " + str(self.atk) + " DEF: " + str(self.defense)
        return string

    def calculate_dmg (self,other):
        '''calculates damage inflicted into other pokeman'''
        import random
        r = random.uniform (0.85, 1.1)
        dmg = (((12/5)*(self.atk/other.defense))+2)*r
        return dmg

    def attack (self,other):
        '''deals attack damage and maybe kills pokeman'''
        import math
        damage = round (self.calculate_dmg (other))
        print (self.name + " deals " + str(damage) + " damage!")
        other.health -= damage
        if other.health <= 0:
            print (other.name + " has fainted!")
            return

b = Pokemon('Bulbasaur', 45, 49, 49)
c = Pokemon('Charmander', 39, 52, 43)

