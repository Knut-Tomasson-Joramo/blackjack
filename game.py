# game.py
# 
# implements the logic of the game
# #

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

    def add_player(self, player):
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
            else:
                return None


    def play_game(self):
        print("Hello players!")
        print("Lets play blackjack.")
        
        while len(self.players_playing) > 0:
            counter = 0
            to_standing = []
            to_busted = []
            for player in self.players_playing:
                print("Hello {}".format(player.get_name()))
                print("your score is {}".format(player.score()))
                print("choose one option")
                print("1. hit")
                print("2. stand")
                the_gamble = input()
                if the_gamble == "1":
                    player.hit(self.deck.get_card())
                    print("your score is now {}".format(player.score()))
                else:
                    to_standing.append(counter)                
                if player.score() > 21:
                    print("You're out!")
                    to_busted.append(counter)
                
                counter += 1
            for stand in to_standing:
                self.standing_players.append(self.players_playing.pop(stand))
            for bust in to_busted:
                self.busted_players.append(self.players_playing.pop(bust))
        
        print("Dealers turn!")

        while self.dealer.score() < 17:            
            print("Dealer hits!")
            self.dealer.hit(self.deck.get_card())
            time.sleep(1)
            print("Dealers score is: {}".format(self.dealer.score()))

        if self.dealer.bust():
            for player in self.standing_players:
                print("{} you are a winner".format(player.get_name()))
        else:
            for player in self.standing_players:
                if player.score() > self.dealer.score():
                    print("{} you win!".format(player.get_name()))
                elif player.score() == self.dealer.score():
                    print("it's a tie for you {}".format(player.get_name()))
                else:
                    print("Sorry {} you loose..".format(player.get_name()))

        