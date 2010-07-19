#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Item_Factory.py


from Item_Module import *


class Item_Factory:

    def __init__(self):
        self


    ##---------------------------------------------------------
    ## Generic Generate (generates abundant to medium-rare
    ## items)
    ##---------------------------------------------------------

    def generate(self):
        item_type = random.randrange(1, 101)
        #generate a spell
        if( item_type < 51 ):
            #get a random sell type
            spell_type = radom.randrange(1, 101)
            if( 
        #generate a potion
        else:
            #create a potion


    def generate_potion(self):
        

    def generate_spell(self):
        


    ##---------------------------------------------------------
    ## Rare Generate (generates rare items)
    ##---------------------------------------------------------

    def generate_rare(self):
        

    def generate_rare_potion(self):
        

    def generat_rare_spell(self):
        

    ##---------------------------------------------------------
    ## Description Generators
    ##---------------------------------------------------------
    
    #spells
    def get_random_spell_stun_description(self):
        ss = (
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        )
        return ss[random.randrange(len(ss))]

    def get_random_spell_attack_description(self):
        sa = (
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        )
        return sa[random.randrange(len(sa))]

    def get_random_spell_defense_description(self):
        sd = (
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        )
        return sd[random.randrange(len(sd))]

    #potions
    def get_random_potion_healing_desription(self):
        ph = (
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        )
        return ph[random.randrange(len(ph))]
    
    def get_random_potion_defense_description(self):
        pd = (
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        )
        return pd[random.randrange(len(pd))]

    def get_random_potion_offense_description(self):
        po = (
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        )
        return po[random.randrange(len(po))]

    def get_random_potion_magic_defense_description(self):
        pmd = (
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        )
        return pmd[random.randrange(len(pmd))]

    def get_random_potion_magic_offense_description(self):
        pmo = (
            ('', ''),
            ('', ''),
            ('', ''),
            ('', ''),
        )
        pmo[random.randrange(len(pmo))]



