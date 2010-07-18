#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Player.py

import Static

from Static import Static
from Weapon_Module import Weapon_Factory
from Weapon_Module import Weapon
from Armor import Armor_Factory
from Armor import Armor
from Item_Module import *
from Effect import *
import random

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
        self.potion = list()
        self.effect = list()
        self.OS = 0
        self.DS = 0

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

    def add_potion(self, potion):
        #adds a new potion to the potion inventory
        self.potion.append(potion)

    def primary_weapon(self):
        if self.weapon == None or len(self.weapon) == 0:
            return Weapon(1, 1, 0, 1, 'None', 'Nothing') 
        else:
            return self.weapon[0]
           
    def primary_armor(self):
        if self.armor == None or len(self.armor) == 0:
            return Armor(10, 0, 'None', 'Nothing') 
        else:
            return self.armor[0]

    def add_armor(self, armor):
        #adds a new armor to the armor inventory
        self.armor.append(armor)

    def add_effect(self, effect):
        #adds a new effect to the player
        self.effect.append(effect)

    def remove_effect(self, effect):
        #removes an effect from the player
        self.effect.remove(effect)

    def is_stunned(self):
        #returns True if Player is stunned, False if not
        #check all effects for stun type, else return False
        for e in self.effect:
            if isinstance(e, Stun_Effect):
                return True
        return False

    def offense_bonus(self):
        #returns the amount of offensive bonus to physical attacks
        #from effects
        bonus = 0
        for e in self.effect:
            if isinstance(e, Offense_Effect):
                bonus += e.bonus
        return bonus

    def offense_bonus_magic(self):
        #returns the amount of offensive bonus to magic attacks
        #from effects
        bonus = 0
        for e in self.effect:
            if isinstance(e, Magic_Offense_Effect):
                bonus += e.bonus
        return bonus

    def defense_bonus(self):
        #returns the amount of defensive bonus to physical attacks
        #from effects
        bonus = 0
        for e in self.effect:
            if isinstance(e, Defense_Effect):
                bonus += e.bonus
        return bonus

    def defense_bonus_magic(self):
        #returns the amount of defensive bonus to magic attacks
        #from effects
        bonus = 0
        for e in self.effect:
            if isinstance(e, Magic_Defense_Effect):
                bonus += e.bonus
        return bonus
                

class Creature(Player):
    def __init__(self, name, hp, armor=list(), weapon=list(), element=None):
        Player.__init__(self, name, hp, armor, weapon)
        self.element = element

    def current_attack(self):
        #returns the attack selected by the creature
        #todo: add some kind of biased selection system that we can generate "attack scripts" from
        return self.primary_weapon()

class Adventurer(Player):
    def __init__(self, name, hp):
        Player.__init__(self, name, hp,None,None)
        self.primary = None

    def current_attack(self):
        #returns the primary action selected by the player
        if self.primary == None:
            self.primary = self.primary_weapon()
        return self.primary

class Creature_Factory:
    def __init__(self):
        self

    def generate_difficulty(self, diff):
        #generate random name based on difficulty
        #generate hp based on difficulty
        hp = random.randint(30,50) * diff
        genesis = Creature('Gen',hp)
        wf = Weapon_Factory()
        af = Armor_Factory()
        if diff <= 3:
            genesis.add_armor(af.generate_low_quality())
            genesis.add_weapon(wf.generate_low_quality())
        elif diff <= 8:
            genesis.add_armor(af.generate_medium_quality())
            genesis.add_weapon(wf.generate())
        else:
            genesis.add_armor(af.generate_high_quality())
            genesis.add_weapon(wf.generate_high_quality())
        
        return genesis

    def generate(self):
        return Creature()
