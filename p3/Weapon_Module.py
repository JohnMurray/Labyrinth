#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Weapon.py

from Item_Module import Item
import random
from Distributed_Random import Distributed_Random

class Weapon(Item):
    
    def __init__(self, min_damage, max_damage, chance, speed, name, description):
        Item.__init__(self, name, description) 
        self.min_damage = min_damage
        self.max_damage = max_damage
        #Not sure how I feel about this, overflow results in low chance
        #and chance can be zero
        self.chance = chance % 21 #chance can be no greater than 20
        self.speed = speed
        self.score = self.score()
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
    
    #Quick way of quantifying a weapon's statistics 
    #not a very accurate estimate of actual quality
    def score(self):
        score = self.min_damage
        score += self.max_damage
        score += 3 * self.chance
        score += 5 * self.speed
        return score

class Sword_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, speed, name, description):
        Weapon.__init__(self, min_damage, max_damage, chance, speed, name, description)


class Arrow_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, speed, name, description):
        Weapon.__init__(self, min_damage, max_damage, chance, speed, name, description)


class Spear_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, speed, name, description):
        Weapon.__init__(self, min_damage, max_damage, chance, speed, name, description)


class Hammer_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, speed, name, description):
        Weapon.__init__(self, min_damage, max_damage, chance, speed, name, description)

