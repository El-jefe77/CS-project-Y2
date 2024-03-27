import pygame
import random
from sys import exit
from classes import Deck

VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']



#CALCULATOR OF HAND VALUES/ STRAIGHT 
def value_key(card):
    return VALUES.index(card.value)

def ordered_values(deck):
    check = deck[0:2] + deck[8:13]  # Assuming deck is your array

    ordered_values_values = sorted(check, key=value_key)
    ordered_values = [card.value for card in ordered_values_values]
    return ordered_values
ordered_values = ordered_values(Deck)





def count_pairs_and_triplets(my_list):
    # Initialize a dictionary
    element_count = {}

    # Count how many times each value appears
    for num in my_list:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    # Calculate the number of pairs
    n_pairs = sum(count // 2 for count in element_count.values())
    
    # Calculate the number of triplets
    total_triplets = sum(count // 3 for count in element_count.values())

    return n_pairs, total_triplets

my_list = [0, 1, 2, 2, 4, 4, "A", "A"]

# Call the function
pairs, triplets = count_pairs_and_triplets(my_list)

# Print the results
print("Number of pairs:", pairs)
print("Number of triplets:", triplets)

