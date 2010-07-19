#Authors: Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#File: Creature_Factory.py

from Armor_Factory import Armor_Factory
from Weapon_Factory import Weapon_Factory
from Player import Creature
import random

class Creature_Factory:
    def __init__(self):
        self

    def generate(self):
        return self.generate_difficulty(random.randint(0,10))

    def generate_difficulty(self, diff):
        #generate random name based on difficulty
        #generate hp based on difficulty
        hp = random.randint(30,50) * diff
        genesis = Creature('Gen',hp)
        genesis.weapon = list()
        genesis.armor = list()
        wf = Weapon_Factory()
        af = Armor_Factory()
        if diff <= 3:
            genesis.add_armor(af.generate_low_quality())
            genesis.add_weapon(wf.generate_by_quality(0))
        elif diff <= 8:
            genesis.add_armor(af.generate_medium_quality())
            genesis.add_weapon(wf.generate_by_quality(1))
        else:
            genesis.add_armor(af.generate_high_quality())
            genesis.add_weapon(wf.generate_by_quality(2))
        
        return genesis

