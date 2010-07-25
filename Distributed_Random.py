#Authors: Brad Stephens, John Murray
#Project: CSC 407 - Program 3
#Due: July 19th, 2010
#File Distributed_Random.py

import math
import random

#A class to generate random numbers with distributions rather than equal chance
class Distributed_Random:
    def __init__(self):
        self

    def randint(self, low, high):
        diff = math.floor(high - low)
        mid = low + (diff // 2)
        mid *= 1000
        diff *= 1000
        sd1 = math.floor(.33 * diff)
        sd2 = math.floor(.44 * diff) 
        sd3 = diff // 2
        #Can make it err towards inferior stats to make great equipment more rare
        positive = random.randint(1,100)
        roll = random.randint(1,100)
        if roll <= 66:
            if positive >= 75:
                return random.randint(round(mid / 1000),round((mid+sd1) / 1000))
            else:
                return random.randint(round((mid-sd1) / 1000),round(mid / 1000))
        elif roll <= 88:
            if positive >= 75:
                return random.randint(round(mid / 1000),round((mid+sd2) / 1000))
            else:
                return random.randint(round((mid-sd2) / 1000),round(mid / 1000))
        else:
            if positive >= 75:
                return random.randint(round(mid / 1000),round((mid+sd3) / 1000))
            else:
                return random.randint(round((mid-sd3) / 1000),round(mid / 1000))
