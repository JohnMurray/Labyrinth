#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Item_Module.py

from Item_Interface import Item_Interface
from Effect import *
import random

#Base class from which all items descend
#Siblings include Potion, Spell, Weapon
class Item(Item_Interface):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    #This method is the common interface that all items use to output the result of their use
    #the "first" refers to first person, as in the player used the item
    def output_result_first(self, result):
        print "You used a Base class for %s damage... stupid" % result 

    #"third" here refers to third person, a creature used the item
    def output_result_third(self, result):
        print "hits you with an abstract base class for %s damage, ouch" % result

class Potion(Item):
    def __init__(self, name, description):
        Item.__init__(self, name, description)

    #output first for the use of a potion
    def output_result_first(self, result):
        print "You drink a %s" % self.name

    #output third for the use of a potion
    def output_result_third(self, result):
        print "drinks a %s" % self.name

class Healing_Potion(Potion):
    def __init__(self, name, description, min_heal, max_heal):
        Potion.__init__(self, name, description)
        self.min_heal = min_heal
        self.max_heal = max_heal

    #Special effects like healing the player are accomplished via these hooks
    def attack_post(self, attacker, defender):
        attacker.heal(random.randint(self.min_heal, self.max_heal))

class Defense_Potion(Potion):
    def __init__(self, name, description, duration, bonus):
        Potion.__init__(self, name, description)
        self.duration = duration
        self.bonus = bonus

    #Give the user a Defense_Effect
    def attack_post(self, attacker, defender):
        attacker.add_effect(Defense_Effect(self.duration, self.bonus))

class Offense_Potion(Potion):
    def __init__(self, name, description, duration, bonus):
        Potion.__init__(self, name, description)
        self.duration = duration
        self.bonus = bonus

    #Give the user an Offense_Effect
    def attack_post(self, attacker, defender):
        attacker.add_effect(Offense_Effect(self.duration, self.bonus))

class Magic_Defense_Potion(Potion):
    def __init__(self, name, description, duration, bonus):
        Potion.__init__(self, name, description)
        self.duration = duration
        self.bonus = bonus

    #Give the user a Defense_Effect
    def attack_post(self, attacker, defender):
        attacker.add_effect(Magic_Defense_Effect(self.duration, self.bonus))

class Magic_Offense_Potion(Potion):
    def __init__(self, name, description, duration, bonus):
        Potion.__init__(self, name, description)
        self.duration = duration
        self.bonus = bonus

    #Give the user an Offense_Effect
    def attack_post(self, attacker, defender):
        attacker.add_effect(Magic_Offense_Effect(self.duration, self.bonus))

class Spell(Item):
    def __init__(self, name, description, difficulty):
        Item.__init__(self, name, description)
        self.difficulty = difficulty

    #output a failed spell message first person
    def print_fail_first(self):
        print "You attempt to cast %s... but fail" % self.name

    #output a failed spell message third person
    def print_fail_third(self):
        print "mutters a chant, nothing happens"

    #output message for use a spell, first person
    def output_result_first(self, result):
        if result >= self.difficulty:
            print "You cast %s" % self.name
        else:
            self.print_fail_first()

    #output message for use of a spell, third person
    def output_result_third(self, result):
        if result >= self.difficulty:
            print "casts %s" % self.name
        else:
            self.print_fail_third()

#Attack spells represent damaging spells
#Subclass of Spell
class Attack_Spell(Spell):
    def __init__(self, name, description, difficulty, min_damage, max_damage):
        Spell.__init__(self, name, description, difficulty)
        self.min_damage = min_damage
        self.max_damage = max_damage

    #Output the result of an attack spell, first person
    def output_result_first(self, result, damage=0):
        self.result = result
        if result >= self.difficulty:
            print "You cast %s" % self.name, "hitting for %s damage" % damage
        else:
            self.print_fail_first()

    #Output the result of an attack spell, first person
    def output_result_third(self, result, damage=0):
        self.result = result
        if result >= self.difficulty:
            print "casts %s on you," % result, "hitting for %s damage." % damage
        else:
            self.print_fail_third()

#Defense Spells grant defensive bonuses vs Physical attacks
#Duration is how long the effect lasts and bonus is how big the effect is
class Defense_Spell(Spell):
    def __init__(self, name, description, difficulty, bonus, duration=3):
        Spell.__init__(self, name, description, difficulty)
        self.bonus = bonus
        self.duration = duration

    def output_result_first(self, result):
        self.result = result
        if result >= self.difficulty:
            print "A glowing aura surrounds you, protecting you from harm"
        else:
            self.print_fail_first()

    def output_result_third(self, result):
        self.result = result
        if result >= self.difficulty:
            print "is suddenly wrapped in a protective aura"
        else:
            self.print_fail_third()

    #this hook creates the effect that grants the user the bonus
    #Note this appends the effect to the attacker (person using the spell)
    #Generally spells could be targeted, but this game is really simple
    def attack_post(self, attacker, defender):
        if self.result >= self.difficulty:
            attacker.effect.append(Defense_Effect(self.duration, self.bonus))

#Stun Spells stun the victim, rendering them unable to act
class Stun_Spell(Spell):
    def __init__(self, name, description, difficulty, duration):
        Spell.__init__(self, name, description, difficulty)
        self.duration = duration

    def output_result_first(self, result):
        self.result = result
        if result >= self.difficulty:
            print "You cast %s" % self.name, "stunning your opponent for %s rounds!" % self.duration
        else:
            self.print_fail_first()

    def output_result_third(self, result):
        self.result = result
        if result >= self.difficulty:
            print "casts %s" % self.name, "stunning you for %s rounds!" % self.duration
        else:
            self.print_fail_third()
   
    #This is where the stun effect is applied, again applied to the defender all the time
    def attack_post(self, attacker, defender):
        if self.result >= self.difficulty:
            defender.add_effect(Stun_Effect(self.duration))
