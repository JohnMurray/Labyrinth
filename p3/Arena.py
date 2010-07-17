#Authors: Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#Due: July 19th, 2010
#File Arena.py

import Player
import CLI_Interface
import random

#Note - this class does all the cool stuff
class Arena:
    def __init__(self, player, creature):
        #Creates an Arena instance
        self.player = player
        self.creature = creature

    def round(self, attacker, victim):
        #Represents one round of a turn, an atomic action either potion, spell, weapon attack
        #Hooks in place for items
        if attacker.current_attack() != None:
            attacker.current_attack().attack_pre(attacker, victim)

        if victim.armor != None and len(victim.armor) != 0:
            victim.primary_armor().defense_pre(attacker, victim)

        #Items control their own output based on the result and the context (first/third person)
        #Outcome of the attack has not been realized
        if attacker == self.player:
            attacker.current_attack().output_result_first(self.fight(attacker, victim))
        else:
            print "%s" % attacker.name,
            attacker.current_attack().output_result_third(self.fight(attacker, victim))

        #Post hooks
        if attacker.current_attack() != None:
            attacker.current_attack().attack_post(attacker, victim)
        
        if victim.armor != None and len(victim.armor) != 0:
            victim.primary_armor().defense_post(attacker, victim)

    def fight(self, attacker, victim):        
       #one attack, ambivalent to player/creature
       #kickin' it old school with THAC0
       return attacker.OS - victim.DS + random.randint(1, 20)

    def magic_attack(self, id):
        self.player.primary = self.player.spells[id]
        #Hard coded for now, will add stats or something that effect magic strength
        self.player.OS = 0
        
        if self.player.primary_armor() != None:
            self.player.DS = self.player.primary_armor().chance
        else:
            self.player.DS = 0
        
        if self.creature.primary_weapon() != None: 
            self.creature.OS = self.creature.primary_weapon().chance
        else:
            self.creature.OS = 0

        self.creature.DS = 0
        
        self.turn()
    
    def attack(self):
        self.player.primary = self.player.primary_weapon()
        
        self.player.OS = self.player.primary.chance
        
        if self.player.primary_armor() != None:
            self.player.DS = self.player.primary_armor().chance
        else:
            self.player.DS = 0

        #currently hard coded attack action for opponent
        if self.creature.primary_weapon() != None:
            self.creature.OS = self.creature.primary_weapon().chance
        else:
            self.creature.OS = 0

        if self.creature.primary_armor() != None:
            self.creature.DS = self.creature.primary_armor().chance
        else:
            self.creature.DS = 0
        
        self.turn()

    def turn(self):
        #self.creature.select_attack()
        #player attacks first
        self.round(self.player, self.creature)
        if self.creature.hp > 0:
            #it lives! Counter attack!
            self.round(self.creature, self.player)

