#Authors: Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#Due: July 19th, 2010
#File Arena.py

import Player
import random
from Weapon_Module import Weapon

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

        result = self.fight(attacker, victim)
        if isinstance(attacker.current_attack(), Weapon):
            damage = self.calc_damage(attacker, victim)
            victim.hp -= damage
        else:
            damage = 0

        #Items control their own output based on the result and the context (first/third person)
        #Outcome of the attack has not been realized
        if attacker == self.player:
            attacker.current_attack().output_result_first(result, damage)
        else:
            print "%s" % attacker.name,
            attacker.current_attack().output_result_third(result, damage)

        #Post hooks
        if attacker.current_attack() != None:
            attacker.current_attack().attack_post(attacker, victim)
        
        if victim.armor != None and len(victim.armor) != 0:
            victim.primary_armor().defense_post(attacker, victim)

    def fight(self, attacker, victim):        
       #one attack, ambivalent to player/creature
       #kickin' it old school with THAC0
       return attacker.OS - victim.DS + random.randint(1, 20)

    def calc_damage(self, attacker, victim):
        #calculates damage for an attack
        #does not currently account for elemental or effects
        damage = random.randint(attacker.current_attack().min_damage, attacker.current_attack().max_damage)
        return damage - victim.primary_armor().damage_reduction

    def magic_attack(self, id):
        self.player.primary = self.player.spells[id]
        #Hard coded for now, will add stats or something that effect magic strength
        self.player.OS = 0
        self.player.DS = self.player.primary_armor().defense

        self.creature.OS = self.creature.primary_weapon().chance
        self.creature.DS = 0
        
        self.turn()
    
    def attack(self):
        self.player.primary = self.player.primary_weapon()
        
        self.player.OS = self.player.current_attack().chance
        self.player.DS = self.player.primary_armor().defense

        #currently hard coded attack action for opponent
        self.creature.OS = self.creature.primary_weapon().chance
        self.creature.DS = self.creature.primary_armor().defense
        
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
        #player attacks first
        self.round(self.player, self.creature)
        if self.creature.hp > 0:
            #it lives! Counter attack!
            self.round(self.creature, self.player)

