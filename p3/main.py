#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: main.py

#not sure if we need to really have a class, or just a procedural
#launching of the game, class here may just be overkill

#import statements
import Level
from Level import Level


#define main's global variables
level = None
game_name = "adventure game"


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










#start the game!! WOO HOO!!
print_initial_instructions()
settings = get_user_settings()

