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
        genesis = self.generate_stats(diff, genesis)
        wf = Weapon_Factory()
        af = Armor_Factory()
        if diff <= 3:
            genesis.add_armor(af.generate_by_quality(0))
            genesis.add_weapon(wf.generate_by_quality(0))
        elif diff <= 8:
            genesis.add_armor(af.generate_by_quality(1))
            genesis.add_weapon(wf.generate_by_quality(1))
        else:
            genesis.add_armor(af.generate_by_quality(2))
            genesis.add_weapon(wf.generate_by_quality(2))
        
        return genesis

    def stat_max(self, max, gen):
        gen.strength = random.randint(1, max)
        gen.agility = random.randint(1, max)
        gen.dexterity = random.randint(1, max)
        gen.intel = random.randint(1, max)
        gen.stamina = random.randint(1, max)
        return gen

    def generate_stats(self, diff, gen):
        if diff <= 3:
            gen = self.stat_max(3,gen)
        elif diff <= 5:
            gen = self.stat_max(diff, gen)
        elif diff <= 10:
            gen = self.stat_max(7, gen)
        else:
            gen = self.stat_max(diff, gen)
        
        return gen

    def generate_player_stats(self, player):
        return self.generate_stats(10, player)

