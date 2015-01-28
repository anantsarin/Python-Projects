# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
open_card = True
busted = False
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def back_card(self, canvas, pos):
        
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                          [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]],
                          CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
            # create Hand object
        self.hand = []

    def __str__(self):
        string = ""
        for i in self.hand:
            string = string + str(i) + " "
        return "Hand contains " + string	# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        count = 0
        a_count =0
        for i in self.hand:
            count +=VALUES[i.get_rank()]
            if i.get_rank() == 'A':
                a_count +=1
        if a_count >=1 :
            if (count + 10) <= 21:
                count +=10
        return count
    def draw(self, canvas, pos):
        counter = 1
        for i in self.hand:
            i.draw(canvas,[pos[0]*counter,pos[1]])
            counter +=1
    
    def back_card(self, canvas, pos):
        self.hand[0].back_card(canvas,pos)
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i,j))
    
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)
        
    def deal_card(self):
        card=self.deck[0]
        self.deck.pop(0)
        return card# deal a card object from the deck
        
            
    def __str__(self):
        string = ""
        for i in self.deck:
            string = string + str(i) + " "
        return "Deck contains " + string #return self.deck	# return a string representing the deck
        
############################
deck = Deck()
dealer_cards = Hand()
players_cards = Hand()
#############################3
#define event handlers for buttons
def deal():
    global outcome,busted,deck,open_card, in_play ,RANKS ,SUITS,dealer_cards , players_cards
    open_card = True
    deck = Deck()
    dealer_cards = Hand()
    players_cards = Hand()
    deck.shuffle()
    #create object of player and dealer hand 
    outcome = ""
    busted = False
    
    # deal
    dealer_cards.add_card(deck.deal_card())
    players_cards.add_card( deck.deal_card())
    dealer_cards.add_card(deck.deal_card())
    players_cards.add_card( deck.deal_card())
    
   
    print dealer_cards
    print players_cards    
    
    players_cards.get_value()
    dealer_cards.get_value()
    
    #dealer_cards.add_card(random.choice(RANKS),random.choice(SUITS))
    #print dealer_cards
    # your code goes here
    in_play = True
    print "done"

def hit():
    
        # replace with your code below
    global in_play, score, outcome, open_card, busted
    #print players_cards 
    if in_play:
        players_cards.add_card( deck.deal_card())
        in_play = False
    if players_cards.get_value() >21:
        score -= 1
        outcome = "You are Busted"
        busted = True
    
            
    print players_cards         
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
    in_play = True   

    
    
def stand():
    global busted, in_play, score, open_card, outcome
    if not busted :
        if in_play:
            open_card = False
            while dealer_cards.get_value()<= 17:
                dealer_cards.add_card(deck.deal_card())
                if dealer_cards.get_value()>21:
                    outcome = "Dealer is Busted, You Won"
                    score +=1
                    return
                in_play = False
            if dealer_cards.get_value()>=players_cards.get_value():
                outcome="You Lose"
                score -= 1 
    else:
        outcome = "You are Busted :( "
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    in_play = True
    print "D="
    print dealer_cards

    
    
    
# draw handler    
def draw(canvas):
    global outcome
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Dealer :', (100, 90), 35, 'Yellow')
    canvas.draw_text('Player :', (100, 290), 35, 'Yellow')
    
    canvas.draw_text('Score '+str(score), (780, 40), 40, 'Yellow')
    canvas.draw_text('BLACK JACK', (400, 50), 40, 'Red')
    
    canvas.draw_text(outcome, (250, 500), 40, 'Yellow')
    dealer_cards.draw(canvas, [100, 100])
    if open_card:
        dealer_cards.back_card(canvas, [100, 100])
    players_cards.draw(canvas, [100, 300])
    if in_play:
        canvas.draw_text('Hit Or Deal ?', (300, 290), 30, 'Yellow')
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 1000, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

deal()
frame.start()
# remember to review the gradic rubric