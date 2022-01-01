# game.py
# 
# implements the logic of the game
# #

from player import Player
from dealer import Dealer
from deck import Deck

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
            pass
        