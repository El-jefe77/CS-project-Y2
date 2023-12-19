import random

#THIS SECTION CONTAINS THE CREATION OF THE DECK, AND DEAL OF TWO CARDS TO EACH PLAYER 

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 
        
        #prints cards
    def final_card(self):
        print("{} of {}".format(self.value, self.suit))

#deck of cards

class Deck:
    def __init__(self): #self is used to define a method in a class
        self.cards = [] #initialize attribute called cards (is an attribute of deck, "contains class called cards" initializes an empty list of ".cards" each deck will have their own cards)
        self.create()   #self.build is a method call within the constructor, creates the deck
 
    def create(self):   #calls the METHOD create ("method is a function")
        #THIS GENERATES A LIST OF CARD FOR ALL COMBINATIONS OF CARDS AND STORES THEM IN SELF.CARDS
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

#suffle cards (deck)
    def shuffle(self):
        random.shuffle(self.cards)

#checks if there is at least two cards 
    def deal(self):
        if len(self.cards) >= 2: #checks if there is enough cards in the deck
            return [self.cards.pop()] #controls the number of cards given to each player (add more cards  , self.cards.pop())
        else:
            print("Not enough cards to deal.")

# Constants
SUITS = ['C', 'S', 'H', 'D']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = Deck()
deck.shuffle()

first = deck.deal()
second = deck.deal()

#outputs the combination of cards (does not prints them)
#first two cards for player one
for card in first:
    card.final_card()

for card in second: 
    card.final_card()




#give 2 random cards to the user 
#if raise, then / increase bet 
#if check, then / not raise
#if call, then  / raise to required amount 
#if fold then   /surrender 



#random_suit = random.choice(SUITS)
#random_ranks = random.choice(RANKS)

#print(random_suit, random_ranks)




#shuffle/ build/ random functions 

#use shuffle function to make a deck of cards   
#select first card to user, second to n player and third to table 
              

#to test the classes (outputs the value and suit of the card)
#card = Card("Clubs", 6)
#card.show()
