#Authers: Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#Due: July 19th, 2010
#File: Effect.py

#Base class which other Effects descend, should never be instantiated
class Effect:
    def __init__(self, duration):
        self.duration = duration

    #Active effects need to be applied each round
    #When the effect duration is decremented this method will be called
    #Only Active effects need implement apply
    def apply(self, owner):
        #just apply yourself, slacker
        self

#Stun Effect of variable duration, Stun prevents player or creatures for acting
class Stun_Effect(Effect):
    def __init__(self, duration):
        Effect.__init__(self, duration)
        self.duration = duration

#Heal-Over-Time Effect, heals the effect by bonus hp every round
#for duration rounds
class HOT_Effect(Effect):
    def __init__(self, duration, bonus):
        Effect.__init__(self, duration)
        self.bonus = bonus

    def apply(self, owner):
        owner.heal(self.bonus)

#Damage-Over-Time Effect, like HOT--but damage, (duh)
class DOT_Effect(Effect):
    def __init__(self, duration, damage):
        Effect.__init__(self, duration)
        self.damage = damage

    def apply(self, owner):
        owner.hp -= self.damage

#Defense effect of variable duration and strength (bonus)
#Defense effects give you a bonus to DS vs Physical Attacks
class Defense_Effect(Effect):
    def __init__(self, duration, bonus):
        Effect.__init__(self, duration)
        self.bonus = bonus

#Same as Defense_Effect, but gives you a bonus vs Magic Attacks
class Magic_Defense_Effect(Effect):
    def __init__(self, duration, bonus):
        Effect.__init__(self, duration)
        self.bonus = bonus

#Offense effect of variable duration and strength (bonus)
#Offense effects give you a bonus to OS for Physical Attacks (Weapons)
class Offense_Effect(Effect):
    def __init__(self, duration, bonus):
        Effect.__init__(self, duration)
        self.bonus = bonus    

#Same as Offense_Effect, but gives you a bonus for Magic Attacks
class Magic_Offense_Effect(Effect):
    def __init__(self, duration, bonus):
        Effect.__init__(self, duration)
        self.bonus = bonus

