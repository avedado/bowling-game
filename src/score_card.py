
class ScoreCard:

    def __init__(self, score_card):
        self.pins = score_card
        self.LAST_FRAME = 10
        self.frame = 1
        self.score = 0

    def get_pins(self):
        return self.pins
    
    def 