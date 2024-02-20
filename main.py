import pygame
import random
from sys import exit
from classes import Deck
pygame.init()

#setup the screen/ framerate
pygame.display.set_caption("Card game")
screen = pygame.display.set_mode((1200,700))
clock = pygame.time.Clock()              

#Surface content (background)/ siz-e of surface "BACKGROUND"
background_surface = pygame.image.load("images/table.jpg").convert_alpha()
background_surface = pygame.transform.scale(background_surface, (1200, 700))

#BUTTON FOR PLAYER DECISION
pygame.display.set_caption("button")
font = pygame.font.SysFont("Georgia", 40, bold=True)
surf = font.render("Quit", True, "white")
button = pygame.Rect(200, 200, 110, 60)

#object render/ size of card /
lst = list(Deck)            #gets card from the set created (deck)
print(lst[0].get_image())

lst = list(Deck)            #gets card from the set created (deck)
print(lst[1].get_image1())


#setup the screen/ framerate / image size / ui / images cards and background 
pygame.display.set_caption("Card game")
screen = pygame.display.set_mode((1200,700))
clock = pygame.time.Clock()   

card = pygame.image.load(lst[0].get_image()).convert_alpha()
card = pygame.transform.scale_by(card, 0.25)

card1 = pygame.image.load(lst[1].get_image1()).convert_alpha()
card1 = pygame.transform.scale_by(card1, 0.25)

#if card given from "classes = heart then go to heart function"
#function = if card was = to heart, then check number and select a card image

#COMMANDS
    #"while true" will create an infinite loop, meaning it will execute it indefinitely until the program is interrupted or terminated
    #all operations inside the while loop are constantly updated 

#first decision and then put the dealers cards 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:        #button actions constructor 
            if button.collidepoint(event.pos):
                print("HOLA :)")   #action of button


 #COORDINATES OF SURFACES image
    screen.blit(background_surface,(0,0))
    screen.blit(card, (425, 475))
    screen.blit(card1, (625, 475))

    #draw the button on the screen
    pygame.draw.rect(screen, (255, 0, 0), button)  # Red rectangle as the button
    screen.blit(surf, (button.x + 10, button.y + 10))  # Display the text on the button

    #framerate 
    pygame.display.update()
    clock.tick(60)

    #wont work due to changes in classes.py