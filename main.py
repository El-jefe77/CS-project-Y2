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

#BUTTONS
font = pygame.font.SysFont("ARIAL", 30, bold=True)     #font /// font size
surf_menu = font.render("Menu", True, "white")                #text inside the button / colour
button_menu = pygame.Rect(25, 25, 80, 50)                     #position button /// size button

surf_check = font.render("Check", True, "white")                #text inside the button / colour
button_check = pygame.Rect(545, 600, 80, 50)     

surf_raise = font.render("Raise", True, "white")                #text inside the button / colour
button_raise = pygame.Rect(700, 600, 80, 50)    

surf_fold = font.render("Fold", True, "white")                #text inside the button / colour
button_fold = pygame.Rect(200, 600, 80, 50)    

#object render/ size of card /
lst = list(Deck)             #gets card from the set created (deck)
print(lst[0].get_image())

lst = list(Deck)            #gets card from the set created (deck)
print(lst[1].get_image1())


#setup the screen/ framerate / image size / ui / images cards and background 
card = pygame.image.load(lst[0].get_image()).convert_alpha()
card = pygame.transform.scale_by(card, 0.25)

card1 = pygame.image.load(lst[1].get_image1()).convert_alpha()
card1 = pygame.transform.scale_by(card1, 0.25)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:        #button actions constructor 
            if button_menu.collidepoint(event.pos):
                print("HOLA MENU :)")                        #action of button
        if event.type == pygame.MOUSEBUTTONDOWN:        #button actions constructor 
            if button_check.collidepoint(event.pos):
                print("HOLA CHECK :)")                        #action of button
        if event.type == pygame.MOUSEBUTTONDOWN:        #button actions constructor 
            if button_raise.collidepoint(event.pos):
                print("HOLA RAISE :)")  
        if event.type == pygame.MOUSEBUTTONDOWN:        #button actions constructor 
            if button_fold.collidepoint(event.pos):
                print("HOLA FOLD :)")  


 #COORDINATES OF SURFACES image
    screen.blit(background_surface,(0,0))
    screen.blit(card, (425, 475))
    screen.blit(card1, (625, 475))

    #draw the button on the screen
    pygame.draw.rect(screen, (0, 0, 0), button_menu)      #colour of button
    screen.blit(surf_menu, (button_menu.x + 7, button_menu.y + 7))  # position of the text inside button

    pygame.draw.rect(screen, (0, 0, 100), button_check)      #colour of button
    screen.blit(surf_check, (button_check.x, button_check.y ))  # position of the text inside button

    pygame.draw.rect(screen, (0, 0, 100), button_raise)      #colour of button
    screen.blit(surf_raise, (button_raise.x, button_raise.y ))  # position of the text inside button

    pygame.draw.rect(screen, (0, 0, 100), button_fold)      #colour of button
    screen.blit(surf_fold, (button_fold.x, button_fold.y ))  # position of the text inside button


    #framerate 
    pygame.display.update()
    clock.tick(60)

    #wont work due to changes in classes.py