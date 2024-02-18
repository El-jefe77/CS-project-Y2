import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 
        
        #prints cards
    def final_cards_p1(self):
        print("{} of {}".format(self.value, self.suit))

    def final_cards_p2(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self): #self is used to define a method in a class
        self.cards = [] #initialize attribute called cards (is an attribute of deck, "contains class called cards" initializes an empty list of ".cards" each deck will have their own cards)
        self.create()   #self.build is a method call within the constructor, creates the deck
 
    def create(self):   #calls the METHOD create ("method is a function")
        #THIS GENERATES A LIST OF CARD FOR ALL COMBINATIONS OF CARDS AND STORES THEM IN SELF.CARDS
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
            return [self.cards.pop() for _ in range(num_cards)] #controls the number of cards given to each player (add more cards  , self.cards.pop())

# Constants
SUITS = ['C', 'S', 'H', 'D']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = Deck()
deck.shuffle()

player_one = deck.deal(2)    #change the number of cards 
player_two = deck.deal(2)    #if you eliminate one of them you can only have player one or two 

#outputs the combination of cards (does not prints them)
#first two cards for player one
for card in player_one:
    card.final_cards_p1()

for card in player_two: 
    card.final_cards_p2()

