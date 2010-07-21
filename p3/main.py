#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: main.py

#not sure if we need to really have a class, or just a procedural
#launching of the game, class here may just be overkill

#import statements
from Level import *
from Player import *
from CLI_Interface import *
from Weapon_Module import *
from Item_Module import *
from Armor import *
from Armor_Factory import *
from Weapon_Factory import *
from Item_Factory import *

#define main's global variables
level = None
game_name = "adventure game"
character_name = ""
items = Item_Factory()
wf = Weapon_Factory()
af = Armor_Factory()

def print_initial_instructions():
    
    global game_name
    
    game_instructions = "\n\tThe point of " + game_name + " is to defeat all the"
    game_instructions += "\n\tcreatures in the level and collect as much gold as"
    game_instructions += "\n\tpossible. You can move from room to room to defeat"
    game_instructions += "\n\tcreatures and collect gold, items, weapons, and new"
    game_instructions += "\n\tarmor. If you die (loose all of your hp) you must"
    game_instructions += "\n\tstart over from the beginning. You may type 'help'"
    game_instructions += "\n\tat any point in the game to get a list of game "
    game_instructions += "\n\tcommands. Type 'options' to get a list of commands"
    game_instructions += "\n\tthat pertain to your current move's options."
    
    print "Welcome to", game_name, "!"
    print "Instructions"
    print game_instructions


def get_user_settings():
    valid_input = False
    while( not valid_input ):
        print "What level size would you like to play on?"
        print "[1] Extra-Large (100 rooms)"
        print "[2] Large (64 rooms)"
        print "[3] Medium (36 rooms)"
        print "[4] Medium-Small (25 rooms)"
        print "[5] Small (16 rooms)"
        print "[6] Extra-Small (9 rooms)"
        print "[7] Tiny (4 rooms)"
        level_size = raw_input(": ")
        try:
            level_size = int(level_size)
            if( type(level_size) == int and level_size > 0 and level_size < 8):
                valid_input = True
            else:
                print "Not valid input. Try again."
        except:
            print "Not a number, try again"
    valid_input = False
    while( not valid_input ):
        print ""
        print "What would you like your character name to be?"
        character_name = raw_input(": ")
        if( len(character_name) > 0 ):
            valid_input = True
        else:
            print "Not valid input. Try again."
    valid_input = False
    while( not valid_input ):
        print ""
        print "What difficulty would you like to play at?"
        print "[1] Extreme (25% hp)"
        print "[2] Hard (50% hp)"
        print "[3] Medium (75% hp)"
        print "[4] Easy (100% hp)"
        difficulty = raw_input(": ")
        try:
            difficulty = int(difficulty)
            if( type(difficulty) == int and difficulty > 0 and difficulty < 5):
                valid_input = True
            else:
                print "Not valid input. Try again."
        except:
            print "Not a number, try again"

    return {
        "level_size":level_size,
        "character_name":character_name,
        "difficulty":difficulty
    }




def victorious(level):
    return level.defeated_all_creatures()

def print_class_information():
    print "Warrior:"
    print "     Warriors excel at melee combat, if you don't know what",
    print "excel means this is the class for you"
    print "     Warriors receive a + 1 to Strength and Stamina"
    print "     Warriors receive a - 1 to Intelligence and Agility"
    print ""
    print "Rogue:"
    print "     Rogues rely on wit and fleetness of foot to survive",
    print "the perils of the labyrinth"
    print "     Rogues receive a + 1 to Agility and Dexterity"
    print "     Rogues receive a - 1 to Strength and Stamina"
    print ""
    print "Mage:"
    print "     Mages are ineffective fighters, but they have access",
    print "to powerful arts of mystic origin."
    print "     Should they live long enough to use them..."
    print "     Mages receive a + 2 to Intelligence"
    print "     Mages receive a - 1 to Strength and Dexterity"

def calc_starting_hp(stamina):
    return 100 + random.randint(stamina^2, stamina*10)   

def equip_potion(player):
    player.potion = list()
    player.add_potion(items.generate_potion_healing(1))
    player.add_potion(items.generate_potion_healing(1))
    return player

def equip_weapon(player):
    player.weapon = list()
    wpn = wf.generate_by_quality(0)
    while wpn.required_strength > player.strength or wpn.required_agility > player.agility:
        wpn = wf.generate_by_quality(0)
    player.add_weapon(wpn)
    return player

def equip_armor(player):
    player.armor = list()
    armor = af.generate_by_quality(0)
    while armor.required_strength > player.strength:
        armor = af.generate_by_quality(0)
    player.add_armor(armor)
    return player

def standard_equipment(player):
    player = equip_potion(player)
    player = equip_weapon(player)
    player = equip_armor(player)
    return player

