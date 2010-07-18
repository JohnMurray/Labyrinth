#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Room.py

import random
import Player
import Static

from Static import Static
from Player import *

class Room:

    def __init__(self, description, creature=None, item=list(), gold=0):
        #code here
        self.description = description
        self.creature = creature
        self.item = item
        self.gold = gold

class Room_Factory:

    #static definition to generate random descriptions
    def get_room_description():
        descrip = [
            'room 1',
            'room 2',
            'room 3',
            'room 4',
            'room 5',
            'room 6',
            'room 7',
            'room 8',
            'room 9',
            'room 10',
            'room 11',
            'room 12',
        ]
        
        return descrip[random.randrange(0, len(descrip))]

    def generate():
        #description item and gold
        description = Room_Factory.get_room_description()
        gold = random.randrange(101)
        cf = Creature_Factory()
        creature = cf.generate()
        #generate items
        items = list()
        itf = Item_Factory()
        items.append( itf.generate() )
        wf = Weapon_Factory()
        items.append( wf.generate() )
        af = Armor_Factory()
        items.append( af.generate() )
        return Room( description, creature, items, gold )
            
    
    generate = Static(generate)
    get_room_description = Static(get_room_description)
