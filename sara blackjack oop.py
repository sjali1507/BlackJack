import random #the random module is used to pick out random cards from the deck created
import time
from time import sleep
deck_suits=['Clubs', 'Spades', 'Diamonds', 'Hearts']
deck_ranks=['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Jack', 'Ace']
deck_values={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,
             'Ten':10, 'King':10, 'Queen':10, 'Jack':10, 'Ace':0}
            #dictionary used to store the vaules in key: value pairs

gameplaying=True #to keep the game running the variable gameplaying set as true



#Creation of class Card
class Card:
    
    def __init__(self, deck_rank, deck_suit):
        #self is used to refer to the arguments
        #init function is used to assign values to the class card's object properties
        self.deck_rank= deck_rank #setting the attributes to an assigned name
        self.deck_suit=deck_suit

    #def str is used to return the string object
    def __str__(self):
        return self.deck_rank+ " of " + self.deck_suit
        #this prints out the card- both value & rank


class DeckofCards:
    def __init__(self):
        
        self.deckcards=[] #an empty list ([] for list) for the deck is created 
        for deck_suit in deck_suits: #loops through the list containing the suit names
            #the loop checks that the deck suit name/val
            #loop for every type of suit

            #loop for every type of rank within a suit
            for deck_rank in deck_ranks:
                #another loop is created within the first loop that will loop through the ranks/values

                #the card is added to the deck
                self.deckcards.append(Card(deck_rank, deck_suit))
                
                #the Card(deck_suit, deck_rank) is appended to the self.deckcards list
                #this occurs within the second loop which will produce for eg Two of Diamonds
                #Each card is added to the cards attribute list

    
    def __str__(self): 
        deck=''
        for card in self.deckcards:
            deck +='\n ' + card.__str__()
        #this prints out the card- both value & rank

    def shuffle(self): #all the cards within the deck are shuffled using the random and shuffle
        random.shuffle(self.deckcards)

    def cardDrawn(self):
        #here we are drawing out the card from the shuffled deck. The cardDrawn method is created which calls in self.
        card_drawn=self.deckcards.pop()
        return card_drawn
        #this will remoe the last card from the top of the deck and return that card.
        #pop is used to remove.

class Hand:
    def __init__(self):
        self.cards=[] #an empty list to store the cards 
        self.value=0 #the total value 
        self.aces=0 #an ace tracker, helps later to identify if there are any aces

    def add_card(self, card): #purpose is to add a card to the player's or dealer's hand
        self.cards.append(card) #referring to the self.cards
        #append adds the item to the list
        self.value += deck_values[card.deck_rank]
        if card.deck_rank=='Ace':
            if self.value<11:
                self.value +=11
            else:
                self.value +=1

#Functions

def hit(deck, hand):
    #cards are taken from the deck
    #add to the hand
    
    hand.add_card(deck.cardDrawn())
   
 
   

def hit_orstand(deck, hand):
    global gameplaying
    while True:
        
        q=input("Would you like to hit or stand? Please enter hit or stand ")
        if q.lower()=="hit":
            hit(deck, hand) #call hit function
        elif q.lower()=="stand":
            print ("Player chooses to stand, so Dealer is playing.")
            sleep(1)
            gameplaying=False
        else:
            print("Sorry but please enter hit or stand. Try again")
            continue #to keep on asking the question
        break #once they have entered h or s

def show_somecards(player, dealer):
    print("Some cards of both the dealer and player are listed below: ")
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =" , player.value)
    print("\nDealer's Hand: ")
    print(" <card hidden>")
    print("", dealer.cards[1])
 
def show_all(player, dealer):
    print("The cards of both the dealer and player are listed below: ")
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand=" , player.value)
    print("\nDealer's Hand:" , *dealer.cards, sep="\n ")
    print("Dealer's Hand=" , dealer.value)

def player_busts(player, dealer):
    print("\n-- Player busts!--")
    show_all(player, dealer)
    
def player_wins(player, dealer):
    print("\n-- Player has blackjack! You win!--")
    show_all(player, dealer)
    
def dealer_busts(player, dealer):
    print("\n-- Dealer busts! You win!--")
    show_all(player, dealer)
    
    
def dealer_wins(player, dealer):
    print("\n-- Dealer wins!--")
    show_all(player, dealer)
    

def push(player, dealer):
    print("Its a push! Player and Dealer tie!")
    show_all(player, dealer)
    


#GAME

game = True #loop that runs the game
while game == True: #while game is true, run the game
    print("Welcome to a game of BlackJack!")

    #a shuffled deck is created
    deck=DeckofCards()
    deck.shuffle()

    player_hand=Hand()
    player_hand.add_card(deck.cardDrawn())
    player_hand.add_card(deck.cardDrawn())

    dealer_hand=Hand()
    dealer_hand.add_card(deck.cardDrawn())
    dealer_hand.add_card(deck.cardDrawn())

    show_somecards(player_hand, dealer_hand)
    while gameplaying:
        
        hit_orstand(deck, player_hand)
        show_somecards(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)
        else:
            push(player_hand, dealer_hand)
    ready_validation = True #loop that allows for validation to work
    while ready_validation == True: #while this validation is true, run the loop to validate input
        replay = input("Play again? Yes or No: ").upper()
        if replay == "YES" or replay == "Y":
            print()
            game = True
            ready_validation = False
            #because they typed yes the right way, the game is still going to run because the game loop is true and the validation stops because
            #the validation loop is true
        elif replay == "NO" or replay == "N":
            print("Thank you for playing")
            ready_validation = False
            game = False
        else:
            print()
        

