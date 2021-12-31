#
#
# this is the player class
#

class Player:

    player_count = 0

    def __init__(self,  player_name=""):
        Player.player_count += 1
        self.player_id = Player.player_count
        name_holder = player_name.strip()
        self.player_name = ""
        if(name_holder == ""):
            self.player_name = "Unknown player nr.{}".format(self.player_id)
        else:
            self.player_name = player_name

