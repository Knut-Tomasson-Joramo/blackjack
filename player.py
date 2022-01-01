# player.py
#
# this is the player class
#


class Player:

    player_count = 0

    def __init__(self,  player_name=""):
        # set the id of the player
        Player.player_count += 1
        self.player_id = Player.player_count

        # make sure player has a name
        name_holder = player_name.strip()
        self.player_name = ""
        if(name_holder == ""):
            self.player_name = "Unknown player nr.{}".format(self.player_id)
        else:
            self.player_name = player_name

        # set other variables
        self.player_score = 0
        self.player_bust = False
        self.player_still_playing = True
    
    def bust(self):
        self.player_bust = True

    def score(self):
        return self.player_score

    def hit(self, card):
        self.player_score += card

    def get_name(self):
        return self.player_name

