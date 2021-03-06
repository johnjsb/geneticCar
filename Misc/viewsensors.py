# -*- coding: utf-8 -*-
"""
@author: sophiali
"""

import pygame, random, math, time
from pygame.locals import *
import math
from numpy import mean

walls = []

class Wall(object):
    def __init__(self, pos):

        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        self.pos = pos

class Platformer_Model:
    """ Encodes the game state """
    """TO-DO: Clean up these level lists"""
    def __init__(self):
        #self.level1 = change_to_list(0)
        self.duck = Duck(self,(100,100))
        self.drawTrack = False
        self.drawMode = True
        self.Track = []
        self.offsetMode = True
        self.trackPopped = []
        self.innerTrack = []
        self.Track1 = [[],[]]
        self.Track2 = [[],[]]
        self.Track3 = [[],[]]
        
    def update(self):
        self.duck.update(vx, vy)

class Duck:
    """Code for moving car"""

    def __init__(self,model,pos):
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        self.x = pos[0]       #x position
        self.y = pos[1]        #y position
        self.dx = 0        
        self.dy = 0
        self.theta=0 #angle from the reference frame of the car is at angle zero if it pointed in the positive x direction. 
        self.radius = 5 #wheel radius
        self.pointlist = [pos,pos]
        self.model= model

    def update(self, w1, w2):
        """ updates the position and angle of the car given the speed of rotation of the wheel. Angular veloctity of the wheel is use rather than a torque output becuase
        the only way to reasonable simuulate a torque output would be to calcualte the loading curve of the motor. At this point in the project it is 
        more reasonable to assume an ideal motor that does not respond to differenct loading conditions, or a motor with a well tuned PID loop and feedback
        Inputs:
        W1: angular velocity of wheel 1. This is the wheel on the left side of the car, looking from the back
        W2: angular velocity of wheel 2. This is the wheel on the right side of the car, looking from the back

        Outputs:
        Car angle, x and y updated
        Car angle is determined from the reference frame of the car
        """
        t=(w2-w1)*self.radius #distance around the turning circle that the wheels have traveled against each other
        w = math.atan(float(t)/self.rect.width)

        dist = float(w1+w2)/2 #calculates the forward distance by which the car travels

        self.theta+=w #updates angle\

        #updating the position of the car
        self.dx = dist*math.cos(self.theta)
        self.dy = dist*math.sin(self.theta)

        self.x += self.dx
        self.y += self.dy
        self.rect.center = (self.x,self.y)

        """
        print 'w',w,"theta",self.theta,'dist',dist
        print 'x',self.x,'dx',self.dx,'y',self.y,'dy',self.dy
        print "wheel1pos", (self.x-self.rect.width/2*math.sin(self.theta),self.y+self.rect.width/2*math.cos(self.theta) )
        #print "wheel2pos", (self.x+self.rect.width/2*math.sin(self.theta),self.y-self.rect.width/2*math.cos(self.theta) )

        print """
        self.pointlist.append((self.x,self.y))
    

        if self.dx != 0:
            self.collision_test(self.dx, 0)
        if self.dy != 0:
            self.collision_test(0, self.dy)
        
    def collision_test(self, vx, vy):
        # Move the rect
        self.rect.x += vx
        self.rect.y += vy
    
        # If you collide with a wall, move out based on velocity
        for wall in self.model.Track3[1]:
            if self.rect.colliderect(wall.rect):
                if vx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if vx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if vy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if vy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
        for wall in self.model.Track3[0]:
            if self.rect.colliderect(wall.rect):
                if vx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if vx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if vy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if vy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom
                    
    

        
