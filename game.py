# game.py
# 
# implements the logic of the game
# #

from player import Player
from dealer import Dealer

class Game:
    def __init__(self, players=[]):
        self.dealer = Dealer()
        self.players_playing = players
        self.busted_players = []
        self.standing_players = []

    def add_player(self, player):
        print("Pleas write player name or exit to abort:")
        name = input()
        if name != "exit":
            self.players_playing.append(Player(name))


    def run(self):
        pass