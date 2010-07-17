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

class RoomFactory:

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
        description = RoomFactory.get_room_description()
        gold = random.randrange(101)
        creature = CreatureFactory.generate()
        item_choice = random.randrange(2) + 1
        items = list()
        if( item_choice == 1 ):
            items.append( PotionFactory.generate() )
        if( item_choice == 2 ):
            items.append( SpellFactory.generate() )
        items.append( WeaponFactory.generate() )
        items.append( AromorFactory.append() )
        return Room( description, creature, items, gold)
            
    
    generate = Static(generate)
    get_room_description = Static(get_room_description)
