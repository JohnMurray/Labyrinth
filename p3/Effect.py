#Authers: Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#Due: July 19th, 2010
#File: Effect.py

#Base class which other Effects descend, should never be instantiated
class Effect:
    def __init__(self, duration):
        self.duration = duration

#Stun Effect of variable duration, Stun prevents player or creatures for acting
class Stun_Effect(Effect):
    def __init__(self, duration):
        Effect.__init__(self, duration)

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

