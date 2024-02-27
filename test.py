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



#parent class 
class Card:
    def __init__(self, value, suit):    #this is the constructor of the class
        self.value = value              #gives attribute to value 
        self.suit = suit                #gives attribute to suit 
    #prtin the cards for player 


    def get_image(self):                                #return from "print[lst]"
        return "cards img/" + str(self) + ".png"        #add value and suit to create path
    def print_card(self):                  
        print(self.value, self.suit)
    def get_image1(self):                                #return from "print[lst]"
        return "cards img/" + str(self) + ".png"        #add value and suit to create path
    def print_card1(self):                  
        print(self.value, self.suit) 

    def __str__(self):
        return self.value + self.suit



SUITS = ['C', 'S', 'H', 'D']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

#random generator 
n = 52
Deck = []

for suit in SUITS:
    for value in VALUES:
        Deck.append(Card(value, suit))
        print(value, suit)

random.shuffle(Deck)


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
card1 = pygame.image.load(Deck[1].get_image1()).convert_alpha()
card1 = pygame.transform.scale_by(card1, 0.20)

#west
card_w1 = pygame.image.load(Deck[2].get_image()).convert_alpha()
card_w1 = pygame.transform.scale_by(card_w1, 0.20)
card_w2 = pygame.image.load(Deck[3].get_image1()).convert_alpha()
card_w2 = pygame.transform.scale_by(card_w2, 0.20)

#east
card_e1 = pygame.image.load(Deck[4].get_image()).convert_alpha()
card_e1 = pygame.transform.scale_by(card_e1, 0.20)
card_e2 = pygame.image.load(Deck[5].get_image1()).convert_alpha()
card_e2 = pygame.transform.scale_by(card_e2, 0.20)

#north 
card_n1 = pygame.image.load(Deck[6].get_image()).convert_alpha()
card_n1 = pygame.transform.scale_by(card_n1, 0.20)
card_n2 = pygame.image.load(Deck[7].get_image1()).convert_alpha()
card_n2 = pygame.transform.scale_by(card_n2, 0.20)

#dealer
card_d1 = pygame.image.load(Deck[8].get_image()).convert_alpha()
card_d1 = pygame.transform.scale(card_d1, (int(card_d1.get_width() * 0.20), int(card_d1.get_height() * 0.20)))
card_d2 = pygame.image.load(Deck[9].get_image1()).convert_alpha()
card_d2 = pygame.transform.scale(card_d2, (int(card_d2.get_width() * 0.20), int(card_d2.get_height() * 0.20)))
card_d3 = pygame.image.load(Deck[10].get_image()).convert_alpha()
card_d3 = pygame.transform.scale(card_d3, (int(card_d3.get_width() * 0.20), int(card_d3.get_height() * 0.20)))


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


 #COORDINATES OF SURFACES CARDS (position of cards)
    screen.blit(background_surface,(0,0))

    screen.blit(card, (450, 430))
    screen.blit(card1, (555, 430))
   
    screen.blit(card_w1, (150, 250))
    screen.blit(card_w2, (180, 250))
    screen.blit(card_n1, (480, 25))
    screen.blit(card_n2, (520, 25))
    screen.blit(card_e1, (950, 250))
    screen.blit(card_e2, (980, 250))

    screen.blit(card_d1, (475, 250))
    screen.blit(card_d2, (575, 250))
    screen.blit(card_d3, (675, 250))

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