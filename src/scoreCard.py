
class ScoreCard:
    VALUE_X = 10
    VALUE_CERO = 0

    def __init__(self, score_card):
        self.pins = score_card #lanzamientos

        '''self.score = 0 #puntaje
        self.frame = 10 #turnos
        self.intentos = 0 #cambiar nombre'''

    def get_pins(self):
        return self.pins
    
    def total_score(self):
      return sum(int(pin) for pin in self.pins)
         #separamos los lanzamientos y los convertimos
         #en números enteros para sumarlos

    def strike(self):
        self.score = 0
        for pin in self.pins:
            if pin == 'X':
                self.score += int(ScoreCard.VALUE_X)
            elif pin == '-':
                continue
            else:
                self.score += int(pin)
        return self.score

    def spares(self):
        frame_spares = list()
        for pin in self.pins:
            if pin == '5':
                frame_spares.append(pin)
            elif pin == '/':
                frame_spares.append(pin)
                return 150
        #por cada pin en pins, si es igual a '5'
        #agregalo a la lista, si el igual a '/'
        #tambien y devuelve 150.
        #es una función muy específica

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
