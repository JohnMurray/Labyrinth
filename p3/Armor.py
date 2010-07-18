#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Armor.py

from Item_Interface import Item_Interface
from Distributed_Random import Distributed_Random
import random

class Armor(Item_Interface):

    def __init__(self, defense, damage_reduction):
        #code here
        self.defense = defense
        self.damage_reduction = damage_reduction

class Armor_Factory:
    def __init__(self):
        self

    def generate(self):
        #generate a random piece of armor
        #create a dictionary of outcomes
        gen = {
                0: self.generate_light_armor(),
                1: self.generate_medium_armor(),
                2: self.generate_heavy_armor(),
              }
        #how awesome are function objects? very. 
        return gen[self.select_armor_type()]

    def generate_high_quality(self):
        #generate a random high quality piece of armor
        dist = Distributed_Random()
        defense = dist.randint(12,17)
        dr = dist.randint(5,9)
        return Armor(defense, dr)

    def generate_medium_quality(self):
        #generate random medium quality 
        return self.generate_medium_armor()

    def generate_low_quality(self):
        #generate low quality piece of armor
        dist = Distributed_Random()
        defense = dist.randint(10,17)
        dr = dist.randint(0,1)
        return Armor(defense, dr)

    def select_armor_type(self):
        rand = random.randint(1,100)
        #50/30/20 Light/Medium/Heavy ratio, configurable
        if rand <= 50:
            return 0
        elif rand <= 80:
            return 1
        else:
            return 2
    
    def generate_light_armor(self):
        dist = Distributed_Random()
        defense = dist.randint(10,21)
        dr = dist.randint(0,3)
        return Armor(defense, dr)

    def generate_medium_armor(self):
        dist = Distributed_Random()
        defense = dist.randint(8,19)
        dr = dist.randint(2,5)
        return Armor(defense, dr)

    def generate_heavy_armor(self):
        dist = Distributed_Random()
        defense = dist.randint(6,17)
        dr = dist.randint(4,9)
        return Armor(defense, dr)
        
