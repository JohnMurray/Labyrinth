#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Weapon.py

class Weapon(Item_Interface):
    
    def __init__(self, damage, chance):
        #code here
        self.damage = damage
        self.chance = chance % 21 #chance can be no grater than 20
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
    
    #create and instance of the weapon with it's stats
    return
