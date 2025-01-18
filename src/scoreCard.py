
class ScoreCard:

    def __init__(self, score_card):
        self.pins = score_card #lanzamientos

        self.score = 0 #puntaje
        self.frame = 10 #turnos
        self.intentos = 0 #cambiar nombre

    def get_pins(self):
        return self.pins
    
    def total_score(self):
      return sum(int(pin) for pin in self.pins)
         #separamos los lanzamientos y los convertimos
         #en números enteros para sumamos