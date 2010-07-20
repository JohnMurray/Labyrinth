#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Armor.py

from Item_Module import Item

#All armor is represented by the Armor class
#Armors are broken into 3 rough categories (Light, Medium, Heavy)
#Light armor would be clothing or hide armors
#They generally provide high defensive bonuses but little damage reduction
#Medium armor would be chain mail or composite armors
#They typically offer a good mix between defense and damage reduction
#Heavy armor would be plate mail and other armors of solid metal construction
#They typically present easy targets but are very solid
class Armor(Item):
    #Defense adds a bonus to DS vs Physical attacks
    #Damage_Reduction reduces damage from incoming Physical attacks
    def __init__(self, defense, damage_reduction, name, desc):
        Item.__init__(self, name, desc)
        #code here
        self.defense = defense
        self.damage_reduction = damage_reduction
        self.required_strength = self.calc_required_strength()

    def calc_required_strength(self):
        return int(self.damage_reduction // 2.6)

