#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Treasure.py

from Weapon_Factory import *
from Armor_Factory import *
from Item_Factory import *
from Distributed_Random import *

class Treasure:
    def __init__(self):
        self

    def generate(self, level):
        dist = Distributed_Random
        wf = Weapon_Factory()
        af = Armor_Factory()
        items = Item_Factory()
        treasure = list()
        if random.randint(1,100) - (level*2) < 25:
            #generate a random number of items
            num = dist.randint(1,level//2)
            while num > 0:
                treasure.append(self.gen(level))
        return treasure

       
    def gen(self, level):
        wf = Weapon_Factory()
        af = Armor_Factory()
        items = Item_Factory()
        type = random.randint(1,3)
        if type == 1:
            if level <= 3:
                return wf.generate_by_quality(random.randint(0,1))
            elif level <= 7:
                return wf.generate_by_quality(random.randint(1,2))
            else:
                return wf.generate_by_quality(2)
        elif type == 2:
            if level <= 3:
                return af.generate_by_quality(random.randint(0,1))
            elif level <= 7:
                return af.generate_by_quality(random.randint(1,2))
            else:
                return af.generate_by_quality(2)
        else:
            if level <= 3:
                return items.generate_by_quality(random.randint(1,2))
            elif level <= 7:
                return items.generate(random.randint(2,3))
            else:
                return items.generate(3)
