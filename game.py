# game.py
# 
# implements the logic of the game
# #

import player, dealer

class Game:
    def __init__(self, dealer, players=[]):
        self.dealer = dealer
        self.players_playing = players
        self.busted_players = []
        self.standing_players = []