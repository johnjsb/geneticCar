"""
@author: Sophie Li and Paul Titchener
"""

import pygame, random, math, time
from pygame.locals import *
import math
from car import *

class Platformer_Model:
    """ Encodes the game state """
    """TO-DO: Clean up these level lists"""
    def __init__(self,screen_size):
        #self.level1 = change_to_list(0)
        self.car = car(self,(100,100))
        self.drawTrack = False
        self.drawMode = True
        self.Track = []
        self.offsetMode = True
        self.Track1 = [[],[]]
        self.Track2 = [[],[]]
        self.Track3 = [[],[]]
        self.ArrayTrack = []
        self.drawListInner = []
        self.drawListOuter = []
        #making the track be an array instead of pair of lists
        xInd = 0
        while xInd in range(screen_size[0]):
            yInd = 0

            self.ArrayTrack.append([])
            while yInd in range(screen_size[1]):
                self.ArrayTrack[xInd].append(0)
                yInd +=1
            xInd +=1


        
    def update(self):
        self.car.update(vx, vy)

    def new_individual(self):
        if self.car.FAIL:
            self.car = car(self,(100,100))



def distance(L,Absolute=False):
    """returns the sum of the distances between the elements of a lists
    Input: list
    Output: sum of the distances bewtwen the elements of the list
    """
    if not Absolute:
        x = 0
        y = 0
        for element in L:
            x += element[0]
            y += element[1]
        return (x,y)#math.sqrt(float(x)**2 + float(y)**2)
    else:
        x = 0
        y = 0
        for element in L:
            x += abs(element[0])
            y += abs(element[1])
        return (x,y)#math.sqrt(float(x)**2 + float(y)**2)
