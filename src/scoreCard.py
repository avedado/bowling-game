
class ScoreCard:

    def __init__(self, score_card):
        self.pins = score_card


    def get_pins(self):
        return self.pins
    
    def total_score(self, pins):
        for pin in pins:
            int(pin)
            total = sum(pin)
            return total