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
        item_type = random.randrange(100)
        #generate a spell
        if( item_type < 50 ):
            self.generate_spell()
        #generate a potion
        else:
            self.generate_potion()


    def generate_potion(self):
        spell_type = random.randrange(100)
        if( spell_type < 20 ):
            #create healing potion
            name_descrip = self.get_random_potion_healing_description()
        elif( spell_type < 40 ):
            #create defense potion
        elif( spell_type < 60 ):
            #create offense potion
        elif( spell_type < 80 ):
            #create magic deffense potion
        else:
            #create magic offense potion
        

    def generate_spell(self):
        #get a random sell type 
        spell_type = radom.randrange(100)
        if( spell_type < 33 ):
            #create a attack spell
            
        elif( spell_type < 66 ):
            #create a defense spell
            
        else:
            #create a stun spell
            
        


    ##---------------------------------------------------------
    ## Rare Generate (generates rare items)
    ##---------------------------------------------------------

    def generate_rare(self):
        item_type = random.randrange(100)
        #generate a spell
        if( item_type < 50 ):
            self.generate_spell()
        #generate a potion
        else:
            self.generate_potion()
        

    def generate_rare_potion(self):
        spell_type = random.randrange(100)
        if( spell_type < 20 ):
            #create healing potion
        elif( spell_type < 40 ):
            #create defense potion
        elif( spell_type < 60 ):
            #create offense potion
        elif( spell_type < 80 ):
            #create magic deffense potion
        else:
            #create magic offense potion
        

    def generate_rare_spell(self):
        #get a random sell type 
        spell_type = radom.randrange(100)
        if( spell_type < 33 ):
            #create a attack spell
            
        elif( spell_type < 66 ):
            #create a defense spell
            
        else:
            #create a stun spell
        

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



