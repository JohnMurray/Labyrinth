from Item_Module import *
from Weapon_Module import *
from Player import *
from Arena import Arena


class Test:
    def __init__(self):
        self.player = Adventurer("Valna", 500)
        self.wf = Weapon_Factory()
        self.cf = Creature_Factory()
        self.af = Armor_Factory()
        self.player.add_weapon(self.wf.generate_by_quality(2))
        self.player.add_armor(self.af.generate_high_quality())
        self.gen = self.cf.generate_difficulty(10)
        self.arena = Arena(self.player, self.gen)

    def fight(self):
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

        self.reset()

    def reset(self):
        self.player.hp = 500
        self.player.weapon = list()
        self.player.armor = list()
        self.player.add_weapon(self.wf.generate_by_quality(2))
        self.player.add_armor(self.af.generate_high_quality())
        self.gen = self.cf.generate_difficulty(10)
        self.arena = Arena(self.player, self.gen)
