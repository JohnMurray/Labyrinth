#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Player.py

import Armor

#Note - Superclass of Creature and Adventurer
class Player:
    def __init__(self, name, hp, armor, weapon):
        #code here
        self.name = name
        self.hp = hp
        self.armor = armor
        self.max_hp = hp
        self.weapon = list()

        self.weapon.append(weapon)

    def fight(self, player):
        #do something
        return

    def to_string(self):
        return ''




class Creature(Player):
    def __init__(self, name, hp, armor, weapon, element):
        Player.__init__(self, name, hp, armor, weapon)
        self.element = element




class Adventurer(Player):
    def __init__(self, name, hp):
        Player.__init__(self, name, hp)


class Creature_Factory:
    def generate(self):
        return Creature()
