#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Room.py

import random

class Room:

    def __init__(self, description, creature=None, item=list(), armor=list(), weapon=list(), gold=0):
        #code here
        self.description = description
        self.creature = creature
        self.item = item
        self.weapon = weapon
        self.gold = gold

    def add_weapon(self, weapon):
        self.weapon.append(weapon)

class Room_Factory:

    #static definition to generate random descriptions
    def get_room_description():
        descrip = list(self)
        descrip.append('room 1')
        descrip.append('room 2')
        descrip.append('room 3')
        descrip.append('room 4')
        descrip.append('room 5')
        descrip.append('room 6')
        descrip.append('room 7')
        descrip.append('room 8')
        descrip.append('room 9')
        descrip.append('room 10')
        descrip.append('room 11')
        descrip.append('room 12')
        
        return descrip[random.randrange(0, len(descrip))]

    def generate(self):
        description = self.get_room_description()

