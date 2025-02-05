
class ScoreCard:
    VALUE_X = 10
    VALUE_CERO = 0

    def __init__(self, score_card):
        self.pins = score_card #lanzamientos

    def get_pins(self):
        return self.pins
    
    def total_score(self):
        return sum(int(pin) for pin in self.pins)
         #separamos los lanzamientos y los convertimos
         #en números enteros para sumarlos

    def strike(self):
        for pin in self.pins:
            if pin == 'X':
                return 300
        # por cada pin en pins, si es igual a 'X' devuelve 300
        # es una función muy específica y solo está tomando el
        # primer valor
        
    def spares(self):
        self.score = 0
        for pin in self.pins:
            if pin == '/':
                continue
            elif pin == '5':
                self.score += 15
        return self.score
        # por cada pin en pins, si es igual a '/' continua
        # si es igual a '5' suma 15 al puntaje       

    def heartbreak(self):
        self.score = 0
        for pin in self.pins:
            if pin == '-':
                continue
            self.score += int(pin)
        return self.score
        # definiendo el puntaje en 0, por cada pin en pins
        # si es igual a '-' continua, si no suma el pin al puntaje
        # y devuelve el puntaje
        