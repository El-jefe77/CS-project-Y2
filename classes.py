#creation and testing of the initial menu 
import pygame
import random
from sys import exit
pygame.init()

#this is an example of the use of polymorphism due to the 
#use of many forms of the same thing / same family

#card and card1 are given to the players 
#card2 and card3 given to table and rest to the other players 

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
Deck = set()  # Initialize an empty set to store unique cards

while len(Deck) < n:  # Keep adding cards until the desired size is reached
    random_suit = random.choice(SUITS)
    random_value = random.choice(VALUES)
    card = Card (random_value, random_suit)  # Create a tuple representing the card

    if card not in Deck:  # Check if the card is not already in the deck
        Deck.add(card)  # Add the unique card to the deck




