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
    
    def get_umage(self):
        

    def print_card1(self):
        print(self.value, self.suit)


SUITS = ['C', 'S', 'H', 'D']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

#random generator 
n = 52
Deck = set()  # Initialize an empty set to store unique cards

while len(Deck) < n:  # Keep adding cards until the desired size is reached
    random_suit = random.choice(SUITS)
    random_value = random.choice(VALUES)
    card = (random_suit, random_value)  # Create a tuple representing the card

    if card not in Deck:  # Check if the card is not already in the deck
        Deck.add(card)  # Add the unique card to the deck



print(list(Deck)[0])
print(list(Deck)[0])
print(list(Deck)[1])
print(list(Deck)[2])




# Print the unique cards stored in the deck 
#for suit, value in Deck:
#   print(value, suit)
#---------------------------------------------------------------
#FETCH ONLY A CARD FROM THE DECK 






#print the fetched from the deck 
    #not working as it doesnt fetch from created deck 
#card = Card ("A", "S")
#card.print_card1( )

#child class because inherits its values from cards


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