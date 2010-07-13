#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Player.py

import Armor

#Note - Superclass of Creature and Adventurer
class Player:
    def __init__(self, hp, armor):
        #code here
        self.hp = hp
        self.armor = armor

    def fight(self, player):
        #do something
        return




class Creature(Player):
    def __init__(self, hp):
        Player.__init__(self, hp)




class Adventurer(Player):
    def __init__(self, hp):
        Player.__init__(self, hp)



#def PlayerFactory(player_type, 
