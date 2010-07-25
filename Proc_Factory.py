#Authors Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#File: Proc_Factory.py

from Proc import *
from Distributed_Random import Distributed_Random

class Proc_Factory:
    def __init__(self):
        self

    def generate_weapon_proc(self, quality=0):
        #returns a random Weapon_Proc
        procs = {
                    1: self.generate_leech_proc,
                    2: self.generate_poison_proc,
                    3: self.generate_stun_proc,
                }
        if quality == 0:
            #default, random quality
            return procs[random.randint(1,3)](random.randint(1,3))
        else:
            return procs[random.randint(1,3)](quality)


        
    def generate_armor_proc(self, quality=0):
        #returns a random Armor_Proc
        #only have thorn right now
        if quality == 0:
            return self.generate_thorn_proc(random.randint(1,3))
        else:
            return self.generate_thorn_proc(quality)

    def generate_leech_proc(self, quality=1):
        #generates a leech proc of variable quality
        dist = Distributed_Random()
        chance_min = 15
        chance_max = 30
        perc_min = 5
        perc_max = 15
        if quality == 2:
            chance_max = 50
            perc_min = 10
            perc_max = 20
        if quality == 3:
            chance_min = 40
            chance_max = 75
            perc_min = 20
            perc_max = 30

        chance = dist.randint(chance_min, chance_max)
        percent = dist.randint(perc_min, perc_max)
        return Leech_Proc(chance, percent)

    def generate_thorn_proc(self, quality=1):
        #generates a thorn proc of variable quality
        dist = Distributed_Random()
        chance_min = 15
        chance_max = 30
        damage_min = 5
        damage_max = 10
        if quality == 2:
            chance_max = 50
            damage_min = 7
            damage_max = 20
        if quality == 3:
            chance_min = 40
            chance_max = 75
            damage_max = 30
            damage_min = 15

        chance = dist.randint(chance_min, chance_max)
        damage = dist.randint(damage_min, damage_max)
        return Thorn_Proc(chance, damage)

    def generate_poison_proc(self, quality=1):
        #generates a poison proc of variable quality
        dist = Distributed_Random()
        dura_max = 4
        dura_min = 1
        chance_min = 15
        chance_max = 30
        damage_min = 3
        damage_max = 10
        if quality == 2:
            dura_max = 6
            chance_max = 50
            damage_min = 5
            damage_max = 15
        if quality == 3:
            dura_min = 3
            dura_max = 8
            chance_min = 40
            chance_max = 75
            damage_min = 10
            damage_max = 20
        
        chance = dist.randint(chance_min, chance_max)
        dura = dist.randint(dura_min, dura_max)
        damage = dist.randint(damage_min, damage_max)
        return Poison_Proc(chance, dura, damage)

    def generate_stun_proc(self, quality=1):
        #returns a stun proc of variable quality
        dist = Distributed_Random()
        dura_max = 2
        dura_min = 1 
        chance_min = 15
        chance_max = 30
        if quality == 2:
            dura_max = 4
            chance_max = 50
        if quality == 3:
            dura_max = 6
            dura_min = 3
            chance_min = 40
            chance_max = 75

        return Stun_Proc(dist.randint(chance_min, chance_max), dist.randint(dura_min, dura_max))
