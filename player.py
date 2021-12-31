#
#
# this is the player class
#

class Player:

    player_count = 0

    def __init__(self,  player_name=""):
        Player.player_count += 1
        self.player_id = Player.player_count
        