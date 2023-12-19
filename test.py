import random 
from classes import Card
from classes import Deck


def print_player_one_cards(player_one_cards):
    # Output the cards of player one
    for card in player_one_cards:
        card.final_card()
