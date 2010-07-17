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
        
        if armor == None:
            self.armor = list()
        else:
            self.armor = armor

        if weapon == None:
            self.weapon = list()
        else:
            self.weapon = weapon

        self.max_hp = hp
        self.spell = list()


    def fight(self, player):
        #do something
        return

    def to_string(self):
        return ''

    def add_spell(self, spell):
        #adds a new spell to the spell inventory
        self.spell.append(spell)

    def add_weapon(self, weapon):
        #adds a new weapon to the weapon inventory
        self.weapon.append(weapon)

    def primary_weapon(self):
        if self.weapon == None or len(self.weapon) == 0:
            return None
        else:
            return self.weapon[0]
           
    def primary_armor(self):
        if self.armor == None or len(self.armor) == 0:
            return None
        else:
            return self.weapon[0]

    def add_armor(self, armor):
        #adds a new armor to the armor inventory
        self.armor.append(armor)

class Creature(Player):
    def __init__(self, name, hp, armor, weapon, element):
        Player.__init__(self, name, hp, armor, weapon)
        self.element = element




class Adventurer(Player):
    def __init__(self, name, hp):
        Player.__init__(self, name, hp,None,None)


class Creature_Factory:
    def generate(self):
        return Creature()
