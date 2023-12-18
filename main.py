import pygame
from sys import exit
from classes import Card
pygame.init()

#setup the screen/ framerate
pygame.display.set_caption("Card game")
screen = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()              

#creation of surfaces 
    #Surface content (background)/ size of surface
background_surface = pygame.image.load("images/table.jpg").convert_alpha()
background_surface = pygame.transform.scale(background_surface, (1200, 600))

#ORIGINAL CARD/ size of card "aspect ratio" (NO OOB)
card = pygame.image.load("cards img/ace_of_spades.png").convert_alpha()
card1 = pygame.transform.scale_by(card, 0.2)




#COMMANDS
    #"while true" will create an infinite loop, meaning it will execute it indefinitely until the program is interrupted or terminated
    #all operations inside the while loop are constantly updated 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

 #COORDINATES OF SURFACES
    screen.blit(background_surface,(0,0))
    screen.blit(card1, (100, 100))

    #framerate 
    pygame.display.update()
    clock.tick(60)