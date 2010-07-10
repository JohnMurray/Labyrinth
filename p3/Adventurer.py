#Authors: Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#Due: July 19th, 2010
#File: Adventurer.py

#import declarations
import Armor
import Weapon
import Player

from Player import Player

class Adventurer(Player):
    
    def __init__(self, hp):
        #create the character here
        #self is required to assign data, but is not actually given as a para-
        #meter when calling the constructor.
        #local members can be assignd by using self.var = value

        #initialize parent
        Player.__init__(self, hp)
