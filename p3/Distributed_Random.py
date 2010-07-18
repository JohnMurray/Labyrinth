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
        sd1 = math.floor(.33 * diff)
        sd2 = math.floor(.44 * diff) 
        sd3 = diff // 2
        #Can make it err towards inferior weapons to make great weapons more rare
        positive = random.randint(1,100)
        roll = random.randint(1,100)
        if roll <= 66:
            if positive >= 75:
                return random.randint(mid,mid+sd1)
            else:
                return random.randint(mid-sd1,mid)
        elif roll <= 88:
            if positive >= 75:
                return random.randint(mid,mid+sd2)
            else:
                return random.randint(mid-sd2,mid)
        else:
            if positive >= 75:
                return random.randint(mid,mid+sd3)
            else:
                return random.randint(mid-3,mid)
