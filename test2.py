#creation and testing of the initial menu 
import pygame
import random
from sys import exit
pygame.init()

#setup the screen/ framerate
pygame.display.set_caption("Card game")
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()   

#COMMANDS
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #framerate 
    pygame.display.update()
    clock.tick(60)