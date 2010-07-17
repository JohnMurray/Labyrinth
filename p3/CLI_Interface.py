#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: CLI_Interface.py

import random
import Arena
import sys

from Arena import Arena

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
            "move-north": (False, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "move-east": (False, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "move-south": (False, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "move-west": (False, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "flee": (True, '', 'Similar to move-* command. Allows you to flee a room where monster is, but the room is random and you may drop weapons, items, or gold when fleeing.', None),
            "attack": (True, '', 'Attack an opponent when in battle with primary weapon.', None),
            "magic-attack": (True, 'id', 'Attack an opponent with a spell. Must give id.(Use the inventory-spell to get spell id).', int),
            "look-around": (True, '', 'Look at all the items currently in the room. Shows item name and id.', None),
            "study": (True, 'id', 'View an item in the room in great detail. A.K.A - View the item\'s stats and/or description, etc. Must give item id. (use look-around to get item id)', int),
            "pickup": (True, '', 'Pick up and item in the room. Must give item id. (use look-around to get item id)', None),
            "inventory-weapon": (True, '', 'List your current weapon inventory. View each weapon\'s name and id.', None),
            "inventory-armor": (True, '', 'List your current armor inventory. View each armor\'s name and id.', None),
            "inventory-potion": (True, '', 'List your current potion inventory. View each potion\'s name and id.', None),
            "inventory-spell": (True, '', 'List your current spell inventory. View each spell\'s name and id.', None),
            "inspect-weapon": (True, 'id', 'View an weapon in the inventory in great detail. A.K.A - View the weapon\'s stats and/or description, etc. Must give id. (use inventory-weapon to get item id)', int),
            "inspect-armor": (True, 'id', 'View an armor in the inventory in great detail. A.K.A - View the armor\'s stats and/or description, etc. Must give id. (use inventory-armor to get item id)', int),
            "inspect-potion": (True, 'id', 'View an potion in the inventory in great detail. A.K.A - View the potion\'s stats and/or description, etc. Must give id. (use inventory-potion to get item id)', int),
            "inspect-spell": (True, 'id', 'View an spell in the inventory in great detail. A.K.A - View the spell\'s stats and/or description, etc. Must give id. (use inventory-spell to get item id)', int),
            "drop-weapon": (True, 'id', 'Drop a weapon in the inventory. Must give weapon id. (use inventory-weapon to get weapon id)', int),
            "drop-armor": (True, 'id', 'Drop an armor in the inventory. Must give armor id. (use inventory-armor to get armor id)', int),
            "drop-potion": (True, 'id', 'Drop a potion in the inventory. Must give potion id. (use inventory-potion to get potion id)', int),
            "drop-spell": (True, 'id', 'Drop an spell in the inventory. Must give spell id. (use inventory-spell to get spell id)', int),
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
        return self.commands.get(command)[0]   
     
     
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
        if( self.command == "help"):
            self.execute_help()
        elif( self.command == "lookaround"):
            self.execute_lookaround()
        elif( self.command == "study"):
            self.execute_study()
        elif( self.command[0:9] == "inventory" ):
            self.execute_inventory()
        elif( self.command[0:7] == "inspect" ):
            self.execute_inspect()
        #if there are NO creatures in the room, then allow these
        #command    
        if( self.level.get_current_room().creature == None ):
            if( self.command == "pickup" ):
                self.execute_pickup()
            if( self.command[0:4] == "drop" ):
                self.execute_drop()
        #if there is a creature in the room, then allow these commands
        if( self.level.get_current_room().creature != None ):
            if( self.command == "flee" ):
                self.execute_flee()
            if( self.command == "attack" ):
                self.execute_attack()
            if( self.command == "magic-attack" ):
                self.execute_magic_attack()
            if( self.command == "use-potion" ):
                self.execute_potion()

        #check if the creature or the player is dead
        creature = self.level.get_current_room().creature
        if(creature != None):
            if( creature.hp <= 0 ):
                self.level.get_current_room().creature = None
        if(self.player.hp <= 0):
            print "Game Over! You died sucka!"
            sys.exit()
    

    
    
    def execute_use_potion(self):
        arena = Arena(self.player, self.level.get_current_room().creature)
        if( len(self.player.potion) - 1 >= self.params and self.params >= 0 ):
            arena.potion(self.params)



    def execute_magic_attack(self):
        arena = Arena(self.player, self.level.get_current_room().creature)
        if( len(self.player.spells) - 1 >= self.params and self.params >= 0 ):
            arena.magic_attack(self.params)




    def execute_attack(self):
        arena = Arena(self.player, self.level.get_current_room().creature)
        arena.attack()
    
    
    
    
    def execute_flee(self):
        #get random direction
        direction = random.randrange(1, 5)
        #get randome type {1:weapon, 2:armor, 3:potion, 4:spell}
        drop_type = random.randrange(1, 5)
        if( drop_type == 1 ):
            if( len(self.player.weapon) > 1 ):
                drop_id = random.randrange(len(self.player.weapon))
            else:
                drop_id = -1
        if( drop_type == 2 ):
            if( len(self.player.armor) > 0 ):
                drop_id = random.randrange(len(self.player.armor))
            else:
                drop_id = -1
        if( drop_type == 3 ):
            if( len(self.player.potion) > 0 ):
                drop_id = random.randrange(len(self.player.potion))
            else:
                drop_id = -1
        if( drop_type == 4 ):
            if( len(self.player.spell) > 0 ):
                drop_id = random.randrange(len(self.player.spell))
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
        }.[direction]()
        #drop something random
        if( drop_id != -1 ):
            {
                1: self.player.weapon,
                2: self.player.armor,
                3: self.player.potion,
                4: self.player.spell
            }[drop_type].pop(drop_id)
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
                print self.player.spell[self.params]
        except:
            print "Can't inspect " + self.command[8:] + " that does not exist"



    def execute_inventory(self):
        i = 0
        if( self.commands[10:] == "weapon" ):
            for w in self.player.weapon:
                print "[%(id)i] %(d)s" % {'id': i, 'd': w.short_name()}
                i += 1
        if( self.commands[10:] == "armor" ):
            for a in self.player.armor:
                print "[%(id)i] %(d)s" % {'id': i, 'd': a.short_name()}
                i += 1
        if( self.commands[10:] == "potion" ):
            for p in self.player.potion:
                print "[%(id)i] %(d)s" % {'id': i, 'd': p.short_name()}
                i += 1
        if( self.commands[10:] == "spell" ):
            for s in self.player.armor:
                print "[%(id)i] %(d)s" % {'id': i, 'd': s.short_name()}
                i += 1



    def execute_drop(self):
        try:
            if( self.commands[5:] == 'weapon' ):
                item = self.player.weapon.pop(self.params)
            if( self.commands[5:] == 'armor' ):
                item = self.player.armor.pop(self.params)
            if( self.commands[5:] == 'potion' ):
                item = self.player.potion.pop(self.params)
            if( self.commands[5:] == 'spell' ):
                item = self.player.spell.pop(self.params)

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
            if( isinstance(item, Spell) ):
                self.player.spell.append(item)
                print "Spell added to inventory"
            if( isinstance(item, Armor) ):
                self.player.armor.append(item)
                print "Armor added to inventory"
            if( isinstance(item, Weapon) ):
                self.player.weapon.append(item)
            room.item.pop(self.params)
        except:
            print 'Item with id of ' + self.params + 'does not exist in the room'

    def execute_study(self):
        try:
            print self.level.get_current_room().item[self.params]
        except:
            print ''
    

    def execute_lookaround(self):
        room = self.level.get_current_room()
        items = room.item
        i = 0
        for item in items:
            print "[%(id)i] - %(descrip)s" % {'id':i, 'descrip':item.short_name()}
       
    
    
    def execute_help(self):
        for tag, (turn_based, params, description, junk) in self.commands.items():
            print tag + "[" + params + "]"
            print "\t" + description
            print "\tUses Turn: " + str(turn_based)
    
    
    
    
