#Authers: Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#Due: July 19th, 2010
#File: Effect.py

class Effect:
    def __init__(self, duration):
        self.duration = duration

class Stun_Effect(Effect):
    def __init__(self, duration):
        Effect.__init__(self, duration)

class Defense_Effect(Effect):
    def __init__(self, duration, bonus):
        Effect.__init__(self, duration)
        self.bonus = bonus

class Magic_Defense_Effect(Effect):
    def __init__(self, duration, bonus):
        Effect.__init__(self, duration)
        self.bonus = bonus

class Offense_Effect(Effect):
    def __init__(self, duration, bonus):
        Effect.__init__(self, duration)
        self.bonus = bonus    

class Magic_Offense_Effect(Effect):
    def __init__(self, duration, bonus):
        Effect.__init__(self, duration)
        self.bonus = bonus