class Weapon_Factory:
    def __init__(self):
        self
    
    #Returns a subclass of Weapon 
    def generate(self):
        #create an instance of the weapon with it's stats
        #gen is a dictionary mapping integers to functions
        gen = {
                0: self.generate_sword(),
                1: self.generate_arrow(),
                2: self.generate_spear(),
                3: self.generate_hammer(),
              }
        #randomly generate a type and call the correct method, return the result
        return gen[self.select_weapon_type()]        

    #Generates a low quality item of random type
    #Returns a subclass of Weapon
    def generate_low_quality(self):
        gen = {
                0: self.generate_sword(0),
                1: self.generate_arrow(0),
                2: self.generate_spear(0),
                3: self.generate_hammer(0),
              }
        return gen[self.select_weapon_type()]
   
    #Generates a high quality item of random type
    #Returns a subclass of Weapon
    def generate_high_quality(self):
        gen = {
                0: self.generate_sword(2),
                1: self.generate_arrow(2),
                2: self.generate_spear(2),
                3: self.generate_hammer(2),
              }
        return gen[self.select_weapon_type()]

    #Returns 0 for Sword, 1 for Arrow, 2 for Spear, 3 for Hammer
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

    #Hard coded material look up, production product would use external data storage
    def get_material(self, quality = 1):
        materials = [ "Stone", "Copper", "Bronze", "Brass", "Silver", "Iron", "Gold", "Steel", "Platinum", "Mithril", "Adamantium" ]
        if quality == 0:
            return materials[random.randint(0,2)]
        elif quality == 1:
            return materials[random.randint(3,6)]
        else:
            return materials[random.randint(7,9)]

    #Generates a hammer's name based on quality
    #0 for low, 1 for medium, 2 for high
    #Returns a string
    def generate_hammer_name(self, quality = 1):
        mat = self.get_material(quality)
        names = [ "Club", "Cudgel", "Mace", "Hammer", "Morning Star", "Flail", "Maul", "War Hammer", "Tetsubo", "Great Maul" ]

        if quality == 0:
            selected = names[random.randint(0,1)]
        elif quality == 1:
            selected = names[random.randint(2,6)]
        else:  
            selected = names[random.randint(7,8)]

        return mat + ' ' + selected
           
    #Generates a hammer of variable quality
    #Returns Hammer
    #Quality parameter follows same format throughout
    def generate_hammer(self, quality = 1):
        dist = Distributed_Random()
        abs_range = 40
        min_range = 29
        chance_range = 5
        chance_min = 0
        abs_min = 5
        min_min = 12
        #Vary stats for high/low quality
        #Hard coding for simplicity
        if quality == 0:
            abs_range = 30
            min_range = 21
            chance_range = 3
        elif quality == 2:
            abs_min = 10
            min_min = 20
            chance_min = 1

        min_dam = dist.randint(12,40)
        abs_dam = dist.randint(5,29)
        max_dam = min_dam + abs_dam
        speed = max_dam // 15
        chance = dist.randint(0,6)
        name = self.generate_hammer_name(quality)
        return Hammer_Weapon(min_dam, max_dam, chance, speed, name, 'desc')

    #Same as the others, Generates Arrow names
    def generate_arrow_name(self, quality=1):
        mat = self.get_material(quality)
        names = [ "Dart", "Throwing Knife", "Short Bow", "Long Bow", "Compound Bow", "Recurve Bow", "Light Crossbow", "Heavy Crossbow", "Matchlock Pistol", "Matchlock Rifle" ]
        if quality == 0:
            name = names[random.randint(0,2)]
        elif quality == 1:
            name = names[random.randint(3,6)]
        else:
            name = names[random.randint(7,9)]
        
        return mat + ' embossed ' + name

    #Generates an Arrow object of variable quality
    def generate_arrow(self, quality = 1):
        dist = Distributed_Random()
        abs_range = 35
        min_range = 36
        chance_range = 5
        chance_min = 0
        abs_min = 5
        min_min = 10
        
        if quality == 0:
            abs_range = 25
            min_range = 24
            chance_range = 3
        elif quality == 2:
            abs_min = 10
            min_min = 20
            chance_min = 1

        min_dam = dist.randint(10,36)
        abs_dam = dist.randint(5,35)
        max_dam = min_dam + abs_dam
        speed = max_dam // 13
        chance = dist.randint(0,6)
        return Arrow_Weapon(min_dam, max_dam, chance, speed, self.generate_arrow_name(quality), 'desc')

    #Generates a name for a spear of variable quality
    def generate_spear_name(self, quality):
        names = [ "Crude Spear", "Short Spear", "Long Spear", "Halberd", "Pike", "Yari", "Naginata", "Lance" ]
        mat = self.get_material(quality)
        if quality == 0:
            name = names[random.randint(0,1)]
        elif quality == 1:
            name = names[random.randint(2,4)]
        else:
            name = names[random.randint(5,6)]
        return mat + '-tipped ' + name

    #Generates a Spear object of variable quality
    def generate_spear(self, quality = 1):
        dist = Distributed_Random()
        abs_range = 36
        min_range = 24
        chance_range = 7 
        chance_min = 0
        abs_min = 3
        min_min = 5 
        
        if quality == 0:
            abs_range = 24
            min_range = 12
            chance_range = 5
        elif quality== 2:
            abs_min = 9
            min_min = 11
            chance_min = 2

        min_dam = dist.randint(min_min, min_range+1)
        abs_dam = dist.randint(abs_min, abs_range+1)
        max_dam = min_dam + abs_dam
        speed = max_dam // 9
        chance = dist.randint(chance_min, chance_range+1)
        return Spear_Weapon(min_dam, max_dam, chance, speed, self.generate_spear_name(quality), 'desc')

    #Generates a name for a sword of variable quality
    def generate_sword_name(self, quality):
        names = [ "Shiv", "Knife", "Dagger", "Cleaver", "Short Sword", "Longsword", "Broadsword", "Rapier", "Epee", "Claymore", "Basterd Sword", "Greatsword" ]
        mat = self.get_material(quality)
        if quality == 0:
            name = names[random.randint(0,4)]
        elif quality == 1:
            name = names[random.randint(5,8)]
        else:
            name = names[random.randint(9,12)]
        return mat + ' ' + name

    def generate_sword(self, quality = 1):
        #generate sword with random stats and magical properties
        dist = Distributed_Random()
        abs_range = 32
        min_range = 20
        chance_range = 7
        chance_min = 0
        abs_min = 1
        min_min = 1
        if quality == 0:
            abs_range = 20
            min_range = 10
            chance_range = 5
        elif quality == 2:
            abs_min = 7
            min_min = 7
            chance_min = 2
            
        min_dam = dist.randint(min_min, min_range + 1)
        abs_dam = dist.randint(abs_min, abs_range + 1)
        max_dam = min_dam + abs_dam
        speed = max_dam // 7
        chance = dist.randint(chance_min, chance_range + 1)
        return Sword_Weapon(min_dam, max_dam, chance, speed, self.generate_sword_name(quality), 'desc')
