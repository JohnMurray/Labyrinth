#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Armor_Factory.py

from Distributed_Random import Distributed_Random
import random
from Armor import Armor

#Armor_Factory generates random and selected pieces of armor
class Armor_Factory:
    def __init__(self):
        self

    def generate_by_quality(self, quality):
        gen = {
                0: self.generate_low_quality(),
                1: self.generate_medium_quality(),
                2: self.generate_high_quality(),
              }
        return gen[self.select_armor_type()]

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
 
	#Randomly select armor type
    def select_armor_type(self):
        rand = random.randint(1,100)
        #50/30/20 Light/Medium/Heavy ratio, configurable
        if rand <= 50:
            return 0
        elif rand <= 80:
            return 1
        else:
            return 2
   
    #Look up method for light materials
    def generate_light_material(self):
        names = [ "Cloth", "Bone", "Hide", "Leather" ]
        return names[random.randint(0,3)]

   #Look up method for medium materials 
    def generate_medium_material(self):
        names = [ "Chain", "Scale", "Banded" ]
        return names[random.randint(0,2)]

    #Look up method for heavy materials
    def generate_heavy_material(self):
        names = [ "Steel", "Mithril", "Adamantium" ]
        return names[random.randint(0,2)]
 
 #Just call it plate mail and be done with it
    def generate_heavy_name(self):
        return self.generate_heavy_material() + ' Plate Mail'

    #All medium armors just became mail
    def generate_medium_name(self):
        return self.generate_medium_material() + ' Mail'

    #Cloth armor? whatever.
    def generate_light_name(self):
        return self.generate_light_material() + ' Armor'

	#Generate a high quality piece of armor
    #Will be a "Heavy" type armor
    def generate_high_quality(self):
        #generate a random high quality piece of armor
        dist = Distributed_Random()
        defense = dist.randint(12,17)
        dr = dist.randint(5,9)
        return Armor(defense, dr, self.generate_heavy_name(), 'desc')

    def generate_medium_quality(self):
        #generate random medium quality 
        return self.generate_medium_armor()

    def generate_low_quality(self):
        #generate low quality piece of armor
        dist = Distributed_Random()
        defense = dist.randint(10,17)
        dr = dist.randint(0,1)
        return Armor(defense, dr, self.generate_light_name(), 'desc')

    #Generate a random light armor
    def generate_light_armor(self):
        dist = Distributed_Random()
        defense = dist.randint(10,21)
        dr = dist.randint(0,3)

        return Armor(defense, dr, self.generate_light_name(), 'desc')

    #Generate a random medium armor
    def generate_medium_armor(self):
        dist = Distributed_Random()
        defense = dist.randint(10,19)
        dr = dist.randint(2,5)
        return Armor(defense, dr, self.generate_medium_name(), 'desc')

    #Generate a random heavy armor
    def generate_heavy_armor(self):
        dist = Distributed_Random()
        defense = dist.randint(10,17)
        dr = dist.randint(4,9)
        return Armor(defense, dr, self.generate_heavy_name(), 'desc')
        
