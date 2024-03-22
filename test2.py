import pygame
import random
from sys import exit
from classes import Deck

print(Deck[9])

print(Deck[9].value)

#checking the player's hand 
if Deck[10].value == Deck[9].value:  # Checks if they are pair 
    print("yes they are pair")
elif Deck[10].value == Deck[10].value  and Deck[10].value == Deck[8].value:  # Compares cards to check if they are triple
    print("they are triple pair")
else:
    print("no they are not")

#checking for two pair 
if Deck[10].value == Deck[9].value and Deck[8].value == Deck[7].value:
    print("Yes, there are two pairs.")
elif Deck[10].value == Deck[9].value and Deck[6].value == Deck[5].value:
    print("Yes, there are two pairs.")
elif Deck[10].value == Deck[8].value and Deck[7].value == Deck[5].value:
    print("Yes, there are two pairs.")
else:
    print("No, there are not two pairs.")


#needs more work, create a looop that checks all teh cards at once, at the moment is checking double pairs in specific cards not all the possible double pairs in hte hand 
    #repeat process for the rest of functions 




#we ned to return the self.value of the card to check if pair 