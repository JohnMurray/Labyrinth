#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Weapon.py

from Item_Interface import Item_Interface

class Weapon(Item_Interface):
    
    def __init__(self, damage, chance):
        #code here
        self.damage = damage
        #Not sure how I feel about this, overflow results in low chance
        #and chance can be zero
        self.chance = chance % 21 #chance can be no greater than 20
        return


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
