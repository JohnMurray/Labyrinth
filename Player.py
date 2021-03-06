#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Player.py

import Static
from Weapon_Module import Wand_Weapon
from Item_Module import Spell
from Item_Module import Potion 
from Armor import Armor
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
        self.primary = None
        self.strength = 0
        self.agility = 0
        self.dexterity = 0
        self.intel = 0
        self.stamina = 0
        self.level = 1
        self.gold = 0
    
    def to_string(self):
        return ''

    def __str__(self):
        return self.name + "   (HP: " + str(self.hp) + ")"

    def add_spell(self, spell):
        #adds a new spell to the spell inventory
        self.spells.append(spell)

    def add_weapon(self, weapon):
        #adds a new weapon to the weapon inventory
        self.weapon.append(weapon)

    def heal(self, amt):
        if self.hp + amt > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amt

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
                
    def calc_DS_Physical(self):
        #simulate encumbrance
        d = self.agility - self.encum() 
        #Primary armor's defense value
        x = self.primary_armor().defense
        #Add bonus from effects
        x += self.defense_bonus()
        if d > 0:
            x += d
        if self.is_stunned():
            x -= 3
        if x < 0:
            x = 0
        return x


    def calc_DS_Magic(self):
        x = self.intel + self.defense_bonus_magic()
        if self.is_stunned():
            x -= 3
        if x < 0:
            x = 0
        return x

    def calc_OS_Physical(self):
        x = self.primary_weapon().chance
        x += self.offense_bonus()
        if isinstance(self.primary_weapon(), Wand_Weapon):
            off = self.intel - self.encum()
        else:
            off = self.dexterity - self.encum() 
        if off > 0:
            x += off
        
        return x

    def calc_OS_Magic(self):
        return self.intel + self.offense_bonus_magic()

    def encum(self):
        return self.primary_armor().required_strength

    def calc_num_attacks(self):
        a = self.current_attack()
        if isinstance(a, Spell) or isinstance(a, Potion):
            return 1
        num = self.dexterity
        num += self.agility
        num -= self.encum()
        num += self.primary_weapon().speed
        num = num // 7 
        if num < 1:
            num = 1
        return num

    def current_attack(self):
        if self.primary == None:
            self.primary = self.primary_weapon()
        return self.primary

    def all_equipment(self):
        temp = list()
        for w in self.weapon:
            temp.append(w)
        for a in self.armor:
            temp.append(a)
        for p in self.potion:
            temp.append(p)
        for s in self.spells:
            temp.append(s)
        return temp

class Creature(Player):
    def __init__(self, name, hp, armor=list(), weapon=list(), element=None):
        Player.__init__(self, name, hp, armor, weapon)
        self.element = element

    def select_attack(self):
        #returns the attack selected by the creature
        #todo: add some kind of biased selection system that we can generate "attack scripts" from
        self.primary = self.primary_weapon()
        return self.primary

    def calc_experience(self):
        xp = self.strength * 2
        xp += self.stamina * 2
        xp += self.dexterity * 2
        xp += self.agility * 2
        xp += self.intel * 2
        xp += self.max_hp // 5 
        xp += self.primary_weapon().score // 5
        xp += self.primary_armor().damage_reduction * 2
        return xp * 3


class Adventurer(Player):
    def __init__(self, name, hp):
        Player.__init__(self, name, hp,None,None)
        self.experience = 0
        self.next_level = 1000
        self.ap = 0
    
    def calc_next_level(self):
        return 1000 + (1500 * (self.level-1))
    
    def grant_xp(self, xp):
        self.experience += xp 
        while self.experience > self.next_level:
            self.gain_level()
     
    def gain_level(self):
        self.level += 1
        self.next_level = self.calc_next_level()
        hp_gain = random.randint(self.stamina*4, self.stamina*10)
        self.max_hp += hp_gain
        self.hp = self.max_hp
        self.ap = self.level * 2 + self.intel
        print "Congratulations! You are now Level %s!" % self.level
        print "You gained %s max hp and" % hp_gain, "%s attribute points."

