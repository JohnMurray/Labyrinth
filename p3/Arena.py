#Authors: Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#Due: July 19th, 2010
#File Arena.py

import Player
import random
from Weapon_Module import Weapon
from Item_Module import Potion
from Item_Module import Attack_Spell

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
        if isinstance(attacker.current_attack(), Potion):
            return 0
        elif isinstance(attacker.current_attack(), Weapon): 
            damage = random.randint(attacker.current_attack().min_damage, attacker.current_attack().max_damage)
            return damage - victim.primary_armor().damage_reduction
        elif isinstance(attacker.current_attack(), Attack_Spell):
            damage = random.randint(attacker.current_attack().min_damage, attacker.current_attack().max_damage)
            #Possible location for elemental resistances
            return damage
        else:
            return 0

    def magic_attack(self, id):
        self.player.primary = self.player.spells[id]
        #Hard coded for now, will add stats or something that effect magic strength
        self.player.OS = 0
        self.player.OS += self.player.offense_bonus_magic()
        self.player.DS = self.player.primary_armor().defense
        self.player.DS += self.player.defense_bonus()

        self.creature.OS = self.creature.primary_weapon().chance
        self.creature.OS += self.creature.offense_bonus()
        self.creature.DS = 0
        self.creature.DS += self.creature.defense_bonus_magic() 
        
        self.turn()
    
    def attack(self):
        self.player.primary = self.player.primary_weapon()
        
        self.player.OS = self.player.current_attack().chance
        self.player.OS += self.player.offense_bonus()
        self.player.DS = self.player.primary_armor().defense
        self.player.DS += self.player.defense_bonus()

        #currently hard coded attack action for opponent
        self.creature.OS = self.creature.primary_weapon().chance
        self.creature.OS += self.creature.offense_bonus()
        self.creature.DS = self.creature.primary_armor().defense
        self.creature.DS += self.creature.defense_bonus()
        
        self.turn()

    def potion(self, id):
        self.player.primary = self.player.potion[id]
        self.player.OS = 0
        self.player.DS = self.player.primary_armor().defense

        #replace with creature method for selecting attack and calculating OS/DS
        self.creature.OS = self.creature.primary_weapon().chance
        self.creature.DS = self.creature.primary_armor().defense

        self.turn()
        
    def turn(self):
        #self.creature.select_attack()
        #check for player stun
        if self.player.is_stunned():
           #creature gets a freebie
           self.round(self.creature, self.player)
           self.update_effects()
           self.turn()
        else:
            #player attacks first
            self.round(self.player, self.creature)
            if self.creature.hp > 0 and not self.creature.is_stunned():
                #it lives! Counter attack!
                self.round(self.creature, self.player)
            self.update_effects()

    def update_effects(self):
        #reduce the duration of all effects by one turn for creature and player 
        player_pending = list()
        creature_pending = list()
        
        for e in self.player.effect:
            e.duration -= 1
            if(e.duration == 0):
                player_pending.append(e)

        for e in self.creature.effect:
            e.duration -= 1
            if(e.duration == 0):
                creature_pending.append(e)

        for p in player_pending:
            self.player.effect.remove(p)
        for p in creature_pending:
            self.creature.effect.remove(p)
        

