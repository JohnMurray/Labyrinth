#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Weapon.py

from Item_Module import Item
import random
from Distributed_Random import Distributed_Random

class Weapon(Item):
    
    def __init__(self, min_damage, max_damage, chance, speed):
        #code here
        self.min_damage = min_damage
        self.max_damage = max_damage
        #Not sure how I feel about this, overflow results in low chance
        #and chance can be zero
        self.chance = chance % 21 #chance can be no greater than 20
        self.speed = speed
        return

    def output_result_first(self, result, damage=0):
        if result >= 0:
            print "You attack for %s damage" % damage
        else:
            print "You attack, but miss"

    def output_result_third(self,  result, damage=0):
        if result >= 0:
            print "attacks you for %s damage" % damage
        else:
            print "attacks you, but misses"

class Magical_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, speed):
        Weapon.__init__(self, min_damage, max_damage, chance, speed)


class Sword_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, speed):
        Weapon.__init__(self, min_damage, max_damage, chance, speed)


class Arrow_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, speed):
        Weapon.__init__(self, min_damage, max_damage, chance, speed)


class Spear_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, speed):
        Weapon.__init__(self, min_damage, max_damage, chance, speed)


class Hammer_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, speed):
        Weapon.__init__(self, min_damage, max_damage, chance, speed)

class WeaponFactory:
    def __init__(self):
        self
    
    def generate(self):
    #create an instance of the weapon with it's stats
        self.select_weapon_type()
        gen = {
                0: self.generate_sword(),
                1: self.generate_arrow(),
                2: self.generate_spear(),
                3: self.generate_hammer(),
              }
        w = gen[self.select_weapon_type()]        
        return w

    def select_weapon_type(self):
        #Would like to make this configurable
        #currently 40% sword, 20% arrow, 20% spear, 20% hammer
        rand = random.randint(1,100)
        if rand <= 40:
            return 0
        elif rand <= 60:
            return 1
        elif rand <= 80:
            return 2
        else:
            return 3

    def generate_hammer(self):
        dist = Distributed_Random()
        min_dam = dist.randint(12,40)
        abs_dam = dist.randint(5,29)
        max_dam = min_dam + abs_dam
        speed = max_dam // 15
        chance = dist.randint(0,6)
        return Hammer_Weapon(min_dam, max_dam, chance, speed)

    def generate_arrow(self):
        dist = Distributed_Random()
        min_dam = dist.randint(10,36)
        abs_dam = dist.randint(5,35)
        max_dam = min_dam + abs_dam
        speed = max_dam // 13
        chance = dist.randint(0,6)
        return Arrow_Weapon(min_dam, max_dam, chance, speed)

    def generate_spear(self):
        dist = Distributed_Random()
        min_dam = dist.randint(5,25)
        abs_dam = dist.randint(3,37)
        max_dam = min_dam + abs_dam
        speed = max_dam // 9
        chance = dist.randint(0,8)
        return Spear_Weapon(min_dam, max_dam, chance, speed)

    def generate_sword(self):
        #generate sword with random stats and magical properties
        dist = Distributed_Random()
        min_dam = dist.randint(1,21)
        abs_dam = dist.randint(1,33)
        max_dam = min_dam + abs_dam
        speed = max_dam // 7
        chance = dist.randint(0,8)
        return Sword_Weapon(min_dam, max_dam, chance, speed)
