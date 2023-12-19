import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 
        
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = [] # initializes an empty deck of cards 
        self.create() # populates the deck

    def create(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self, num_cards):
        if len(self.cards) >= num_cards:
            return [self.cards.pop() for _ in range(num_cards)]
        else:
            print("Not enough cards to deal.")
            return []

# Constants
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Example usage
deck = Deck()
deck.shuffle()

# Deal 3 cards to player 1 and 1 card to player 2
player1_hand = deck.deal_cards(1)
player2_hand = deck.deal_cards(1)

# Display hands
print("Player 1's hand:")
for card in player1_hand:
    card.show()

print("\nPlayer 2's hand:")
for card in player2_hand:
    card.show()
