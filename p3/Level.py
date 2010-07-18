#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Level.py
#Note: Level consists of a 2-dimensional list (acts as an array) that creates
#      a matrix of Rooms. This makes moving directionally (north, south, etc.)
#      more natural programatically

import Room_Module
from Room_Module import *


#Level
#   __init__ : constructor
#   move_(north, east, south, west): move to a new room
#   (get, set)_current_room: getter and setter for current/active room
#   defeated_all_creatures: (bool) are all creatures defeated
#   number_of_creatures_left: the num. of creatures in level still
#   __iter__ : exposes and iterator for the Level class

class Level:

    def __init__(self, dimension):
        #code here
        self.rooms = list()
        for i in range(0, dimension):
            #create a sub-list
            self.rooms.append(list())
            for j in range(0, dimension):
                #create a room
                room = Room_Factory.generate()
                self.rooms[i].append(room)
        self.current = (0, 0)

    def move_north(self):
        i = self.current[0]
        j = self.current[1]

        if i == 0:
            i = len(self.rooms) - 1
        else:
            i+=1
        self.current = (i, j)

    def move_east(self):
        i = self.current[0]
        j = self.current[1]
        
        if j == len(self.rooms[i]) - 1:
            j = 0
        else:
            j+=1
        self.current = (i, j)

    def move_south(self):
        i = self.current[0]
        j = self.current[1]
        
        if i == len(self.rooms) - 1:
            i = 0
        else:
            i-=1
        self.current = (i, j)
    
    def move_west(self):
        i = self.current[0]
        j = self.current[1]

        if j == 0:
            j = len(self.rooms[i]) - 1
        else:
            j-=1
        self.current = (i, j)

    def get_current_room(self):
        return self.rooms[self.current[0]][self.current[1]]

    def set_current_room(self, room):
        self.rooms[self.current[0]][self.current[1]] = room

    def defeated_all_creatures(self):
        flag = True
        for i in self.rooms:
            for j in i:
                if j.creature != None:
                    flag = False
        return flag

    def number_of_creatures_left(self):
        count = 0
        for i in self.rooms:
            for j in i:
                if j.creature != None:
                    count+=1

    def __iter__(self):
        for i in self.rooms:
            for j in i:
                yield j
