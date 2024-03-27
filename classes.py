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
        
    def __str__(self):
        return self.value + self.suit
#new changes


SUITS = ['C', 'S', 'H', 'D']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

#random generator 
n = 52
Deck = []

for suit in SUITS:
    for value in VALUES:
        Deck.append(Card(value, suit))

#        print(value, suit) this function prints the whole deck but in order 
random.shuffle(Deck)


#THIS FETCHES SPECIFIC CARDS FROM THE DECK AND WRITES THEM IN NUMERICAL ORDE
#FOLLOWING THE ORDER OF "VALUES"
def value_key(card):
    return VALUES.index(card.value) #only return .value of card n 

def ordered_values(deck):
    check = deck[0:2] + deck[8:13]  # specific n of the cards in list

    ordered_values_values = sorted(check, key=value_key)
    ordered_values = [card.value for card in ordered_values_values]
    return ordered_values
ordered_values = ordered_values(Deck)
def count_pairs_and_triplets(ordered_values):

#---------------working code from .test
    # Initialize a dictionary
    element_count = {}

    # Count how many times each value appears
    for num in ordered_values:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    # Calculate the number of pairs
    n_pairs = sum(count // 2 for count in element_count.values())
    
    # Calculate the number of triplets
    total_triplets = sum(count // 3 for count in element_count.values())

    return n_pairs, total_triplets


# Call the function agani
pairs, triplets = count_pairs_and_triplets(ordered_values)

# Print the results
print("Number of pairs:", pairs)
print("Number of triplets:", triplets)