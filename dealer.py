# dealer.py
# 
# dealer class
# 
# 

class Dealer:
    def __init__(self):
        self.score = 0
        self.bust = False

    def hit(self, score):
        self.score += score
        if self.score > 21:
            self.bust = True

    def get_bust(self):
        return self.bust

    def get_score(self):
        return self.score

    def reset(self):
        self.score = 0