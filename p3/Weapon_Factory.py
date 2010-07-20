#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Weapon_Factory.py

import random
from Distributed_Random import Distributed_Random
from Weapon_Module import *
import Config
from Proc_Factory import Proc_Factory

#Generates Weapons
class Weapon_Factory:
    def __init__(self):
        self
    
    #Returns a subclass of Weapon 
    def generate(self):
        #create an instance of the weapon with it's stats
        return self.generate_by_quality(random.randint(0,2))

    #Generates an item of random type of the quality level requested
    #0 = Low Quality, 1 = Medium Quality, 2 = High Quality
    #Returns a subclass of Weapon
    def generate_by_quality(self, quality):
        gen = { 
                0: self.generate_sword(quality),
                1: self.generate_arrow(quality),
                2: self.generate_spear(quality),
                3: self.generate_hammer(quality),
              }
        wpn = gen[self.select_weapon_type()]
        if quality == 1 and random.randint(1,100) < 20:
            pf = Proc_Factory()
            proc = pf.generate_weapon_proc(random.randint(1,2))
            wpn.name = proc.prefix + " " + wpn.name
            wpn.add_proc(proc)
        
        if quality == 2 and random.randint(1,100) < 40:
            pf = Proc_Factory()
            proc2 = None
            proc = pf.generate_weapon_proc(random.randint(1,3))
            if random.randint(1,100) < 20:
                proc2 = pf.generate_weapon_proc(random.randint(1,3))

            wpn.name = proc.prefix + " " + wpn.name
            wpn.add_proc(proc)
            if proc2 != None:
                wpn.name = wpn.name + " " + proc2.suffix
                wpn.add_proc(proc2)
        
        return wpn

    #Generates a weapon of the requested type and quality
    #Type is 0 for Sword, 1 for Arrow, 2 for Spear, 3 for Hammer
    #Quality is optional 0 = Low Quality, 1 = Medium Quality, 2 = High Quality
    #Default is Medium Quality
    def generate_by_type(self, type, quality=1):
        gen = {
                0: self.generate_sword(quality),
                1: self.generate_arrow(quality),
                2: self.generate_spear(quality),
                3: self.generate_hammer(quality),
              }
        return gen[type]

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
        abs_range = Config.weapon["hammer"]["abs_range"][quality] 
        min_range = Config.weapon["hammer"]["min_range"][quality]
        chance_range = Config.weapon["hammer"]["chance_range"][quality] 
        chance_min = Config.weapon["hammer"]["chance_min"][quality] 
        abs_min = Config.weapon["hammer"]["abs_min"][quality] 
        min_min = Config.weapon["hammer"]["chance_range"][quality] 
        #Vary stats for high/low quality

        min_dam = dist.randint(min_min,min_range)
        abs_dam = dist.randint(abs_min,abs_range)
        max_dam = min_dam + abs_dam
        chance = dist.randint(chance_min,chance_range)
        name = self.generate_hammer_name(quality)
        return Hammer_Weapon(min_dam, max_dam, chance, name, 'desc')

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
        abs_range = Config.weapon["arrow"]["abs_range"][quality] 
        min_range = Config.weapon["arrow"]["min_range"][quality] 
        chance_range = Config.weapon["arrow"]["chance_range"][quality] 
        chance_min = Config.weapon["arrow"]["chance_min"][quality] 
        abs_min = Config.weapon["arrow"]["abs_min"][quality] 
        min_min = Config.weapon["arrow"]["min_min"][quality] 
        
        min_dam = dist.randint(min_min,min_range)
        abs_dam = dist.randint(abs_min, abs_range)
        max_dam = min_dam + abs_dam
        chance = dist.randint(chance_min, chance_range)
        return Arrow_Weapon(min_dam, max_dam, chance, self.generate_arrow_name(quality), 'desc')

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
        abs_range = Config.weapon["spear"]["abs_range"][quality] 
        min_range = Config.weapon["spear"]["min_range"][quality] 
        chance_range = Config.weapon["spear"]["chance_range"][quality] 
        chance_min = Config.weapon["spear"]["chance_min"][quality] 
        abs_min = Config.weapon["spear"]["abs_min"][quality] 
        min_min = Config.weapon["spear"]["min_min"][quality] 
        
        min_dam = dist.randint(min_min, min_range)
        abs_dam = dist.randint(abs_min, abs_range)
        max_dam = min_dam + abs_dam
        chance = dist.randint(chance_min, chance_range)
        return Spear_Weapon(min_dam, max_dam, chance, self.generate_spear_name(quality), 'desc')

    #Generates a name for a sword of variable quality
    def generate_sword_name(self, quality):
        names = [ "Shiv", "Knife", "Dagger", "Cleaver", "Short Sword", "Longsword", "Broadsword", "Rapier", "Epee", "Claymore", "Basterd Sword", "Greatsword" ]
        mat = self.get_material(quality)
        if quality == 0:
            name = names[random.randint(0,3)]
        elif quality == 1:
            name = names[random.randint(4,7)]
        else:
            name = names[random.randint(8,11)]
        return mat + ' ' + name

    def generate_sword(self, quality = 1):
        #generate sword with random stats and magical properties
        dist = Distributed_Random()
        abs_range = Config.weapon["sword"]["abs_range"][quality] 
        min_range = Config.weapon["sword"]["min_range"][quality]
        chance_range = Config.weapon["sword"]["chance_range"][quality] 
        chance_min = Config.weapon["sword"]["chance_min"][quality] 
        abs_min = Config.weapon["sword"]["abs_min"][quality] 
        min_min = Config.weapon["sword"]["min_min"][quality]
            
        min_dam = dist.randint(min_min, min_range)
        abs_dam = dist.randint(abs_min, abs_range)
        max_dam = min_dam + abs_dam
        chance = dist.randint(chance_min, chance_range)
        return Sword_Weapon(min_dam, max_dam, chance, self.generate_sword_name(quality), 'desc')
