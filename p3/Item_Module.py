#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Item_Module.py

from Item_Interface import Item_Interface
from Effect import Effect

class Item(Item_Interface):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def output_result_first(self, result, damage):
        print "You used a Base class for %s damage... stupid" % result 

    def output_result_third(self, result, damage):
        print "hits you with an abstract base class for %s damage, ouch" % result

class Potion(Item):
    def __init__(self, name, description, value):
        Item.__init__(self, name, description)
        self.value = value

    def output_result_first(self, result, damage):
        print "You drink a %s" % self.name

    def output_result_third(self, result, damage):
        print "drinks a %s" % self.name

    def attack_post(self, attacker, defender):
        attacker.hp += self.value

class Spell(Item):
    def __init__(self, name, description, difficulty, min_damage, max_damage):
        Item.__init__(self, name, description)
        self.difficulty = difficulty
        self.min_damage = min_damage
        self.max_damage = max_damage

    def print_fail_first(self):
        print "You attempt to cast %s... but fail" % self.name

    def print_fail_third(self):
        print "mutters a chant, nothing happens"

    def output_result_first(self, result, damage):
        if result >= self.difficulty:
            print "You cast %s" % self.name, "for %s damage" % damage
        else:
            self.print_fail_first()

    def output_result_third(self, result, damage):
        if result >= self.difficulty:
            print "casts %s" % self.name, "on you for %s damage" % damage
        else:
            self.print_fail_third()

class Stun_Spell(Spell):
    def __init__(self, name, description, difficulty, duration):
        Spell.__init__(self, name, description, difficulty, 0, 0)
        self.duration = duration

    def output_result_first(self, result, damage):
        self.result = result
        if result >= self.difficulty:
            print "You cast %s" % self.name, "stunning your opponent for %s rounds!" % self.duration
        else:
            self.print_fail_first()

    def output_result_third(self, result, damage):
        self.result = result
        if result >= self.difficulty:
            print "casts %s" % self.name, "stunning you for %s rounds!" % self.duration
        else:
            self.print_fail_third()
    
    def attack_post(self, attacker, defender):
        if self.result >= self.difficulty:
            defender.add_effect(Effect(0, self.duration, 0))
