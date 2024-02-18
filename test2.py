#creation and testing of the initial menu 
import pygame
import random
from sys import exit
pygame.init()


#this is an example of the use of polymorphism due to the 
#use of many forms of the same thing / same family

#parent class 
class Card:
    def __init__(self, value, suit):    #this is the constructor of the class
        self.value = value              #gives attribute to value 
        self.suit = suit                #gives attribute to suit 
    
    def print_card_p1(self):
        print("{} of {}".format(self.value, self.suit))

#child class because inherits its values from cards


SUITS = ['C', 'S', 'H', 'D']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']









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