def equip_mage(player):
    player = standard_equipment(player)
    player.add_spell(items.generate_spell_attack(2))
    player.add_spell(items.generate_spell_attack(2))
    player.add_spell(items.generate_spell(2))
    player.add_spell(items.generate_spell(2))
    player.add_spell(items.generate_spell(1))
    player.add_spell(items.generate_spell(1))
    player.add_spell(items.generate_spell(1))
    player.add_spell(items.generate_spell(1))
    wpn = wf.generate_by_type(4)
    while wpn.required_intel > player.intel:
        wpn = wf.generate_by_type(4, random.randint(0,1))
    player.add_weapon(wpn)
    return player

def equip_rogue(player):
    player = standard_equipment(player)
    wpn = wf.generate_by_type(1)
    while wpn.required_agility > player.agility or wpn.required_strength > player.strength:
        wpn = wf.generate_by_type(1,random.randint(0,1))
    player.add_weapon(wpn)
    player.add_spell(items.generate_spell(1))
    player.add_spell(items.generate_spell(1))
    player.add_potion(items.generate_potion(1))
    player.add_potion(items.generate_potion(0))
    return player

def equip_warrior(player):
    player = standard_equipment(player)
    wpn = wf.generate_by_quality(1)
    while wpn.required_agility > player.agility or wpn.required_strength > player.strength:
        wpn = wf.generate_by_quality(random.randint(0,1))
    armor = af.generate_by_quality(1)
    while armor.required_strength > player.strength:
        armor = af.generate_by_quality(random.randint(0,1))
    player.add_weapon(wpn)
    player.add_armor(armor)
    player.add_potion(items.generate_potion_healing(1))
    return player

def create_character():
    valid_input = False
    while( not valid_input ):
        print " " 
        print "Select a class:"
        print "[1] Warrior"
        print "[2] Rogue"
        print "[3] Mage"
        print "{i} More information"
        #Shamelessly pasted code, the variable's name is stupid
        isint = True
        difficulty = raw_input(": ")
        try:
            int_input = int(difficulty)
        except:
            isint = False

        if isint and int_input > 0 and int_input < 4:
            valid_input = True
        elif difficulty == "i" or difficulty == "I":
            print_class_information()
        else:
            print "Not valid input. Try again."

    char = int_input 
    valid_input = False
    cf = Creature_Factory()
    player = Adventurer(character_name,0)
    roll = True 
    while not valid_input:
        print " " 
        print character_name
        if roll:
            player = cf.generate_player_stats(player)
            player.max_hp = calc_starting_hp(player.stamina)
            if char == 1:
                player.strength += 1
                player.stamina += 1
                if player.intel > 1:
                    player.intel -= 1
                if player.agility > 1:
                    player.agility -= 1
            elif char == 2:
                player.agility += 1
                player.dexterity += 1
                if player.strength > 1:
                    player.strength -= 1
                if player.stamina > 1:
                    player.stamina -= 1
            else:
                player.intel += 2
                if player.strength > 1:
                    player.strength -= 1
                if player.dexterity > 1:
                    player.dexterity -= 1

        print "Strength: %s" % player.strength
        print "Stamina: %s" % player.stamina
        print "Agility: %s" % player.agility
        print "Dexterity: %s" % player.dexterity
        print "Intelligence: %s" % player.intel
        player.hp = player.max_hp
        print "Starting HP: %s" % player.max_hp
        print "Would you like to keep this character?"
        print "[Y]es to keep, or [N]o to roll again"
        response = raw_input(": ")
        roll = False
        try:
            if response == "Y" or response == "y":
                valid_input = True
            elif response == "N" or response == "n":
                print ""
                print "Rolling again..."
                roll = True
        except:
            print "Really? There's only two options."
        
    if char == 1:
        player = equip_warrior(player)
    elif char == 2:
        player = equip_rogue(player)
    else:
        player = equip_mage(player)

    return player

##---------------------------------------------------------
## start the game!! WOO HOO!!
##---------------------------------------------------------

#print instructions
print_initial_instructions()
#get user-settings
settings = get_user_settings()

#intialize the Level and Player
dimension = {
    1: 10,
    2: 8,
    3: 6,
    4: 5,
    5: 4,
    6: 3,
    7: 2,
}[settings['level_size']]
level = Level(dimension)

player = create_character()

#initialize the CLI object
cli = CLI(player, level)


#start the game loop
while( not victorious(level) ):
    #get the command
    cur_cmd = cli.get_command()
    #check if there is a creature in the room
    if( level.get_current_room().creature != None ):
        print "You cannot move when a creature is in the room"
    else:
        {
            'north': level.move_north,
            'east': level.move_east,
            'south': level.move_south,
            'west': level.move_west
        }[cur_cmd[5:]]()
else:
    print "You've won the game!"
    print ""
    print "Your final stats:"
    print "\tHP:   " + str(player.hp)
    print "\tGold: " + str(player.gold)