class Platform:
    """ Encodes the state of a singular rectangular platform in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class PyGameWindowView:
    """ Draws our game in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
                   
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(screen, pygame.Color(0,255,0), model.duck.rect)
        for wall in walls:
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), wall.rect)          
        pygame.display.update()

    def draw1(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.rect(screen, pygame.Color(0,255,0), model.duck.rect)
        if self.model.drawMode == True:
            for trackblock in model.Track:
                pygame.draw.rect(screen,pygame.Color(255,255,255),trackblock.rect)
        else:
            for trackblock in model.Track3[1]:
                pygame.draw.rect(screen,pygame.Color(255,255,255),trackblock.rect)
            for trackblock in model.Track3[0]: #model.FinalTrack[1]:
                pygame.draw.rect(screen,pygame.Color(255,0,255),trackblock.rect)
        pygame.display.update()

    def draw2(self):
        drawListInner  = []
        drawListOuter = []
        self.screen.fill(pygame.Color(0,0,0))

        pygame.draw.rect(screen, pygame.Color(0,255,0), model.duck.rect)
        if self.model.drawMode == True:
            for trackblock in model.Track:
                intRect = trackblock.rect.inflate(50,50)
                pygame.draw.rect(screen,pygame.Color(255,255,255),intRect)
        else:
            drawInd = 0
            for trackblock in model.Track3[1]:
                drawListInner.append((trackblock.pos[0],trackblock.pos[1]))
            for trackblock in model.Track3[0]: #model.FinalTrack[1]:
                drawListOuter.append((trackblock.pos[0],trackblock.pos[1]))
            pygame.draw.lines(screen,(255,255,255),True,drawListInner)
            pygame.draw.lines(screen,(255,255,255),True,drawListOuter)   

        pygame.display.update()

    def draw3(self):
        drawListInner  = []
        drawListOuter = []
        self.screen.fill(pygame.Color(0,0,0))
        pygame.draw.lines(screen,(255,255,255),False,self.model.duck.pointlist)

        pygame.draw.rect(screen, pygame.Color(0,255,0), model.duck.rect)
        if self.model.drawMode == True:
            for trackblock in model.Track:
                intRect = trackblock.rect.inflate(50,50)
                pygame.draw.rect(screen,pygame.Color(255,255,255),intRect)
        else:
            drawInd = 0
            for trackblock in model.Track3[1]:
                drawListInner.append((trackblock.pos[0],trackblock.pos[1]))
            for trackblock in model.Track3[0]: #model.FinalTrack[1]:
                drawListOuter.append((trackblock.pos[0],trackblock.pos[1]))
            pygame.draw.lines(screen,(255,255,255),True,drawListInner)
            pygame.draw.lines(screen,(255,255,255),True,drawListOuter)   

        pygame.display.update()

    def distance_calculate(self):
        xp = float(self.model.duck.rect.x)
        yp = float(self.model.duck.rect.y)
        
        xp_l = xp
        yp_l = yp
        
        xp_r = xp
        yp_r = yp
        
        print "Current car location", xp, yp
        theta = float(self.model.duck.theta)
        theta_back = theta + (pi/2)
        print "Current car orientation", theta
        x = 500*sin(theta)
        y = 500*cos(theta)
        
        x_l = 500*sin(theta_back)
        y_l = 500*cos(theta_back)
        
        x_r = 500*sin(theta_back - pi)
        y_r = 500*cos(theta_back - pi)
        
        distance = math.sqrt((x-xp)**2 + (y-yp)**2)
        dx = (x-xp)/distance * 2
        dy = (y-yp)/distance * 2
        pygame.draw.line(screen,(255,0,0),(xp,yp),(x,y))

        distance1 = math.sqrt((x_l-xp)**2 + (y_l-yp)**2)
        dx_l = (x_l-xp)/distance1 * 2
        dy_l = (y_l-yp)/distance1 * 2
        pygame.draw.line(screen,(0,255,0),(xp,yp),(x_l,y_l))        
        
        distance2 = math.sqrt((x_r-xp)**2 + (y_r-yp)**2)
        dx_r = (x_r-xp)/distance2 * 2
        dy_r = (y_r-yp)/distance2 * 2
        pygame.draw.line(screen,(0,0,255),(xp,yp),(x_r,y_r))   
        
        pygame.display.update()

        f_inner = []
        l_inner = []
        f_outer = []
        l_outer = []
        
        r_outer = []
        r_inner = []        
        
        while distance >= 2:
            xp += dx
            yp += dy
            
            distance -= 2
            
            #finds distances for inner wall
            for wall in self.model.Track3[0]:
                if wall.rect.collidepoint(xp,yp):
                    f_inner.append((xp, yp))

            #finds distances for outer wall
            for wall in self.model.Track3[1]:
                if wall.rect.collidepoint(xp,yp):
                    f_outer.append((xp,yp))

        while distance1 >= 2:         
            xp_l += dx_l
            yp_l += dy_l
            
            distance1 -= 2
            #finds distances for inner wall
            for wall in self.model.Track3[0]:
                if wall.rect.collidepoint(xp_l,yp_l):
                    l_inner.append((xp_l, yp_l))

            #finds distances for outer wall
            for wall in self.model.Track3[1]:
                if wall.rect.collidepoint(xp_l,yp_l):
                    l_outer.append((xp_l, yp_l))
                    
        while distance2 >= 2:
            xp_r += dx_r
            yp_r += dy_r
            
            distance2 -= 2
            
            #finds distances for inner wall
            for wall in self.model.Track3[0]:
                if wall.rect.collidepoint(xp_r,yp_r):
                    r_inner.append((xp_r, yp_r))

            #finds distances for outer wall
            for wall in self.model.Track3[1]:
                if wall.rect.collidepoint(xp_r,yp_r):
                    r_outer.append((xp_r, yp_r))

        print "Closest forward outer", tuple(map(mean, zip(*f_outer)))
        print "Closest forward inner", (tuple(map(mean, zip(*f_inner))))
        
        print "Closest left outer", tuple(map(mean, zip(*l_outer)))
        print "Closest left inner", tuple(map(mean, zip(*l_inner)))

        print "Closest right outer", tuple(map(mean, zip(*r_outer)))
        print "Closest right inner", tuple(map(mean, zip(*r_inner)))
        
        print "  "
        
class PyGameController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_event_key(self, event):
        if event.type == KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.model.duck.update(4,5)
            if event.key == pygame.K_RIGHT:
                self.model.duck.update(5,4)
            if event.key == pygame.K_UP:
                self.model.duck.update(5,5)
            if event.key == pygame.K_DOWN:
                self.model.duck.update(-5,-5)
        else:
            return
        
                
    def handle_pygame_event_mouse(self,event):
        if event.type == MOUSEBUTTONDOWN:
            self.model.drawTrack = True
    
        elif event.type == MOUSEBUTTONUP:
            self.model.drawTrack=False
            self.model.drawMode =False
        else:
            return

    def draw_track(self):
        wallBlock = Wall(pygame.mouse.get_pos())
        model.Track.append(wallBlock)


    def offset_track(self,radius):
        i = 0
        for element in self.model.Track:
            xDiff = float((element.pos[0] - self.model.Track[i-1].pos[0]))
            yDiff = float((element.pos[1] - self.model.Track[i-1].pos[1]))

            if xDiff == 0 and yDiff ==0:
                pass
            elif xDiff != 0:
                xSign = xDiff/abs(xDiff)
                slope = yDiff/xDiff#float((element.pos[1] - self.model.Track[i-1].pos[1]))/(element.pos[0] - self.model.Track[i-1].pos[0])
                if slope != 0:
                    ySign = yDiff/abs(yDiff)
                    slopeSign = slope/abs(slope)

                    perpendicularSlope = -1.0/slope
                    angle = math.atan(perpendicularSlope)
                    innerPos = (element.pos[0] + abs(math.cos(angle))*radius*(xSign**2*ySign) , element.pos[1] + abs(math.sin(angle))*radius*-(xSign*ySign**2))
                    outerPos = (element.pos[0] - abs(math.cos(angle))*radius*(xSign**2*ySign) , element.pos[1] - abs(math.sin(angle))*radius*-(xSign*ySign**2))
                else:
                    innerPos = (element.pos[0] , element.pos[1] + radius*-xDiff/abs(xDiff))
                    outerPos = (element.pos[0] , element.pos[1] - radius*-xDiff/abs(xDiff))

            else:
                innerPos = (element.pos[0] +radius*yDiff/abs(yDiff), element.pos[1])
                outerPos = (element.pos[0] -radius*yDiff/abs(yDiff), element.pos[1])
            
            #print math.sqrt((innerPos[0]-outerPos[0])**2 + (innerPos[1]-outerPos[1])**2)


            innerBlock = Wall(innerPos)
            outerBlock = Wall(outerPos)
            self.model.Track1[0].append(innerBlock)
            self.model.Track1[1].append(outerBlock)

            i +=1

        #Check for outliers 
        innerInd = 1
        while innerInd in range(len(self.model.Track1[0])-2):
            innerPop = False
            if dist_walls(self.model.Track1[0][innerInd],self.model.Track1[0][innerInd+1]) > 20:
                innerPop = True
            if not innerPop:
                self.model.Track2[0].append(self.model.Track1[0][innerInd])
            innerInd +=1

        outerInd = 1
        while outerInd in range(len(self.model.Track1[1])-2):
            outerPop = False
            if dist_walls(self.model.Track1[1][outerInd],self.model.Track1[1][outerInd+1]) > 20 :
                outerPop = True
            if not outerPop:
                self.model.Track2[1].append(self.model.Track1[1][outerInd])
            outerInd +=1





        #Make sure that the tracks are the proper distance appart
        j = 0
        numPopped = 0
        sizePopped = len(self.model.Track2[0])
        for innerElement in self.model.Track2[0]:
            popped = False
            for outerElement in self.model.Track2[1]:
                if not popped:    
                    #if abs(innerElement.pos[0] - outerElement.pos[0]) < radius*2+5 and abs(innerElement.pos[1] - outerElement.pos[1]) < radius*2+5: #radius-20 > math.sqrt((innerElement.pos[0]-outerElement.pos[0])**2 + (innerElement.pos[1]-outerElement.pos[1])**2) :# If the distance is too snall between any two inner and outer elements, remove those elements
                    if  math.sqrt((innerElement.pos[0]-outerElement.pos[0])**2 + (innerElement.pos[1]-outerElement.pos[1])**2) <= float(radius*2-5) :
        
                        popped = True
                        numPopped +=1

            if not popped:
                self.model.Track3[0].append(innerElement)
            j+=1

        for element in self.model.Track2[1]:
            self.model.Track3[1].append(element)

        print 'number of popped elements',numPopped

def dist_walls(wall1,wall2):
    return math.sqrt((wall1.pos[0]-wall2.pos[0])**2 + (wall1.pos[1]-wall2.pos[1])**2)

if __name__ == '__main__':
#    walls = []
    pygame.init()
    walls = []
    size = (1200, 900)

    screen = pygame.display.set_mode(size)
    model = Platformer_Model()
    view = PyGameWindowView(model,screen)
    controller = PyGameController(model)


    running = True

    while running:
           
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                controller.handle_pygame_event_mouse(event)
            if event.type == KEYDOWN: 
                controller.handle_pygame_event_key(event)
                view.distance_calculate()
                
            if model.drawTrack == True and model.drawMode == True:
                controller.draw_track()
            if model.drawTrack == False and model.drawMode ==False and model.offsetMode == True:
                controller.offset_track(50)
                model.offsetMode = False
            

        
#        model.update()
        view.draw1()
        time.sleep(0.001)

    pygame.quit()