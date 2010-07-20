from Player import Adventurer
from Creature_Factory import * 
from Proc import *
from Item_Module import Healing_Potion
from Arena import Arena
from Distributed_Random import Distributed_Random

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
        high = 0
        cnt = 0
        wpn = None
        while cnt < 1000:
            w = self.wf.generate_by_quality(2)
            if w.required_strength > high:
                high = w.required_strength
                wpn = w
            cnt += 1
        print high
        return wpn

    def reset(self, diff):
        #self.player.add_weapon(self.wf.generate_by_quality(2))
        self.player = self.cf.generate_difficulty(diff)
        self.gen = self.cf.generate_difficulty(diff)
        self.player.primary_weapon().proc.append(Poison_Proc(100,5,200))
        #self.gen.add_effect(DOT_Effect(3,200))
        self.arena = Arena(self.player, self.gen)
