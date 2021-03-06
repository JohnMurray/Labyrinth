#Authors Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#Due: July 19th, 2010
#File: Proc.py

import random
from Effect import *
from Player import Adventurer
import math

#Procs are effects that can be attached to weapons/armor
#Procs cause various effects examples elemental damage, chance to stun
#Procs are classified as Armor_Proc and Weapon_Proc
class Proc:
    def __init__(self):
        self.prefix = ""
        self.suffix = ""

#Armor_Proc's happen on defense_post and have various effects
#Typically require a hit and a chance of firing
#Not for human consumption, use concrete implementations
class Armor_Proc(Proc):
    def __init__(self):
        Proc.__init__(self)
    
    #abstract implementation of defense_post 
    def defense_post(self, attacker, defender, result, damage):
       pass

#Weapon_Proc's happen on attack_post and have various effects
#Typically require a hit and have a chance of firing 
#Not for human consumption use concrete implementations
class Weapon_Proc(Proc):
    def __init__(self):
        Proc.__init__(self)

    #abstract implementation of attack_post
    def attack_post(self, attacker, defender, result, damage):
        pass

#Thorn_Proc does damage to an attack on a hit
class Thorn_Proc(Armor_Proc):
    def __init__(self, chance, damage):
        Armor_Proc.__init__(self)
        self.chance = chance
        self.damage = damage
        self.prefix = "Thorny"
        self.suffix = "of Thorns"

    #Remove thorn damage hp from attacker
    def defense_post(self, attacker, defender, result):
        #If hit and less roll < chance
        if result >= 0 and random.randint(1,100) <= self.chance:
            attacker.hp -= self.damage

#Leech_Proc drains life from the attacker on a hit
#Draining the defenders hp and giving it to the attacker
#chance is likelihood the proc will fire
#percent is percent of damage inflicted in the attack that will be given to the attacker
#percent should be very low for balance (20-30 would be very good)
class Leech_Proc(Weapon_Proc):
    def __init__(self, chance, percent):
        Weapon_Proc.__init__(self)
        self.chance = chance
        self.percent = percent
        self.prefix = "Vampiric"
        self.suffix = "of draining"

    def attack_post(self, attacker, defender, result, damage):
        if result >= 0 and random.randint(1,100) < self.chance:
            attacker.heal(int(math.floor(self.percent * damage / 100)))

#Poison_Proc poisons the defender 
class Poison_Proc(Weapon_Proc):
    def __init__(self, chance, duration, damage):
        Weapon_Proc.__init__(self)
        self.chance = chance
        self.duration = duration
        self.damage = damage
        self.prefix = "Putrid"
        self.suffix = "of decay"

    def attack_post(self, attacker, defender, result, damage):
        if result >= 0 and random.randint(1,100) <= self.chance:
            defender.add_effect(DOT_Effect(self.duration,self.damage))    
            if isinstance(attacker, Adventurer):
                print "Your %s oozes venom on" % attacker.current_attack().name,
                print defender.name + "."
            else:
                print "%s's" % attacker.name,
                print "%s oozes venom on you! *** PoIsOnEd ***" % attacker.current_attack().name
                

#Stun_Proc stuns the defender for duration rounds
class Stun_Proc(Weapon_Proc):
    def __init__(self, chance, duration):
        Weapon_Proc.__init__(self)
        self.chance = chance
        self.duration = duration
        self.prefix = "Dazzling"
        self.suffix = "of victory"

    def attack_post(self, attacker, defender, result, damage):
        if defender.is_stunned():
            return
        if result >= 0 and random.randint(1,100) <= self.chance:
            defender.add_effect(Stun_Effect(self.duration))
            if isinstance(attacker, Adventurer):
                print "Your %s flashes with mystical power," % attacker.current_attack().name,
                print "stunning your opponent for %s rounds!" % self.duration
            else:
                print "You're blinded by a flash from the %s," % attacker.current_attack().name,
                print "you are stunned for %s rounds!" % self.duration
