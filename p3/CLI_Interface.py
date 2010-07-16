#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: CLI_Interface.py

#class: CLI
#purpose: A Command Line Interface class that handles the parsing of user
#         input and validation of input, the execution of non-turn based
#         commands, and returns the values of turn-based commands.
class CLI:
    def __init__(self, player, room):
        
        self.player = player
        self.room = room
        
        #lists commands with a tuple that defines
        #(turn-based, options(name), description(for help), param_type)
        self.commands = {
            "help" : (False, '', 'Shows the help dialog all available commands (not much un-similar to this page)turn/move.', None),
            "move-north": (True, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "move-east": (True, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "move-south": (True, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "move-west": (True, '', 'Moves through the level. Not allowed when you enter a room with a creature (an alive one).', None),
            "flee": (True, '', 'Similar to move-* command. Allows you to flee a room where monster is, but the room is random and you may drop weapons, items, or gold when fleeing.', None),
            "attack": (True, '', '', None),
            "magic-attack": (True, 'id', '', int),
            "look-around": (False, '', 'Look at all the items currently in the room. Shows item name and id.', None),
            "study": (False, 'id', 'View an item in the room in great detail. A.K.A - View the item\'s stats and/or description, etc. Must give item id. (use look-around to get item id)', int),
            "pickup": (False, '', 'Pick up and item in the room. Must give item id. (use look-around to get item id)', None),
            "inventory-weapon": (False, '', 'List your current weapon inventory. View each weapon\'s name and id.', None),
            "inventory-armor": (False, '', 'List your current armor inventory. View each armor\'s name and id.', None),
            "inventory-potion": (False, '', 'List your current potion inventory. View each potion\'s name and id.', None),
            "inventory-spell": (False, '', 'List your current spell inventory. View each spell\'s name and id.', None),
            "inspect-weapon": (False, 'id', 'View an weapon in the inventory in great detail. A.K.A - View the weapon\'s stats and/or description, etc. Must give id. (use inventory-weapon to get item id)', int),
            "inspect-armor": (False, 'id', 'View an armor in the inventory in great detail. A.K.A - View the armor\'s stats and/or description, etc. Must give id. (use inventory-armor to get item id)', int),
            "inspect-potion": (False, 'id', 'View an potion in the inventory in great detail. A.K.A - View the potion\'s stats and/or description, etc. Must give id. (use inventory-potion to get item id)', int),
            "inspect-spell": (False, 'id', 'View an spell in the inventory in great detail. A.K.A - View the spell\'s stats and/or description, etc. Must give id. (use inventory-spell to get item id)', int),
            "drop": (False, 'id', 'Drop an item in the inventory. Must give item id. (use inventory to get item id)', int)
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
                #check if the parameter requires a turn
                if( self.requires_turn(self.command) ):
                    return [self.command, self.params]
                else:
                    self.execute()
                    return self.get_command()
                
            #parameter validation has faild (aka - none given when one or more needed)
            else:
                print "Error: Parameter must be given and of correct type. Please refer to the help guide by typing 'help.'"
                return self.get_command()
        else:
            #print error and start over
            print "Error: Command not defined"
            return self.get_command()
     
     
    def requires_turn(self, command):
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
        if( self.command == "help"):
            self.execute_help()
    
    
    
    def execute_help(self):
        for tag, (turn_based, params, description, junk) in self.commands.items():
            print tag + "[" + params + "]"
            print "\t" + description
            print "\tUses Turn: " + str(turn_based)
    
    
    
    
