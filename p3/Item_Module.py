#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Item_Module.py

from Item_Interface import Item_Interface

class Item(Item_Interface):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def output_result_first(self, result):
        print "You used a Base class for %s damage... stupid" % result 

    def output_result_third(self, result):
        print "hits you with an abstract base class for %s damage, ouch" % result

class Potion(Item):
    def __init__(self, name, description):
        Item.__init__(self, name, description)

class Spell(Item):
    def __init__(self, name, description, difficulty, damage):
        Item.__init__(self, name, description)
        self.difficulty = difficulty
        self.damage = damage

    def output_result_first(self, result):
        if result >= self.difficulty:
            print "You cast %s" % self.name, "for %s damage" % self.damage
        else:
            print "You attempt to cast %s... but fail" % self.name

    def output_result_third(self, result):
        if result >= self.difficulty:
            print "casts %s" % self.name, "on you for %s damage" % self.damage
        else:
            print "mutters a chant, nothing happens"
