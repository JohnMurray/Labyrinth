from Player import Adventurer
from Creature_Factory import * 
from Proc import *
from Item_Module import Healing_Potion
from Arena import Arena
from Distributed_Random import Distributed_Random
import random

class Test:
    def __init__(self):
        self.wf = Weapon_Factory()
        self.cf = Creature_Factory()
        self.af = Armor_Factory()
        #self.player.add_weapon(self.wf.generate_by_quality(2))
        #self.player = self.cf.generate_player_stats(self.player)
        #self.player.primary_weapon().proc.append(Leech_Proc(50,20))
        #self.player.add_armor(self.af.generate_high_quality())
        self.reset(1)

    def fight(self, diff):
        self.reset(diff)
        while self.player.hp > 0 and self.gen.hp > 0:
            self.arena.attack()
            print "Gen: HP = %s" % self.gen.hp, "/%s" % self.gen.max_hp,
            print "OS = %s" % self.gen.OS, "DS = %s" % self.gen.DS,
            print "WPN Score = %s" % self.gen.primary_weapon().score

            print "PLR: HP = %s" % self.player.hp, "/%s" % self.player.max_hp,
            print "OS = %s" % self.player.OS, "DS = %s" % self.player.DS,
            print "WPN Score = %s" % self.player.primary_weapon().score

        if self.player.hp > 0:
            print "Player WIN"
        else:
            print "Player LOSS"

    def temp(self):
        wpn = self.wf.generate_by_type(random.randint(0,3),random.randint(0,2))
        agi_high = 0
        agi_low = 10
        str_high = 0
        str_low = 10
        cnt = 0
        while cnt < 1000:
            if wpn.required_agility > agi_high:
                agi_high = wpn.required_agility
            if wpn.required_agility < agi_low:
                agi_low = wpn.required_agility
            if wpn.required_strength > str_high:
                str_high = wpn.required_strength
            if wpn.required_strength < str_low:
                str_low = wpn.required_strength
            wpn = self.wf.generate_by_type(random.randint(0,3), random.randint(0,2))
            cnt += 1
        print agi_low, agi_high, str_low, str_high

    def reset(self, diff):
        self.player = Adventurer("Valna",300)
        self.player.add_weapon(self.wf.generate_by_quality(2))
        self.player.add_armor(self.af.generate_by_quality(2))
        self.gen = self.cf.generate_difficulty(diff)
        #self.player.primary_weapon().proc.append(Poison_Proc(50,1,10))
        #self.gen.add_effect(DOT_Effect(3,200))
        self.arena = Arena(self.player, self.gen)
