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










