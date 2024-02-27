#creation and testing of the initial menu 
import pygame
import random
from sys import exit
pygame.init()

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
