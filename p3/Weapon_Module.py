#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Weapon.py

from Item_Module import Item
import random
from Distributed_Random import Distributed_Random

class Weapon(Item):
    
    def __init__(self, min_damage, max_damage, chance, name, description):
        Item.__init__(self, name, description) 
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.abs_damage = min_damage + max_damage * 2

        if chance > 20:
            self.chance = 20
        else:
            self.chance = chance

        self.speed = self.calc_speed() 
        self.required_strength = self.calc_required_strength()
        self.required_agility = self.calc_required_agility()
        self.score = self.score()
        self.proc = list()
        return

    def output_result_first(self, result, damage=0):
        self.result = result
        self.damage = damage
        if result >= 0:
            print "You attack for %s damage" % damage
        else:
            print "You attack, but miss"

    def output_result_third(self,  result, damage=0):
        self.result = result
        self.damage = damage
        if result >= 0:
            print "attacks you for %s damage" % damage
        else:
            print "attacks you, but misses"
   
    def attack_post(self, attacker, defender):
        for p in self.proc:
            p.attack_post(attacker, defender, self.result, self.damage)

    #Quick way of quantifying a weapon's statistics 
    #not a very accurate estimate of actual quality
    def score(self):
        score = self.min_damage
        score += 2 * self.max_damage
        score += 5 * self.chance
        score += 3 * self.speed
        return score

    def calc_required_strength(self):
        return self.abs_damage // 18 

    def calc_required_agility(self):
        req = self.chance - 4
        if req < 0:
            req = 0
        return req

    def calc_speed(self):
        speed = 21 - (self.abs_damage // 10)
        return speed

    def add_proc(self, proc):
        self.proc.append(proc)

class Sword_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, name, description):
        Weapon.__init__(self, min_damage, max_damage, chance, name, description)

    #In production could would have a database of attack descriptions
    #choosing them at random based on result and damage (critical hits)
    def output_result_first(self, result, damage=0):
        self.result = result
        self.damage = damage
        if result >= 0:
            print "You swing your %s," % self.name,
            print "hitting for %s damage." % damage
        else:
            print "You swing your %s, but miss" % self.name

    def output_result_third(self, result, damage=0):
        self.result = result
        self.damage = damage
        if result >= 0:
            print "swings a %s at you," % self.name,
            print "hitting you for %s damage." % damage
        else:
            print "swings a %s at you, but misses." % self.name

class Arrow_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, name, description):
        Weapon.__init__(self, min_damage, max_damage, chance, name, description)

    def output_result_first(self, result, damage=0):
        self.result = result
        self.damage = damage
        aim = "You aim and fire your " + self.name + ","
        if result>= 0:
            print aim,
            print "it hits the target for %s damage." % damage
        else:
            print aim,
            print "but miss the target."

    def output_result_third(self, result, damage=0):
        self.result = result
        self.damage = damage
        aim = "aims and fires a " + self.name + " at you,"
        if result >= 0:
            print aim,
            print "it hits you for %s damage." % damage
        else:
            print aim,
            print "it flies wide."

    def calc_required_agility(self):
        abs_damage = self.min_damage + self.max_damage * 2
        return abs_damage // 18 

    def calc_required_strength(self):
        return self.calc_required_agility() // 2

    def calc_speed(self):
        speed = 18 - self.abs_damage // 10
        return speed

class Spear_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, name, description):
        Weapon.__init__(self, min_damage, max_damage, chance, name, description)

    def output_result_first(self, result, damage=0):
        self.result = result
        self.damage = damage
        tmp = "You thrust your " + self.name + " at your foe,"
        if result >= 0:
            print tmp,
            print "you hit your target for %s damage." % damage
        else:
            print tmp,
            print "but miss."

    def output_result_third(self, result, damage=0):
        self.result = result
        self.damage = damage
        tmp = "thrusts a " + self.name + " at you,"
        if result >= 0:
            print tmp,
            print "it hits you for %s damage" % damage
        else:
            print tmp,
            print "but misses you."    
        


class Hammer_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, name, description):
        Weapon.__init__(self, min_damage, max_damage, chance, name, description)


    def output_result_first(self, result, damage=0):
        self.result = result
        self.damage = damage
        tmp = "You swing your " + self.name + " at the enemy,"
        if result >= 0:
            print tmp,
            print "bashing it for %s damage." % damage
        else:
            print tmp,
            print "WHIFF!"

    def output_result_third(self, result, damage=0):
        self.result = result
        self.damage = damage
        tmp = "swings a " + self.name + " at you,"
        if result >= 0:
            print tmp,
            print "slamming you for %s damage." % damage
        else:
            print tmp,
            print "you dodge."

    def calc_speed(self):
        speed = 14 - self.abs_damage // 10
        return speed

#Probably not how I would implement wands ideally. Quicky and dirty, right?
class Wand_Weapon(Weapon):
    def __init__(self, min_damage, max_damage, chance, name, description):
        Weapon.__init__(self, min_damage, max_damage, chance, name, description)
        self.required_intel = self.calc_required_intel()

    def output_result_first(self, result, damage=0):
        self.result = result
        self.damage = damage
        tmp = "You wave your " + self.name + " at the enemy,"
        if result >= 0:
            print tmp,
            print "the bolt of magical energy lands for %s damage." % damage
        else:
            print tmp,
            print "but you miss the mark."

    def output_result_third(self, result, damage=0):
        self.result = result
        self.damage = damage
        tmp = "waves a " + self.name + " at you, a blast of magical energy flies toward you,"
        if result >= 0:
            print tmp,
            print "striking you for %s damage." % damage
        else:
            print tmp,
            print "but misses."

    def calc_required_intel(self):
        return self.abs_damage // 18

    def calc_required_strength(self):
        return 1

    def calc_required_agility(self):
        return 1

    def calc_speed(self):
        speed = 14 - self.abs_damage // 10
        return speed
