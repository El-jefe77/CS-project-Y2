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

backcard_surface = pygame.image.load("images/back_card.png").convert_alpha()
backcard_surface = pygame.transform.scale(backcard_surface, (50, 50))

#hi owen

#BUTTONS
font = pygame.font.SysFont("ARIAL", 30, bold=True)     #font /// font size
surf_menu = font.render("Menu", True, "white")                #text inside the button / colour
button_menu = pygame.Rect(25, 25, 80, 50)                     #position button /// size button

surf_check = font.render("Check", True, "white")              #text inside the button / colour
button_check = pygame.Rect(545, 600, 80, 50)     

surf_raise = font.render("Raise", True, "white")              #text inside the button / colour
button_raise = pygame.Rect(700, 600, 80, 50)    

surf_fold = font.render("Fold", True, "white")                #text inside the button / colour
button_fold = pygame.Rect(200, 600, 80, 50)    


# CARD size / ui / images cards and background 
card = pygame.image.load(Deck[0].get_image()).convert_alpha()
card = pygame.transform.scale_by(card, 0.20)
card1 = pygame.image.load(Deck[1].get_image()).convert_alpha()
card1 = pygame.transform.scale_by(card1, 0.20)

#west
card_w1 = pygame.image.load(Deck[2].get_image()).convert_alpha()
card_w1 = pygame.transform.scale_by(card_w1, 0.20)
card_w2 = pygame.image.load(Deck[3].get_image()).convert_alpha()
card_w2 = pygame.transform.scale_by(card_w2, 0.20)

#east
card_e1 = pygame.image.load(Deck[4].get_image()).convert_alpha()
card_e1 = pygame.transform.scale_by(card_e1, 0.20)
card_e2 = pygame.image.load(Deck[5].get_image()).convert_alpha()
card_e2 = pygame.transform.scale_by(card_e2, 0.20)

#north 
card_n1 = pygame.image.load(Deck[6].get_image()).convert_alpha()
card_n1 = pygame.transform.scale_by(card_n1, 0.20)
card_n2 = pygame.image.load(Deck[7].get_image()).convert_alpha()
card_n2 = pygame.transform.scale_by(card_n2, 0.20)

#dealer
card_d1 = pygame.image.load(Deck[8].get_image()).convert_alpha()
card_d1 = pygame.transform.scale(card_d1, (int(card_d1.get_width() * 0.20), int(card_d1.get_height() * 0.20)))
card_d2 = pygame.image.load(Deck[9].get_image()).convert_alpha()
card_d2 = pygame.transform.scale(card_d2, (int(card_d2.get_width() * 0.20), int(card_d2.get_height() * 0.20)))
card_d3 = pygame.image.load(Deck[10].get_image()).convert_alpha()
card_d3 = pygame.transform.scale(card_d3, (int(card_d3.get_width() * 0.20), int(card_d3.get_height() * 0.20)))
card_d4 = pygame.image.load(Deck[11].get_image()).convert_alpha()
card_d4 = pygame.transform.scale(card_d4, (int(card_d4.get_width() * 0.20), int(card_d4.get_height() * 0.20)))
card_d5 = pygame.image.load(Deck[12].get_image()).convert_alpha()
card_d5 = pygame.transform.scale(card_d5, (int(card_d5.get_width() * 0.20), int(card_d5.get_height() * 0.20)))




#if deck === to this, then asign value of one 

#check cards and follow if function for ranking system
#check of ranking system will go from lower to higher rating 
#Royal Flush	
#Straight Flush
#Four of a Kind
#Full House
#Flush
#Straight
#Three of a Kind
#Two Pair
#Pair
#High Card


show_backcard = True  # control wether if backcard is shown or not
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:        #button actions constructor 
            if button_menu.collidepoint(event.pos):
                pygame.quit()
                
        if event.type == pygame.MOUSEBUTTONDOWN:        #button actions constructor 
            if button_check.collidepoint(event.pos):
                print("HOLA CHECK :)")                        #action of button
        if event.type == pygame.MOUSEBUTTONDOWN:        #button actions constructor 
            if button_raise.collidepoint(event.pos):
                print("HOLA RAISE :)")  

                show_backcard == pygame.MOUSEBUTTONDOWN
        if event.type == pygame.MOUSEBUTTONDOWN:        #button actions constructor 
            if button_fold.collidepoint(event.pos):
                show_backcard = not show_backcard
                #this removes and adds the back card each time is pressed 
                #need to change so that it only removes the card when pressed 

 #COORDINATES OF SURFACES CARDS (position of cards)
    screen.blit(background_surface,(0,0))
    if show_backcard:
        screen.blit(backcard_surface, (100, 100))
        screen.blit(backcard_surface, (200, 200))

    screen.blit(card, (450, 430))
    screen.blit(card1, (555, 430))
   
    screen.blit(card_w1, (150, 250))
    screen.blit(card_w2, (180, 250))
    screen.blit(card_n1, (480, 25))
    screen.blit(card_n2, (520, 25))
    screen.blit(card_e1, (950, 250))
    screen.blit(card_e2, (980, 250))

    screen.blit(card_d1, (375, 250))
    screen.blit(card_d2, (475, 250))
    screen.blit(card_d3, (575, 250))
    screen.blit(card_d4, (675, 250))
    screen.blit(card_d5, (775, 250))

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


    
#if wanna play
    #then deal 2 cards for the players
    #if wanna keep playing then
        #then reveal 3 cards 
        #if not then reveal all cards
            #second round begins and after, deal another card
            #append that card to the dictionary 