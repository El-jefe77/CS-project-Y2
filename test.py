import random

SUITS = ['C', 'S', 'H', 'D']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

n = 52
Deck = set()  # Initialize an empty set to store unique cards

while len(Deck) < n:  # Keep adding cards until the desired size is reached
    random_suit = random.choice(SUITS)
    random_value = random.choice(VALUES)
    card = (random_suit, random_value)  # Create a tuple representing the card

    if card not in Deck:  # Check if the card is not already in the deck
        Deck.add(card)  # Add the unique card to the deck

# Print the unique cards in the deck
for suit, value in Deck:
    print(value, suit)

# Now Deck contains unique cards without any duplicates
