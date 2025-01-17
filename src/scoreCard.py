
class ScoreCard:

    def __init__(self, score_card):
        self.pins = score_card
        self.score = 0 #puntaje
        self.frame = 10 #turnos
        self.rolls = list(self.pins) #bolos tumbados ¿podemos convertir la lanzada en una lista para manejar cada lanzamiento por separado?
        self.intentos = 0 #cambiar nombre

    def get_pins(self):
        return self.pins
    
    def total_score(self, pins):
        for pin in pins:
            int(pin)
            total = sum(pin)
            return total