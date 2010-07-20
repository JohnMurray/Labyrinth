#Authors: Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#Due: July 19th, 2010
#File Arena.py

import random
import math
from Weapon_Module import Weapon
from Weapon_Module import Arrow_Weapon
from Armor import Armor
from Item_Module import *

#Note - this class does all the cool stuff
class Arena:
    def __init__(self, player, creature):
        #Creates an Arena instance
        self.player = player
        self.creature = creature

    def round(self, attacker, victim):
        #Represents one round of a turn, an atomic action either potion, spell, weapon attack
        #Hooks in place for items
        attacker.current_attack().attack_pre(attacker, victim)
        victim.primary_armor().defense_pre(attacker, victim)

        result = self.fight(attacker, victim)
        damage = self.calc_damage(attacker, victim)
        
        if damage < 0:
            damage = 0
        
        if result > 0:
            victim.hp -= damage

        if attacker == self.player:
            if damage > 0:
                attacker.current_attack().output_result_first(result, damage)
            else:
                attacker.current_attack().output_result_first(result)
        else:
            if damage > 0:
                print attacker.name,
                attacker.current_attack().output_result_third(result, damage)
            else:
                print attacker.name,
                attacker.current_attack().output_result_third(result)

        #Post hooks
        attacker.current_attack().attack_post(attacker, victim)
        victim.primary_armor().defense_post(attacker, victim)

    def fight(self, attacker, victim):        
       #one attack, ambivalent to player/creature
       #kickin' it old school with THAC0
       return attacker.OS - victim.DS + random.randint(1, 20)

    def calc_damage(self, attacker, victim):
        #calculates damage for an attack
        #does not currently account for elemental or effects
        if isinstance(attacker.current_attack(), Weapon): 
            damage = random.randint(attacker.current_attack().min_damage, attacker.current_attack().max_damage)
            damage -= victim.primary_armor().damage_reduction 
            damage -= victim.stamina // 2
            if not isinstance(attacker.current_attack(), Arrow_Weapon):
                damage += attacker.strength * 2 
            return damage
        elif isinstance(attacker.current_attack(), Attack_Spell):
            damage = random.randint(attacker.current_attack().min_damage, attacker.current_attack().max_damage)
            damage += attacker.intel
            #Possible location for elemental resistances
            return damage
        else:
            return 0

    def magic_attack(self, id):
        self.player.primary = self.player.spells[id]
        self.player.OS = self.player.calc_OS_Magic()
        self.creature.DS = self.creature.calc_DS_Magic()

        #Select creature attack
        self.select_creature_attack()
        self.turn()
    
    def attack(self):
        self.player.primary = self.player.primary_weapon()
        self.player.OS = self.player.calc_OS_Physical() 
        self.creature.DS = self.creature.calc_DS_Physical()

        self.select_creature_attack() 
        self.turn()

    def potion(self, id):
        self.player.primary = self.player.potion[id]
        self.player.OS = 0
        self.creature.DS = self.creature.calc_DS_Physical()

        self.select_creature_attack()
        self.turn()
    
    def select_creature_attack(self):
        self.creature.select_attack()
        #Determine if creature selected a spell or something else
        #Calculate OS/DS accordingly
        if isinstance(self.creature.primary, Spell):
            self.creature.OS = self.creature.calc_OS_Magic()
            self.player.DS = self.player.calc_DS_Magic()
        else:
            self.creature.OS = self.creature.calc_OS_Physical()
            self.player.DS = self.player.calc_DS_Physical()

    def turn(self):
        #self.creature.select_attack()
        #check for player stun
        #possible iniative roll here, for now alternate attacks
        p_attacks = self.player.calc_num_attacks()
        c_attacks = self.creature.calc_num_attacks()
        while (p_attacks > 0 or c_attacks > 0) and (self.player.hp > 0 and self.creature.hp >0):
            if self.player.is_stunned():
                #creature gets a freebie
                if c_attacks > 0 and c.hp > 0:
                    self.round(self.creature, self.player)
                    self.update_effects()
            else:
                #player attacks first
                if p_attacks > 0:
                    self.round(self.player, self.creature)
                if self.creature.hp > 0 and not self.creature.is_stunned() and c_attacks > 0:
                    #it lives! Counter attack!
                    self.round(self.creature, self.player)
                self.update_effects()
                c_attacks -= 1
                p_attacks -= 1

    def update_effects(self):
        #reduce the duration of all effects by one turn for creature and player 
        player_pending = list()
        creature_pending = list()
        
        for e in self.player.effect:
            e.apply(self.player)
            e.duration -= 1
            if(e.duration == 0):
                player_pending.append(e)

        for e in self.creature.effect:
            e.apply(self.creature)
            e.duration -= 1
            if(e.duration == 0):
                creature_pending.append(e)

        for p in player_pending:
            self.player.effect.remove(p)
        for p in creature_pending:
            self.creature.effect.remove(p)
        

