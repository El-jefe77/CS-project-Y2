import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 
        
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = [] #initializes an empty deck of cards 
        self.create() #populates the deck mmmm

    def create(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_two_cards(self):
        if len(self.cards) >= 2:
            return [self.cards.pop(), self.cards.pop()]
        else:
            print("Not enough cards to deal.")

# Constants
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Example usage
deck = Deck()
deck.shuffle()

player1_hand = deck.deal_two_cards()
player2_hand = deck.deal_two_cards()

print("Player 1's hand:")
for card in player1_hand:
    card.show()

print("\nPlayer 2's hand:")
for card in player2_hand:
    card.show()