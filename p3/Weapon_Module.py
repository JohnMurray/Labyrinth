#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Weapon.py

from Item_Module import Item

class Weapon(Item):
    
    def __init__(self, damage, chance):
        #code here
        self.damage = damage
        #Not sure how I feel about this, overflow results in low chance
        #and chance can be zero
        self.chance = chance % 21 #chance can be no greater than 20
        return

    def output_result_first(self, result):
        if result >= 0:
            print "You attack for 1 damage"
        else:
            print "You attack, but miss"

    def output_result_third(self,  result):
        if result >= 0:
            print "attacks you for 1 damage"
        else:
            print "attacks you, but misses"

class Magical_Weapon(Weapon):
    def __init__(self, damage, chance):
        Weapon.__init__(self, damage, chance)


class Sword_Weapon(Weapon):
    def __init__(self, damage, chance):
        Weapon.__init__(self, damage, chance)


class Arrow_Weapon(Weapon):
    def __init__(self, damage, chance):
        Weapon.__init__(self, damage, chance)


class Spear_Weapon(Weapon):
    def __init__(self, damage, chance):
        Weapon.__init__(self, damage, chance)


class Hammar_Weapon(Weapon):
    def __init__(self, damage, chance):
        Weapon.__init__(self, damage, chance)




def WeaponFactory(category, stats):
    
    #create an instance of the weapon with it's stats
    return
