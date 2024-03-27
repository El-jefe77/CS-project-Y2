import pygame
import random
from sys import exit
from classes import Deck


#this function prints the whole random deck 
#check = (Deck[0])
#for x in Deck:
#    print(x)
#test iteration from card Deck[0] with the other 3 of the dealer
##check deck from limits in deck []``

##this fetch specific cards
#check = (Deck[7:11]) #11 is actually card[10]
#for card in check:
#    print(card.value)
   

VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']



#CALCULATOR OF HAND VALUES/ STRAIGHT 
def value_key(card):
    return VALUES.index(card.value)

def ordered_values(deck):
    check = deck[0:2] + deck[8:13]  

    ordered_values_values = sorted(check, key=value_key)
    ordered_values = [card.value for card in ordered_values_values]
    return ordered_values
ordered_values = ordered_values(Deck)

element_count = {}



# Count the occurrences of each element
for num in ordered_values:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1

# Calculate the number of pairs
n_pairs = sum(count // 2 for count in element_count.values())

print(f"Number of pairs in the list: {n_pairs}")