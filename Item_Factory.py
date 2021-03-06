#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Item_Factory.py


from Item_Module import *
import random
import Config

class Item_Factory:

    def __init__(self):
        self.spell = Config.item['spell']
        self.potion = Config.item['potion']


    ##---------------------------------------------------------
    ## Generic Generate (generates abundant to medium-rare
    ## items)
    ##---------------------------------------------------------

    def generate(self, rarity = -1):
        if( rarity == -1 ):
            rarity = random.randrange(1, 4) #random range from 1 to 3 inclusive
        elif( rarity > 3 ):
            rarity = 3
        elif( rarity < 1 ):
            rarity = 1
        item_type = random.randrange(100)
        #generate a spell
        if( item_type < 50 ):
            return self.generate_spell(rarity)
        #generate a potion
        else:
            return self.generate_potion(rarity)


    #rarity = {1: weak, 2: medium, 3: rare}
    def generate_potion(self, rarity = 1):
        spell_type = random.randrange(100)
        if( spell_type < 20 ):
            #create healing potion
            return self.generate_potion_healing(rarity)
        elif( spell_type < 40 ):
            #create defense potion
            return self.generate_potion_defense(rarity)
        elif( spell_type < 60 ):
            #create offense potion
            return self.generate_potion_offense(rarity)
        elif( spell_type < 80 ):
            #create magic deffense potion
            return self.generate_potion_magic_defense(rarity)
        else:
            #create magic offense potion
            return self.generate_potion_magic_offense(rarity)


    def generate_potion_magic_offense(self, rarity):
        nd = self.get_random_potion_magic_offense_description(rarity)
        return (
            Magic_Offense_Potion(nd[0], nd[1], random.randrange(self.potion['magic_offense']['common'][0],self.potion['magic_offense']['common'][1]), 
                random.randrange(self.potion['magic_offense']['common'][2],self.potion['magic_offense']['common'][3]) ),
            Magic_Offense_Potion(nd[0], nd[1], random.randrange(self.potion['magic_offense']['normal'][0],self.potion['magic_offense']['normal'][1]), 
                random.randrange(self.potion['magic_offense']['normal'][2],self.potion['magic_offense']['normal'][3]) ),
            Magic_Offense_Potion(nd[0], nd[1], random.randrange(self.potion['magic_offense']['rare'][0],self.potion['magic_offense']['rare'][1]), 
                random.randrange(self.potion['magic_offense']['rare'][2],self.potion['magic_offense']['rare'][3]) ),
        )[rarity - 1]



    def generate_potion_magic_defense(self, rarity):
        nd = self.get_random_potion_magic_defense_description(rarity)
        return (
            Magic_Offense_Potion(nd[0], nd[1], random.randrange(self.potion['magic_defense']['common'][0], self.potion['magic_defense']['common'][1]), 
                random.randrange(self.potion['magic_defense']['common'][2], self.potion['magic_defense']['common'][3]) ),
            Magic_Offense_Potion(nd[0], nd[1], random.randrange(self.potion['magic_defense']['normal'][0],self.potion['magic_defense']['normal'][1]), 
                random.randrange(self.potion['magic_defense']['normal'][2],self.potion['magic_defense']['normal'][3]) ),
            Magic_Offense_Potion(nd[0], nd[1], random.randrange(self.potion['magic_defense']['rare'][0],self.potion['magic_defense']['rare'][1]), 
                random.randrange(self.potion['magic_defense']['rare'][2],self.potion['magic_defense']['rare'][3]) ),
        )[rarity - 1]

    
    def generate_potion_offense(self, rarity):
        nd = self.get_random_potion_offense_description(rarity)
        return (
            Offense_Potion(nd[0], nd[1], random.randrange(self.potion['magic_offense']['common'][0], self.potion['magic_offense']['common'][1]), 
                random.randrange(self.potion['magic_offense']['common'][2], self.potion['magic_offense']['common'][3]) ),
            Offense_Potion(nd[0], nd[1], random.randrange(self.potion['magic_offense']['rare'][0], self.potion['magic_offense']['rare'][1]), 
                random.randrange(self.potion['magic_offense']['rare'][2], self.potion['magic_offense']['rare'][3]) ),
            Offense_Potion(nd[0], nd[1], random.randrange(self.potion['magic_offense']['rare'][0], self.potion['magic_offense']['rare'][1]), 
                random.randrange(self.potion['magic_offense']['rare'][2], self.potion['magic_offense']['rare'][3]) ),
        )[rarity - 1]
        


    def generate_potion_healing(self, rarity):
        if( rarity == 1 ):
            #weak potion
            nd = self.get_random_potion_healing_description_light()
            return Healing_Potion(nd[0], nd[1], self.potion['healing']['common'][0], self.potion['healing']['common'][1])
        elif( rarity == 2):
            #medium potion
            nd = self.get_random_potion_healing_description_medium()
            return Healing_Potion(nd[0], nd[1], self.potion['healing']['normal'][0], self.potion['healing']['normal'][1])
        else:
            #rare potion
            nd = self.get_random_potion_healing_description_heavy()
            return Healing_Potion(nd[0], nd[1], self.potion['healing']['rare'][0], self.potion['healing']['rare'][1])


    def generate_potion_defense(self, rarity):
        nd = self.get_random_potion_defense_description(rarity)
        if( rarity == 1 ):
            #weak potion
            return Defense_Potion(nd[0], nd[1], random.randrange(self.potion['defense']['common'][0], self.potion['defense']['common'][1]), 
                random.randrange(self.potion['defense']['common'][2], self.potion['defense']['common'][3])) 
        if( rarity == 2 ):
            #medium potion
            return Defense_Potion(nd[0], nd[1], random.randrange(self.potion['defense']['normal'][0], self.potion['defense']['normal'][1]), 
                random.randrange(self.potion['defense']['normal'][2],self.potion['defense']['normal'][3]))
        else:
            #rare potion
            return Defense_Potion(nd[0], nd[1], random.randrange(self.potion['defense']['rare'][0],self.potion['defense']['rare'][1]), 
                random.randrange(self.potion['defense']['rare'][2],self.potion['defense']['rare'][3]))
        

    #rarity = {1: weak, 2: medium, 3: rare}
    def generate_spell(self, rarity = 1):
        #get a random sell type 
        spell_type = random.randrange(100)
        if( spell_type < 33 ):
            #create a attack spell
            return self.generate_spell_attack(rarity)
        elif( spell_type < 66 ):
            #create a defense spell
            return self.generate_spell_defense(rarity)
        else:
            #create a stun spell
            return self.generate_spell_stun(rarity)
            
    def generate_spell_stun(self, rarity):
        nd = self.get_random_spell_stun_description(rarity)
        return (
            Stun_Spell(nd[0], nd[1], random.randrange(self.spell['stun']['common'][0], self.spell['stun']['common'][1]), 
                random.randrange(self.spell['stun']['common'][2], self.spell['stun']['common'][3])),
            Stun_Spell(nd[0], nd[1], random.randrange(self.spell['stun']['normal'][0],self.spell['stun']['normal'][1]), 
                random.randrange(self.spell['stun']['normal'][2],self.spell['stun']['normal'][3])),
            Stun_Spell(nd[0], nd[1], random.randrange(self.spell['stun']['rare'][0],self.spell['stun']['rare'][1]), 
                random.randrange(self.spell['stun']['rare'][2],self.spell['stun']['rare'][3])),
        )[rarity - 1]
    def generate_spell_defense(self, rarity):
        nd = self.get_random_spell_defense_description(rarity)
        return (
            Defense_Spell(nd[0], nd[1], random.randrange(self.spell['defense']['common'][0], self.spell['defense']['common'][1]), 
                random.randrange(self.spell['defense']['common'][2], self.spell['defense']['common'][3]), 
                random.randrange(self.spell['defense']['common'][4], self.spell['defense']['common'][5])),
            Defense_Spell(nd[0], nd[1], random.randrange(self.spell['defense']['normal'][0],self.spell['defense']['normal'][1]), 
                random.randrange(self.spell['defense']['normal'][2],self.spell['defense']['normal'][3]), 
                random.randrange(self.spell['defense']['normal'][4],self.spell['defense']['normal'][5])),
            Defense_Spell(nd[0], nd[1], random.randrange(self.spell['defense']['rare'][0],self.spell['defense']['rare'][1]), 
                random.randrange(self.spell['defense']['rare'][2],self.spell['defense']['rare'][3]), 
                random.randrange(self.spell['defense']['rare'][4],self.spell['defense']['rare'][5])),
        )[rarity - 1]
        
    def generate_spell_attack(self, rarity):
        nd = self.get_random_spell_attack_description(rarity)
        return (
            Attack_Spell(nd[0], nd[1], random.randrange(self.spell['attack']['common'][0], self.spell['attack']['common'][1]), 
                random.randrange(self.spell['attack']['common'][2], self.spell['attack']['common'][3]), 
                random.randrange(self.spell['attack']['common'][4],self.spell['attack']['common'][5])),
            Attack_Spell(nd[0], nd[1], random.randrange(self.spell['attack']['normal'][0],self.spell['attack']['normal'][1]), 
                random.randrange(self.spell['attack']['normal'][2],self.spell['attack']['normal'][3]), 
                random.randrange(self.spell['attack']['normal'][4],self.spell['attack']['normal'][5])),
            Attack_Spell(nd[0], nd[1], random.randrange(self.spell['attack']['rare'][0],self.spell['attack']['rare'][1]), 
                random.randrange(self.spell['attack']['rare'][2],self.spell['attack']['rare'][3]), 
                random.randrange(self.spell['attack']['rare'][4],self.spell['attack']['rare'][5])),
        )[rarity - 1]


    ##---------------------------------------------------------
    ## Particular Generate (generates item of specified rarity)
    ##---------------------------------------------------------

    def generate_rare(self):
        return self.generate(3)
    
    def generate_normal(self):
        return self.generate(2)

    def generate_common(self):
        return self.generate(1)
        

    ##---------------------------------------------------------
    ## Description Generators
    ##---------------------------------------------------------
    
    #spells
    def get_random_spell_stun_description(self, rarity):
        ss = (
            ('Tazer', 'Stuns an player for one or more turns.'),
            ('Stun-Gun', 'Stuns a player for one or more turns.'),
            ('Super Tazer', 'Stuns a player for one or more turns.'),
        )
        return ss[rarity - 1]

    def get_random_spell_attack_description(self, rarity):
        sa = (
            ('Beginner Attack Spell', 'A beginner magical attack spell.'),
            ('Sage\' Wrath', 'An intermediate magical attack spell.'),
            ('Magical Beat Down', 'An advanced magical attack spell.'),
        )
        return sa[rarity - 1]

    def get_random_spell_defense_description(self, rarity):
        sd = (
            ('Magical Shield', 'Beginner magical defensive spell.'),
            ('Magical Armor', 'Intermediate magical defensive spell.'),
            ('Magical Fortress', 'Advanced magical defenseive spell.'),
        )
        return sd[rarity - 1]

    #potions
    def get_random_potion_healing_description_light(self):
        ph = (
            ('Light Health Potion', 'Light healing potion. (20 - 30 HP\'s)'),
            ('Light Elixer', 'Light healing potion. (20 - 30 HP\'s)'),
        )
        return ph[random.randrange(len(ph))]
    
    def get_random_potion_healing_description_medium(self):
        ph = (
            ('Medium Health Potion', 'Medium healing potion. (80 - 100 HP\'s)'),
            ('Medium Elixer', 'Medium healing potion. (80 - 100 HP\'s)'),
        )
        return ph[random.randrange(len(ph))]
    
    def get_random_potion_healing_description_heavy(self):
        ph = (
            ('Heavy Health Potion', 'Heavy healing potion. (160 - 200 HP\'s)'),
            ('Heavy Elixer', 'Heavy healing potion. (160 - 200 HP\'s)'),
        )
        return ph[random.randrange(len(ph))]
    
    def get_random_potion_defense_description(self, rarity = 1):
        pd = (
            ('Light Defense Potion', 'A light defense potion. Increases defense 1/2 points for 1/2 turns.'),
            ('Medium Defense Potion', 'A medium defense potion. Increases defense 3/4 points for 1/4 turns.'),
            ('Heavy Defense Potion', 'A heavy defense potion. Increases defense 3/6 points for 3/6 turns.'),
        )
        return pd[rarity - 1]

    def get_random_potion_offense_description(self, rarity):
        po = (
            ('Light Offense Potion.', 'A light offensive potion. Increases offense 2/4 for 1/2 turns.'),
            ('Medium Offense Potion', 'A medium offensive potion. Increases offense 3/6 for 1/4 turns.'),
            ('Potion of Beast Mode', 'A heavy offensive potion. Increases offense 5/10 for 3/6 turns.'),
        )
        return po[rarity - 1]

    def get_random_potion_magic_defense_description(self, rarity):
        pmd = (
            ('Light Magic Defense Potion', 'A light magical defense potion. Increases magical defense 1/2 for 1/2 turns.'),
            ('Mediurm Magic Defense Potion', 'A medium magical defense potion. Increases magical defense 2/4 for 3/4 turns.'),
            ('Heavy Magic Defense Potion', 'A heavy magical defense potion. Increases magical defense 3/6 for 4/5 turns.'),
        )
        return pmd[rarity - 1]

    def get_random_potion_magic_offense_description(self, rarity):
        pmo = (
            ('Ligth Magic Offense Potion', 'A light magical offense potion. Increases magical offense 1/2 for 1/2 turns.'),
            ('Medium Magic Offense Potion', 'A medium magical offense potion. Increases magical offense 3/5 for 1/4 turns.'),
            ('Heavy Magic Offense Potion', 'A heavy magical offense potion. Increases magical offense 4/7 for 3/6 turns.'),
        )
        return pmo[rarity - 1]



