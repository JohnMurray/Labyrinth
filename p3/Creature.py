#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Creature.py

import Player
from Player import Player

class Creature(Player):
    
    def __init__(self, hp):
       Player.__init__(self, hp)
       self.hp = hp
