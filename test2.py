import pygame
import random
from sys import exit
from classes import Deck

print(Deck[9])


if Deck[10] == Deck[9]:  # Checks if they are pair 
    print("yes they are pair")
elif Deck[10] == Deck[10] and Deck[10] == Deck[10]:  # Compares cards to check if they are triple
    print("they are triple pair")
else:
    print("no they are not")

#we ned to return the self.value of the card to check if pair 