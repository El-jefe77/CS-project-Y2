import pygame
import random
from sys import exit
pygame.init()

#setup the screen/ framerate
pygame.display.set_caption("Card game")
screen = pygame.display.set_mode((1200,700))
clock = pygame.time.Clock()              

#Surface content (background)/ siz-e of surface "BACKGROUND"
background_surface = pygame.image.load("images/table.jpg").convert_alpha()
background_surface = pygame.transform.scale(background_surface, (1200, 700))

#object render/ ORIGINAL CARD/ size of card "aspect ratio" (NO OOB) example only 
card = pygame.image.load("cards img/8H.png").convert_alpha()
card1 = pygame.transform.scale_by(card, 0.2)


#if card given from "classes = heart then go to heart function"
#function = if card was = to heart, then check number and select a card image


#COMMANDS
    #"while true" will create an infinite loop, meaning it will execute it indefinitely until the program is interrupted or terminated
    #all operations inside the while loop are constantly updated 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

 #COORDINATES OF SURFACES image
    screen.blit(background_surface,(0,0))
    screen.blit(card1, (100, 100))

    #framerate 
    pygame.display.update()
    clock.tick(60)

    #wont work due to changes in classes.py