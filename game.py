# game.py
# 
# implements the logic of the game
# #

import builtins
from player import Player
from dealer import Dealer
from deck import Deck
import time

class Game:
    def __init__(self, players=[]):
        self.dealer = Dealer()
        self.players_playing = players
        self.busted_players = []
        self.standing_players = []
        self.deck = Deck()

    def add_player(self):
        print("Pleas write player name or exit to abort:")
        name = input()
        if name != "exit":
            self.players_playing.append(Player(name))
    
    def start_menu(self):
        print("choose one option:")
        print("1. Add new player")
        print("2. Start the game")
        print("3. exit")

        return input()


    def run(self):
        print("Hello and welcome to this game of BlackJack!")
        if len(self.players_playing) == 0:
            print("We need to add some players!")
            self.add_player()
            if len(self.players_playing) == 0:
                return None

        while True:
            choice = self.start_menu()
            if choice == "1":
                self.add_player()
            elif choice == "2":
                self.play_game()
                print("play again? (yes or no)")
                again = input()
                if again.strip() == "no":
                    break
                self.reset()
            else:
                return None


    def play_game(self):
        print("Hello players!")
        print("Lets play blackjack.")

        to_standing = []
        to_busted = []
        
        while len(self.players_playing) > 0:
            counter = 0
            
            for player in self.players_playing:
                print()
                print("Hello {}".format(player.get_name()))
                print("your score is {}".format(player.score()))
                print("choose one option")
                print("1. hit")
                print("2. stand")
                the_gamble = input()
                if the_gamble == "1":
                    card = self.deck.get_card()
                    if card == 11:
                        print("You got an Ace! Choose 1 or 11:")
                        choice = input()
                        if choice.strip() == "1":
                            card = 1
                    player.hit(card)
                    print()
                    print("your score is now {}".format(player.score()))
                    print()
                else:
                    self.standing_players.append(player)  
                    self.players_playing.pop(counter)
                    counter -= 1              
                if player.score() > 21:
                    print("You're out!")
                    self.busted_players.append(player)
                    self.players_playing.pop(counter)
                    counter -= 1
                
                counter += 1

        print()
        print("Dealers turn!")
        while (self.dealer.get_score() < 17):            
            print("Dealer hits!")
            card = self.deck.get_card()
            if card == 11:
                if self.dealer.get_score() + card > 21:
                    card = 1
            self.dealer.hit(card)
            time.sleep(1)
            print("Dealers score is: {}".format(self.dealer.get_score()))

        print()
        if self.dealer.get_bust():
            for player in self.standing_players:
                print("{} you are a winner".format(player.get_name()))
        else:
            for player in self.standing_players:
                if player.score() > self.dealer.get_score():
                    print("{} you win!".format(player.get_name()))
                elif player.score() == self.dealer.get_score():
                    print("it's a tie for you {}".format(player.get_name()))
                else:
                    print("Sorry {} you loose..".format(player.get_name()))

    def reset(self):
        for player in self.busted_players:
            player.reset()
            self.players_playing.append(player)
        for player in self.standing_players:
            player.reset()
            self.players_playing.append(player)
        self.dealer.reset()
             
