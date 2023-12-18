greeting = "hello world"
print(greeting)


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 

    def show(self):
        print("{} of {}".format(self.value, self.suit))








#to test the classes (outputs the value and suit of the card)
#card = Card("Clubs", 6)
#card.show()
