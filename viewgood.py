# -*- coding: utf-8 -*-
"""
@author: sophiali
"""

import pygame, random, math, time
from pygame.locals import *

class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)

def hold_levels():
    """Normal function that holds our levels as lists. Any other way is too hard"""
    level = [[
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
        "W                                 W",
        "W         WWWWWW                  W",
        "W   WWWW       W                  W",
        "W   W        WWWW                 W",
        "W WWW  WWWW                       W",
        "W   W     W W                     W",
        "W   W     W   WWW                WW",
        "W   WWW WWW   W W                 W",
        "W     W   W   W W                 W",
        "WWW   W   WWWWW W                 W",
        "W W      WW                       W",
        "W W   WWWW   WWW                  W",
        "W     W    W   W                  W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "W                                 W",
        "WWWWWWWWWWWWW   WWWWWWWWWWWWWWWWW W",
        "W                                 W",
        "W                                 W",
        "WW                                W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                              ]]
    print level
    return level

def change_to_list(num):
    level = hold_levels()       
    for platform in level[num]:
        x = y = 0
        for row in level[num]:
            for col in row:
                if col == "W":
                    Wall((x, y))
#                    if col == "E":
#                        end_rect = pygame.Rect(x, y, 16, 16)
                x += 20
            y += 20
            x = 0
    return walls
    
        
class Platformer_Model:
    """ Encodes the game state """
    """TO-DO: Clean up these level lists"""
    def __init__(self):
        self.level1 = change_to_list(0)
        self.duck = Duck((155,230,249),20,20,40,40)
    
    def update(self):
        self.duck.update()

class Duck:
    """Code for moving car"""
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.vy = 0.0
        self.vx = 0.0
        self.friction = 0
        self.gravity = 0
        
    def update(self):
        self.x += collision_test(dx, 0)
        self.y += collision_test(0,dy)
        
    def collision_test(self, dx, dy):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
    
        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
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
        pygame.draw.rect(self.screen, pygame.Color(self.model.duck.color[0], self.model.duck.color[1], self.model.duck.color[2]), pygame.Rect(self.model.duck.x, self.model.duck.y, self.model.duck.width, self.model.duck.height))
        for wall in walls:
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), wall.rect)          
        pygame.display.update()


class PyGameKeyboardController:
    """ Manipulate game state based on keyboard input """
    def __init__(self, model):
        self.model = model
    
    def handle_pygame_event(self, event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.duck.vx += -2
        if event.key == pygame.K_RIGHT:
            self.model.duck.vx += 2
        if event.key == pygame.K_UP:
            self.model.duck.vy += -2
        if event.key == pygame.K_DOWN:
            self.model.duck.vy += 2


if __name__ == '__main__':
    pygame.init()
    walls = []
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    model = Platformer_Model()
    view = PyGameWindowView(model,screen)
    controller = PyGameKeyboardController(model)

    running = True

    while running:
           
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                controller.handle_pygame_event(event)
        
        model.update()
        view.draw()
        time.sleep(0.001)

    pygame.quit()