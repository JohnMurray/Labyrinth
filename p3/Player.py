#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Player.py

import Armor

#Note - Superclass of Creature and Adventurer
class Player:
    def __init__(self, hit_points):
        #code here
        self.hp = hit_points




class Creature(Player):
    def __init__(self, hp):
        Player.__init__(self, hp)




class Adventurer(Player):
    def __init__(self, hp):
        Player.__init__(self, hp)
