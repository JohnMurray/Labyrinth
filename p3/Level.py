#Authors: Brad Stephens, John Murray 
#Project: CSC 407 - Program 3 
#Due: July 19th, 2010
#File: Level.py
#Note: Level consists of a 2-dimensional list (acts as an array) that creates
#      a matrix of Rooms. This makes moving directionally (north, south, etc.)
#      more natural programatically

import Room_Module
from Room_Module import *
import random


#Level
#   __init__ : constructor
#   move_(north, east, south, west): move to a new room
#   (get, set)_current_room: getter and setter for current/active room
#   defeated_all_creatures: (bool) are all creatures defeated
#   number_of_creatures_left: the num. of creatures in level still
#   __iter__ : exposes and iterator for the Level class

class Level:

    def __init__(self, dimension, mob_size = -1):
        #code here
        #self.rooms = list()
        #for i in range(0, dimension):
        #    #create a sub-list
        #    self.rooms.append(list())
        #    for j in range(0, dimension):
        #        #create a room
        #        rf = Room_Factory()
        #        room = rf.generate()
        #        self.rooms[i].append(room)
        #self.current = (0, 0)

        #new labyrinth code here
        self.gen_lab(dimension)
        self.current = (0, 0)

        #determine mob size here
        if( mob_size == -1 ):
            self.mob_size = round(dimension / 2)
        else:
            self.mob_size = mob_size

    #def: rr
    #purpose: random room (rr) return
    def rr(self, r):
        if( random.randrange(100) > 50):
            return r
        else:
            return None

    def gen_lab(self, dimension):
        self.rooms = list()
        for i in range(dimension):
            self.rooms.append(list())
            for j in range(dimension):
                rf = Room_Factory()
                room = rf.generate()
                if( i == 0 and j == 0 ):
                    self.rooms[i].append(room)
                elif( i == dimension - 1 ):
                    self.rooms[i].append(room)
                else:
                    #if room above
                    if( i > 0 and self.rooms[i - 1][j] != None ):
                        #if no room above left
                        if( j == 0 or self.rooms[i - 1][j - 1] == None ):
                            #if no room above right
                            if( j == dimension - 1 or self.rooms[i - 1][j + 1] == None ):
                                self.rooms[i].append(room)
                            #there is a room above-right
                            else:
                                self.rooms[i].append(self.rr(room))
                        #there is room above-left
                        else:
                            k = i - 1
                            l = j - 1
                            solved = False
                            #while there are rooms still to the left
                            while( l > -1 and self.rooms[k][l] != None and not solved):
                                #room has a room below
                                if( k < dimension - 1 and self.rooms[k + 1][l] != None ):
                                    self.rooms[i].append(self.rr(room))
                                    solved = True
                                #room has no room below
                                else:
                                    l -= 1
                            else:
                                #we did not find a connecting path/room
                                if( solved == False ):
                                    self.rooms[i].append(room)
                    #there are no rooms above
                    else:
                        self.rooms[i].append(self.rr(room))
                                


    def __str__(self):
        out = ''
        for i in self.rooms:
            out2 = ''
            for j in i:
                if j == None:
                    out2 += ' '
                elif( j == self.get_current_room() ):
                    out2 += 'I'
                else:
                    out2 += 'X'
            out += out2 + "\n"
        out += "Legend:\nX => Room\nI => You\n"
        return out

    def move_north(self):
        i = self.current[0]
        j = self.current[1]

        if i == 0:
            i = len(self.rooms) - 1
        else:
            i+=1
        self.current = (i, j)

    def move_north_lab(self):
        i = self.current[0]
        j = self.current[1]
        if( i == 0 ):
            print "You cannot travel north form here."
        else:
            if( self.rooms[i-1][j] == None ):
                print "You cannot travel north from here."
            else:
                i -= 1
        self.current = (i, j)


    def move_east(self):
        i = self.current[0]
        j = self.current[1]
        
        if j == len(self.rooms[i]) - 1:
            j = 0
        else:
            j+=1
        self.current = (i, j)

    def move_east_lab(self):
        i = self.current[0]
        j = self.current[1]

        if( j == len(self.rooms[i]) - 1):
            print "You cannot travel east from here."
        else:
            if( self.rooms[i][j+1] == None ):
                print "You cannot travel east from here."
            else:
                j += 1
        self.current = (i, j)

    def move_south(self):
        i = self.current[0]
        j = self.current[1]
        
        if i == len(self.rooms) - 1:
            i = 0
        else:
            i-=1
        self.current = (i, j)
    
    def move_south_lab(self):
        i = self.current[0]
        j = self.current[1]

        if( i == len(self.rooms) - 1 ):
            print "You cannot move south from here."
        else:
            if( self.rooms[i + 1][j] == None ):
                print "You cannot move south from here."
            else:
                i += 1
        self.current = (i, j)

    def move_west(self):
        i = self.current[0]
        j = self.current[1]

        if j == 0:
            j = len(self.rooms[i]) - 1
        else:
            j-=1
        self.current = (i, j)

    def move_west_lab(self):
        i = self.current[0]
        j = self.current[1]

        if( j == 0 ):
            print "You cannot travel west from here."
        else:
            if( self.rooms[i][j - 1] == None ):
                print "You cannot travel west from here."
            else:
                j -= 1
        self.current = (i, j)

    def get_current_room(self):
        return self.rooms[self.current[0]][self.current[1]]

    def set_current_room(self, room):
        self.rooms[self.current[0]][self.current[1]] = room

    def defeated_all_creatures(self):
        flag = True
        for i in self.rooms:
            for j in i:
                if( j != None ):
                    if j.creature != None:
                        flag = False
        return flag

    def number_of_creatures_left(self):
        count = 0
        for i in self.rooms:
            for j in i:
                if j != None:
                    if j.creature != None:
                        count+=1

    def __iter__(self):
        for i in self.rooms:
            for j in i:
                yield j


    #override for navigation (remove to use old nav style)
    move_north = move_north_lab
    move_east = move_east_lab
    move_south = move_south_lab
    move_west = move_west_lab
