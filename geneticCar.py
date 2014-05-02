"""
Genetic Car Algorithm

@author: Riley Chapman, Sophie Li, Josh Sapers, Paul Titchener

@teamName: Track Bot Driver (TBD)
"""
#import driveMatrixEvolution
import Model
import View
import Controller

import pygame, random, math, time
from pygame.locals import *
import math

#generage a genome
#genomeLength = 4
#gen = driveMatrixEvolution.Genome(genomeLength) 


pygame.init()
walls = []
size = (800, 500)
chromNum = 0

screen = pygame.display.set_mode(size)
model = Model.Platformer_Model(size)
view = View.PyGameWindowView(model,screen)
controller = Controller.PyGameController(model)



running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
            controller.handle_pygame_event(event)
            
        if model.drawTrack == True and model.drawMode == True:
            controller.draw_track()
        if model.drawTrack == False and model.drawMode ==False and model.offsetMode == True:
            controller.offset_track(50)
            model.offsetMode = False

    if model.drawTrack == False and model.drawMode == False and model.offsetMode == False:
        controller.Drive()

    view.draw_sophie()
    time.sleep(0.001)
    if not False in [element.FAIL for element in model.ducks]:
        model.genome.evolve()
        time.sleep(5)
        model.new_generation()
        print "new generation"
        print "evolved",model.genome.chromosomes[0].genes
        chromNum = 0     
        model.Iteration =0
    
    #changes to next chromosome
 
    
    
      
pygame.quit()






#gen.live() #insert chromosome, test chomosme, repeat


#gen.print_genome()



