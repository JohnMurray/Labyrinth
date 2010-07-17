#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Player.py

from Armor import Armor
from Weapon_Module import Weapon

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
        self.spells = list()
        self.effects = list()
        self.OS = 0
        self.DS = 0
        self.primary = None

    def fight(self, player):
        #do something
        return

    def to_string(self):
        return ''

    def add_spell(self, spell):
        #adds a new spell to the spell inventory
        self.spells.append(spell)

    def add_weapon(self, weapon):
        #adds a new weapon to the weapon inventory
        self.weapon.append(weapon)

    def primary_weapon(self):
        if self.weapon == None or len(self.weapon) == 0:
            return Weapon(1,1,1) 
        else:
            return self.weapon[0]
           
    def primary_armor(self):
        if self.armor == None or len(self.armor) == 0:
            return Armor(0,0) 
        else:
            return self.weapon[0]

    def add_armor(self, armor):
        #adds a new armor to the armor inventory
        self.armor.append(armor)

    def add_effect(self, effect):
        #adds a new effect to the player
        self.effects.append(effect)

    def remove_effect(self, effect):
        #removes an effect from the player
        self.effects.remove(effect)

    def current_attack(self):
        #returns the currently readied attack (can be any Item_Interface)
        if self.primary == None:
               self.primary = self.primary_weapon() 

        return self.primary

class Creature(Player):
    def __init__(self, name, hp, armor=list(), weapon=list(), element=None):
        Player.__init__(self, name, hp, armor, weapon)
        self.element = element


class Adventurer(Player):
    def __init__(self, name, hp):
        Player.__init__(self, name, hp,None,None)


class Creature_Factory:
    def generate(self):
        return Creature()
