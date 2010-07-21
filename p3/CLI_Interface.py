#Authors: Brad Stephens, John Murray 
#sProject: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: CLI_Interface.py

import random
import Arena
import sys
import Treasure

from Weapon_Module import *
from Player import *
from Item_Module import *
from Armor import *
from Arena import Arena
from Creature_Factory import *
from Treasure import Treasure

#class: CLI
#purpose: A Command Line Interface class that handles the parsing of user
#         input and validation of input, the execution of non-turn based
#         commands, and returns the values of turn-based commands.
class CLI:
    def __init__(self, player, level):
        
        self.player = player
        self.level = level
        
        #lists commands with a dict and tuple that defines
        #(cli-controlled/handled, options(name), description(for help), param_type)
        self.commands = {
            "help" : (True, '', 'Shows the help dialog all available commands (not much un-similar to this page)turn/move.', None),
            "vhelp" : (True, 'command', 'Verbose help command. Show description for individual commands. (type `vhelp *` to see all commands)', str),
            "map" : (True, '', 'Shows the map of the Level and where all the creatures on on the map', None),
            "status" : (True, '', 'Shows current player stats.', None),
            "move-north": (False, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "move-east": (False, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "move-south": (False, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "move-west": (False, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "flee": (True, '', 'Similar to move-* command. Allows you to flee a room where monster is, but the room is random and you may drop weapons, items, or gold when fleeing.', None),
            "attack": (True, '', 'Attack an opponent when in battle with primary weapon.', None),
            "magic-attack": (True, 'id', 'Attack an opponent with a spell. Must give id.(Use the inventory-spell to get spell id).', int),
            "look-around": (True, '', 'Look at all the items currently in the room. Shows item name and id.', None),
            "study": (True, 'id', 'View an item in the room in great detail. A.K.A - View the item\'s stats and/or description, etc. Must give item id. (use look-around to get item id)', int),
            "pickup": (True, 'id', 'Pick up and item in the room. Must give item id. (use look-around to get item id)', int),
            "switch-weapon": (True, 'id', 'Change your primary weapon. Must give id. (use weapon-inventory to get id)', int),
            "switch-armor":(True, 'id', 'Change your primary armor. Must give id. (use inventory-armor to get id)', int),
            "inventory-weapon": (True, '', 'List your current weapon inventory. View each weapon\'s name and id.', None),
            "inventory-armor": (True, '', 'List your current armor inventory. View each armor\'s name and id.', None),
            "inventory-potion": (True, '', 'List your current potion inventory. View each potion\'s name and id.', None),
            "inventory-spell": (True, '', 'List your current spell inventory. View each spell\'s name and id.', None),
            "inspect-weapon": (True, 'id', 
                    'View an weapon in the inventory in great detail. A.K.A - View the weapon\'s stats and/or description, etc. Must give id. (use inventory-weapon to get item id)', int),
            "inspect-armor": (True, 'id', 
                    'View an armor in the inventory in great detail. A.K.A - View the armor\'s stats and/or description, etc. Must give id. (use inventory-armor to get item id)', int),
            "inspect-potion": (True, 'id', 
                    'View an potion in the inventory in great detail. A.K.A - View the potion\'s stats and/or description, etc. Must give id. (use inventory-potion to get item id)', int),
            "inspect-spell": (True, 'id', 
                    'View an spell in the inventory in great detail. A.K.A - View the spell\'s stats and/or description, etc. Must give id. (use inventory-spell to get item id)', int),
            "drop-weapon": (True, 'id', 'Drop a weapon in the inventory. Must give weapon id. (use inventory-weapon to get weapon id)', int),
            "drop-armor": (True, 'id', 'Drop an armor in the inventory. Must give armor id. (use inventory-armor to get armor id)', int),
            "drop-potion": (True, 'id', 'Drop a potion in the inventory. Must give potion id. (use inventory-potion to get potion id)', int),
            "drop-spell": (True, 'id', 'Drop an spell in the inventory. Must give spell id. (use inventory-spell to get spell id)', int),
            "buy-attribute": (True, 'attribute', 'Buy a specific attribute point with your current AP.', str),
            "use-potion": (True, 'id', 'Use a potion.', int),
        }
        
        self.command = ''
        self.params = ''
    
    #def: get_command
    #purpose: return a command from the user.
    #note: This command is a recursive definition
    #note: If a non-turn command is entered, it is executed
    #returns: list() in form of:
    #       0 => command
    #       1 => parameter or empty string (for no-parameter)
    def get_command(self):
        print "command> "
        command = raw_input()
        while( not self.valid_command(command) ):
            command = raw_input()
            print "Error: Command is not of valid syntax.  `command [options]`"
            print "command>"
        (self.command, seperator, self.params) = command.partition(" ")
        
        #check and see if the command exists
        if( self.command_defined() ):
            #validate the parameter (if required)
            if( self.validate_parameter() ):
                #check if the parameter is execute locally
                if( self.cli_handled() ):
                    self.execute()
                    return self.get_command()
                else:
                    return [self.command, self.params]
                
            #parameter validation has faild (aka - none given when one or more needed)
            else:
                print "Error: Parameter must be given and of correct type. Please refer to the help guide by typing 'help.'"
                return self.get_command()
        #command is not defined
        else:
            #print error and start over
            print "Error: Command not defined"
            return self.get_command()
     
     
    def cli_handled(self):
        return self.commands.get(self.command)[0]   
     
     
    #def: valid_command
    #purpose: determine if the user input is valid (aka - not empty)
    def valid_command(self, command):
        (first_token, seperator, second_token) = command.partition(" ")
        #determine if the command (first_token) is valid and  then if the
        #parameters are valid
        if( first_token != ''):
            return True 
        else:
            return False 
    
    #def: command_defined
    #purpose: determine of a command is in the list of commands
    def command_defined(self):
        command = self.commands.get(self.command, None)
        if( command != None ):
            return True
        else:
            return False 
    
    
    
    def validate_parameter(self):
        #if it requires a param, check that there is one
        if(self.commands.get(self.command)[1] != ''):
            if( self.params != ''):
                if( self.commands.get(self.command)[3] == int ):
                    try:
                        self.params = int(self.params)
                    except:
                        return False
                    return True
                elif( self.commands.get(self.command)[3] == str ):
                    try:
                        self.params = str( self.params )
                    except:
                        return False
                    return True
            else:
                return False
        #this should 'theoretically' NEVER be reached, but for safety...
        else:
            return True


    #EXECUTE (or related) FUNCTION(S) FROM THIS POINT ON

    #def: execute
    #purpose: execute a command that is non-turn based.
    def execute(self):
        #allow these commands regardless
        creature = self.level.get_current_room().creature
        if( self.command == "help" ):
            self.execute_help()
        elif( self.command == "vhelp" ):
            self.execute_vhelp()
        elif( self.command == "map" ):
            self.execute_map()
        elif( self.command == "look-around" ):
            self.execute_lookaround()
        elif( self.command == "study" ):
            self.execute_study()
        elif( self.command[0:9] == "inventory" ):
            self.execute_inventory()
        elif( self.command[0:7] == "inspect" ):
            self.execute_inspect()
        elif( self.command == "switch-weapon" ):
            self.execute_switch_weapon()
        elif( self.command == "switch-armor" ):
            self.execute_switch_armor()
        elif( self.command == "status" ):
            self.execute_status()
        #if there are NO creatures in the room, then allow these
        #command    
        elif( self.level.get_current_room().creature == None ):
            if( self.command == "pickup" ):
                self.execute_pickup()
            elif( self.command[0:4] == "drop" ):
                self.execute_drop()
            elif( self.command == 'use-potion' ):
                self.execute_use_potion()
            elif( self.command == 'buy-attribute' ):
                self.execute_buy_attribute()

            #possibly generate mob since there is no creature in a room
            if( creature == None and self.level.mob_size > 0):
                if( random.randrange(100) > 80 ):
                    cf = Creature_Factory()
                    c = cf.generate()
                    self.level.get_current_room().creature = c
                    self.level.mob_size -= 1
                    print c.name + " entered the room!"

        #if there is a creature in the room, then allow these commands
        elif( self.level.get_current_room().creature != None ):
            if( self.command == "flee" ):
                self.execute_flee()
            elif( self.command == "attack" ):
                self.execute_attack()
            elif( self.command == "magic-attack" ):
                self.execute_magic_attack()
            elif(self.command == 'use-potion' ):
                self.execute_use_potion()

        #check if the creature or the player is dead
        if(creature != None):
            if( creature.hp <= 0 ):
                diff = creature.level - self.player.level
                xp = 0
                if diff >= 0:
                    xp = creature.calc_experience() * (diff+1)
                else:
                    tmp = (diff * -20) // 100
                    xp = int(creature.calc_experience() * tmp)

                self.player.grant_xp(xp)
                print "You gained %s XP for slaying the" % xp,
                print creature.name + "."
                print "You collected %s gold coins from the corpse." % creature.gold
                self.player.gold += creature.gold
                tf = Treasure()
                treasure = tf.generate(creature.level)
                for t in treasure:
                    self.level.get_current_room().item.append(t)
                for p in creature.all_equipment():
                    self.level.get_current_room().item.append(p)

                self.level.get_current_room().creature = None
        if(self.player.hp <= 0):
            print "Game Over! You died sucka!"
            sys.exit()

    

    def execute_buy_attribute(self):
        ap = self.player.ap
        suck = False
        if( self.params == "strength" ):
            s = self.player.strength
            cost = (s ** 2) / 2
            if( ap >= cost ):
                self.player.strength += 1
                print "Strength increased by one"
                self.player.ap -= cost
            else:
                suck = True
        elif( self.params == "agility" ):
            a = self.player.agility
            cost = (a ** 2) / 2
            if( ap >= cost ):
                self.player.agility += 1
                self.player.ap -= cost
                print "Agility increased by one"
            else:
                suck = True
        elif( self.params == "dexterity" ):
            d = self.params.dexterity
            cost = (d ** 2) / 2
            if( ap >= cost ):
                self.player.dexterity += 1
                self.player.ap -= cost
                print "Dexterity increased by one"
            else:
                suck = True
        elif( self.params == "intelligence" ):
            i = self.player.intel
            cost = (i ** 2) / 2
            if( ap >= cost):
                self.player.intel += 1
                self.player.ap -= cost
                print "Intelligence increased by one"
            else:
                suck = True
        elif( self.params == "stamina" ):
            s = self.player.stamina
            cost = (s ** 2) / 2
            if( ap >= cost ):
                self.player.stamina += 1
                self.player.ap -= cost
                print "Stamina increased by one"
            else:
                suck = True
        else:
            print "You cannot buy an attribute that does not exist."

        if suck:
            print "You don't have enough AP, try again later."





    def execute_status(self):
        print "Status: %(n)s" % {'n': self.player.name}
        p = self.player
        out = 'HP: ' + str(p.hp) + '/' + str(p.max_hp) + "\n"
        out += 'Strength: ' + str(p.strength) + "\n"
        out += 'Agility: ' + str(p.agility) + "\n"
        out += 'Dexterity: ' + str(p.dexterity) + "\n"
        out += 'Intelligence: ' + str(p.intel) + "\n"
        out += 'Stamina: ' + str(p.stamina) + "\n"
        out += 'AP: ' + str(p.ap) + "\n"
        print out
        #assuming 80 console width
        bar_width = 74
        out = 'XP: |'
        completion = float(self.player.experience) / float(self.player.next_level)
        completion2 = int(round(float(74 * completion)))
        for i in range(completion2):
            out += '='
        for i in range(bar_width - completion2):
            out += ' '
        out += '|'
        print out
        print str( round(completion*100) ) + '%'
            



    
    
    def execute_map(self):
        #print header
        print "Level Map"
        print self.level




    def execute_switch_armor(self):
        if( self.params > len(self.player.armor) - 1 or self.params < 0 ):
            print "Armor does not exist, try again"
        elif( self.params == 0 ):
            print "Already eqquiped"
        else:
            #make sure they meet the weapon requirements
            p = self.player
            if( p.strength < p.armor[self.params].required_strength ):
                print "Do not have the required strength to equip armor. It didn't look good on anyways."
                return
            temp = self.player.armor[self.params]
            self.player.armor[self.params] = self.player.armor[0]
            self.player.armor[0] = temp
            print "Armor equipped"



    
    def execute_switch_weapon(self):
        if( self.params > len(self.player.weapon) - 1 or self.params < 0 ):
            print "Weapon does not exist, try again"
        elif( self.params == 0 ):
            print "Already equipped"
        else:
            p = self.player
            if( p.strength < p.weapon[self.params].required_strength or
                p.agility < p.weapon[self.params].required_agility):
                print "You do not have enough strength or agility to equip weapon. Get out of the computer chair once in a while, workout more."
                return
            if( isinstance(p.weapon[self.params], Wand_Weapon )):
                if( p.intel < p.weapon[self.params].required_intel ):
                    print "You do not have enough intelligence to use this weapon. Pick up a book or something."
                    return
            temp = self.player.weapon[self.params]
            self.player.weapon[self.params] = self.player.weapon[0]
            self.player.weapon[0] = temp
            print "Weapon equipped"



    
    def execute_use_potion(self):
        if( self.level.get_current_room().creature != None ):
            arena = Arena(self.player, self.level.get_current_room().creature)
            if( len(self.player.potion) - 1 >= self.params and self.params >= 0 ):
                arena.potion(self.params)
                self.player.potion.pop(self.params)

        else:
            #use the potion
            if( len(self.player.potion) - 1 >= self.params and self.params >= 0 ):
                self.player.potion[self.params].attack_post(self.player, None)
                self.player.potion.pop(self.params)



    def execute_magic_attack(self):
        arena = Arena(self.player, self.level.get_current_room().creature)
        if( len(self.player.spells) - 1 >= self.params and self.params >= 0 ):
            arena.magic_attack(self.params)
            self.player.spells.pop(self.params)




    def execute_attack(self):
        arena = Arena(self.player, self.level.get_current_room().creature)
        arena.attack()
    
    
    
    
    def execute_flee(self):
        #get random direction
        valid = False
        while( not valid ):
            direction = random.randrange(1, 5)
            if( direction == 1 ):
                if( self.level.has_north() ):
                    valid = True
            if( direction == 2 ):
                if( self.level.has_east() ):
                    valid = True
            if( direction == 3 ):
                if( self.level.has_south() ):
                    valid = True
            if( direction == 4 ):
                if( self.level.has_west() ):
                    valid = True
        #get randome type {1:weapon, 2:armor, 3:potion, 4:spell}
        drop_type = random.randrange(1, 5)
        if( drop_type == 1 ):
            if( len(self.player.weapon) > 1 ):
                drop_id = random.randrange(len(self.player.weapon))
                print "you dropped a weapon"
            else:
                drop_id = -1
        if( drop_type == 2 ):
            if( len(self.player.armor) > 1 ):
                drop_id = random.randrange(len(self.player.armor))
                print "you dropped your armor"
            else:
                drop_id = -1
        if( drop_type == 3 ):
            if( len(self.player.potion) > 0 ):
                drop_id = random.randrange(len(self.player.potion))
                print "you dropped a potion"
            else:
                drop_id = -1
        if( drop_type == 4 ):
            if( len(self.player.spells) > 0 ):
                drop_id = random.randrange(len(self.player.spells))
                print "you dropped a spell"
            else:
                drop_id = -1

        #get amount of gold to drop
        if( self.player.gold > 0 ):
            gold_ramge = round(self.player.gold * .1)
            if( gold_range > 0 ):
                gold_drop = random.randrange(1, gold_range + 1)
            else:
                gold_drop = 0
        else:
            gold_drop = 0


        #move to a random room
        {
            1: self.level.move_north,
            2: self.level.move_east,
            3: self.level.move_south,
            4: self.level.move_west,
        }[direction]()
        #drop something random
        if( drop_id != -1 ):
            self.level.get_current_room().item.append( {
                1: self.player.weapon,
                2: self.player.armor,
                3: self.player.potion,
                4: self.player.spells,
            }[drop_type].pop(drop_id))
        #decrement player's gold
        self.player.gold -= gold_drop



    def execute_inspect(self):
        try:
            if( self.command[8:] == "weapon" ):
                print self.player.weapon[self.params]
            if( self.command[8:] == "armor" ):
                print self.player.armor[self.params]
            if( self.command[8:] == "potion" ):
                print self.player.potion[self.params]
            if( self.command[8:] == "spell" ):
                print self.player.spells[self.params]
        except:
            print "Can't inspect " + self.command[8:] + " that does not exist"



    def execute_inventory(self):
        i = 0
        if( self.command[10:] == "weapon" ):
            for w in self.player.weapon:
                print "[%(id)i] %(d)s" % {'id': i, 'd': str(w)}
                i += 1
        if( self.command[10:] == "armor" ):
            for a in self.player.armor:
                print "[%(id)i] %(d)s" % {'id': i, 'd': str(a)}
                i += 1
        if( self.command[10:] == "potion" ):
            for p in self.player.potion:
                print "[%(id)i] %(d)s" % {'id': i, 'd': str(p)}
                i += 1
        if( self.command[10:] == "spell" ):
            for s in self.player.spells:
                print "[%(id)i] %(d)s" % {'id': i, 'd': str(s)}
                i += 1



    def execute_drop(self):
        try:
            if( self.command[5:] == 'weapon' ):
                item = self.player.weapon.pop(self.params)
            if( self.command[5:] == 'armor' ):
                item = self.player.armor.pop(self.params)
            if( self.command[5:] == 'potion' ):
                item = self.player.potion.pop(self.params)
            if( self.command[5:] == 'spell' ):
                item = self.player.spells.pop(self.params)

            self.level.get_current_room().item.append(item)

        except:
            print "Unable to drop item that is not in inventory"



    def execute_pickup(self):
        room = self.level.get_current_room()
        try:
            item = room.item[self.params]
            #get item type
            if( isinstance(item, Potion) ):
                self.player.potion.append(item)
                print "Potion added to inventory"
            elif( isinstance(item, Spell) ):
                self.player.spells.append(item)
                print "Spell added to inventory"
            elif( isinstance(item, Armor) ):
                self.player.armor.append(item)
                print "Armor added to inventory"
            elif( isinstance(item, Weapon) ):
                self.player.weapon.append(item)
                print "Weapon added to inventory"
            room.item.pop(self.params)
        except:
            print 'Item with id of ' + str(self.params) + ' does not exist in the room'



    def execute_study(self):
        if( self.params == -1 ):
            try:
                print self.level.get_current_room().creature
            except:
                print "Sorry, no information"
        try:
            print self.level.get_current_room().item[self.params]
        except:
            print ''
    

    def execute_lookaround(self):
        room = self.level.get_current_room()
        items = room.item
        i = 0
        for item in items:
            print "[%(id)i] - %(descrip)s" % {'id':i, 'descrip':item.name}
            i += 1
        if( room.creature != None ):
            print "[%(id)i] - %(descrip)s" % {'id':-1, 'descrip':room.creature.name}

       
    
    
    
    def execute_help(self):
        for tag, (turn_based, params, description, junk) in self.commands.items():
            print tag
        print ""
    
    
    def execute_vhelp(self):
        for tag, (turn_based, params, description, junk) in self.commands.items():
            if( self.params == '*' or self.params == tag ):
                if( params == '' ):
                    tag_param = ''
                else:
                    tag_param = '  [%s]' % params
                print tag + tag_param
                print "\t" + description
                print ""
    
    
    
    
