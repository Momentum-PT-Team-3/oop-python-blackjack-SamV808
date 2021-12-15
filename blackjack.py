# Write your blackjack game here.
# This assignment is based on the card game blackjack (also called 21). If you are unfamiliar with the game, instructions can be found here.

# The main objective is to have a hand of cards whose sum is as close to 21 as possible without going over.
# This game will have two players, one dealer (computer) and one human.
# Reqirements
# Build a blackjack game using python between a player and a dealer.
# The dealer's play is dictated by the rules of the game, and the dealer goes first. The dealer "hits" (is dealt a card) until their hand total is 17 or greater, at which point they stay. The dealers cards are all visible to the player.
# The player then chooses whether to be hit or stay. The player may hit as many times as they want before staying, but if their hand totals over 21, they "bust" and lose.
# If you want to make the game work for multiple players, go for it.
# The deck is a standard 52 card deck with 4 suits. Face cards are worth 10. The Ace card can be worth 1 or 11.
# Use classes. One way to think about classes is that they are the nouns involved in what you are modeling, so Card, Deck, Player, Dealer, and Game are all nouns that could be classes.
# Give those classes methods. Think about the actions that happen to or are caused by these different elements. These choices are subjective and hard, and there is no one right way.
# Use your classes and methods to execute the gameplay. It is always a great idea to sketch and/or comment this out first before writing code.

# 0) Make A only be 1 for this first game version. TODO: handle 1 or 11 option later.
# 1) A) Crete a player and
#    B) dealer class. Each need a hand attribute.
# 2) create a card class: suit, rank
# 3) create a deck class, with cards. 52 total, 2-10, JQKA, in each suit
# 4) Shuffle and deal method for cards
# 5) Dealer play. Methods: hit, stay 
# 6) Player play. Methods: hit, stay
# 7) Determine who wins, loses. Need method for calculating value of hand

import random

SUITS = ["Diamonds", "Spades", "Clubs", "Hearts"]
SCORES = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10, "A":11}

class Player:
    def __init__(self):
        # self.name = input("What is your name? ")
        self.hand = []

    def show_hand(self):
        print("Player")
        for card in self.hand:
            print(card)
    def calculate_score(self):
        raw_score = sum(self.hand)
        for card in self.hand:
            if card.score == 11 and raw_score > 21:
                card.score = 1
                raw_score -= 10
        return raw_score
            

    def __str__(self):
        # return self.name
        return "Player"

class Dealer:
    def __init__(self):
        self.hand = []
            
    def __str__(self):
        return "Dealer"

    def calculate_score(self):
        raw_score = sum(self.hand)
        for card in self.hand:
            if card.score == 11 and raw_score > 21:
                card.score = 1
                raw_score -= 10
        return raw_score    

    def show_hand(self):
        print("dealer")
        for card in self.hand:
            print(card)

class Card:
    def __init__(self, suit, rank, score):
        self.suit = suit
        self.rank = rank
        self.score = score

    def __str__(self):
        return f'{self.rank} of {self.suit} {self.score}'

    def __radd__(self, other):
        return self.score + other

class Deck:
    def __init__(self, suits, scores):
        self.cards = []

        for suit in suits:
            for value in scores.keys():
                card = Card(suit, value, scores.get(value))
                self.cards.append(card)
    
    def show_cards(self):
        for card in self.cards:
            print(card)
    
    def card_draw(self):
        card_draw = random.choice(self.cards)
        self.cards.remove(card_draw)
        return card_draw

# game play
player = Player()
dealer = Dealer()

print(player, dealer)

suits = ["♥️", "♦️", "♠️", "♣️"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]





class Game:
    def __init__(self, suits, scores):
        self.player = Player()
        self.dealer = Dealer()
        self.gamedeck = Deck(suits, scores)

    def deal_card(self):
        for i in range(2):
            # causing input("what's your name?") to repeat twice cause of range(2): How to fix????
            self.dealer.hand.append(self.gamedeck.card_draw())
            self.player.hand.append(self.gamedeck.card_draw())
        self.dealer.show_hand()
        self.player.show_hand()

    def hit(self, person):
        """Adds card to player's hand"""
        person.hand.append(self.gamedeck.card_draw())
        person.show_hand()  
    
    def hit_or_stand(self):
        # Ask for input from person
        busted = False
        while not busted: 
            choice = input("Would you like to hit or stand? ").lower()
            if choice == "hit": 
                self.hit(self.player)
                busted = self.bust(self.player)
            elif choice == "stand" :
                break
            else: print("Try Again.")
                 
        


    def dealer_hit_stand(self):
        busted = False
        while not busted:
            if self.dealer.calculate_score() < 18:
                self.hit(self.dealer)
                busted = self.bust(self.dealer)
            else:
                break
        

    def bust(self, player):
        if player.calculate_score() > 21:
            print("BUST")
            return True
            
        else:
            return False
    
    def winner(self):
        player_score = self.player.calculate_score()
        dealer_score = self.dealer.calculate_score()
        self.player.show_hand()
        self.dealer.show_hand()
        if player_score <= 21:
            if player_score == dealer_score:
                print("Tie!")
                return
            if player_score > dealer_score or dealer_score > 21:
                print("Player Wins!")
                return
        if dealer_score <= 21 and dealer_score > player_score:
            print("Dealer Wins")  
            return 
        else:
            print("Both Bust!")
            
            
        # if player_score == 21 or player_score > dealer_score:
        #     print("Player Wins!")
        # elif dealer_score == 21 or dealer_score > player_score:
        #     print("Dealer Wins!")
        # elif dealer_score == player_score:
        #     print("Tie!")
        # else :
        #     print("Both Lose!")
    
playing = True
while playing:
    game = Game(SUITS, SCORES)
    game.deal_card()

    # game.hit(game.player)
    game.hit_or_stand()
    game.dealer_hit_stand()
    game.winner()
    choice = input("Do you want to play again? Y/N ").lower()
    while choice != "y" and choice != "n":
        print("Please enter Y or N")
        choice = input("Do you want to play again? Y/N ").lower()
    if choice == "n":
        playing = False 










