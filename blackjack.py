import random
from typing import Counter

# This adds colors to output.
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m{}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

SUITS = ["♥️", "♦️", "♠️", "♣️"]
SCORES = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10, "A":11}

print("Welcome To Sam's Casino!")


class Player:
    def __init__(self, name=input("What's Your Name? ")):
        self.name = name
        self.hand = []
        self.chips = 1000
        
    print("You have 1000 chips available to use today. \nIf you win your get double you bet back!")
    count_wins = 0
    win_streak = 0

    def betting(self):

        self.bet = int(input("How much do you want to bet today? "))
        prGreen("You've placed a bet of " + str(self.bet) + " Chips")
    

    def show_hand(self):
        prPurple(self.name)
        for card in self.hand:
            prYellow(card) 
        print(self.calculate_score())

    def calculate_score(self):
        raw_score = sum(self.hand)
        for card in self.hand:
            if card.score == 11 and raw_score > 21:
                card.score = 1
                raw_score -= 10
        return raw_score
            

    def __str__(self):
        # return self.name
        return player.name


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
        prCyan("dealer")
        for card in self.hand:
            prYellow(card)
        print(self.calculate_score())

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



suits = ["♥️", "♦️", "♠️", "♣️"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]



 # wins_count = 0


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
                print(player.name + " Hits")
                self.hit(self.player)
                busted = self.bust(self.player)
            elif choice == "stand" :
                print(player.name + " Stands")
                break
            else: print("Try Again.")
                 
        


    def dealer_hit_stand(self):
        busted = False
        while not busted:
            if self.dealer.calculate_score() < 17:
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
                print("You've Won " + str(player.count_wins) + " Times.")
                print("Your Win Streak: " + str(player.win_streak))
                print("You have", str(player.chips), "chips")
                return
            if player_score > dealer_score or dealer_score > 21:
                print("Player Wins!")
                player.chips += player.bet*2
                player.count_wins += 1
                player.win_streak += 1
                print("You've Won " + str(player.count_wins) + " Times.")
                print("Your Win Streak: " + str(player.win_streak))
                print("You have", str(player.chips), "chips")
                return
        if dealer_score <= 21 or dealer_score > player_score:
            print("Dealer Wins")  
            player.chips -= player.bet
            player.win_streak = 0
            print("You've Won " + str(player.count_wins) + " Times.")
            print("Your Win Streak: " + str(player.win_streak))
            print("You have", str(player.chips), "chips")
            return 
        else:
            print("Both Bust!")
            player.chips -= player.bet
            print("You've Won " + str(player.count_wins) + " Times.")
            player.win_streak = 0
            print("Your Win Streak: " + str(player.win_streak))
            print("You have", str(player.chips), "chips")
            
    
playing = True
while playing:
    game = Game(SUITS, SCORES)
    player.betting()
    game.deal_card()
    game.hit_or_stand()
    game.dealer_hit_stand()
    game.winner()
    choice = input("Do you want to play again? Y/N ").lower()
    while choice != "y" and choice != "n":
        print("Please enter Y or N")
        choice = input("Do you want to play again? Y/N ").lower()
    if choice == "n":
        playing = False 
 










