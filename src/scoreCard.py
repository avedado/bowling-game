
class ScoreCard:

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
        for pin in self.pins:
            pin == 'X'
            return 300
        #por cada pin en pins, si es igual a 'X' devuelve 300
        #es una función muy específica

    def spares(self):
        frame_spares = list()
        for pin in self.pins:
            if pin == '5':
                frame_spares.append(pin)
            elif pin == '/':
                frame_spares.append(pin)
                return 150
        #por cada pin en pins, si es igual a '5'
        #agregalo a la lista, si el igual a '/', 
        #tambien y devuelve 150.
        #es una función muy específica

    def heartbreak(self):
        frame_heartbreak = list()
        for pin in self.pins:
            if pin == '9':
                frame_heartbreak.append(pin)
            elif pin == '-':
                frame_heartbreak.append(pin)
                return 90
        #por cada pin en pins, si es igual a '9'
        #agregalo a la lista, si el igual a '-', 
        #tambien y devuelve 90.
        #es una función muy específica