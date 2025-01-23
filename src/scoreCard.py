
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

    # def strike(self):
    #     self.score = 0
    #     for pin in self.pins:
    #         if pin == 'X':
    #             self.score += int(ScoreCard.VALUE_X)
    #         elif pin == '-':
    #             continue
    #         else:
    #             self.score += int(pin)
    #     return self.score
        # por cada pin en pins, si es igual a 'X' devuelve 300
        # es una función muy específica y solo está tomando el
        # primer valor
        
    def strike(self):
        self.score = 0
        num_pins = len(self.pins)
        posicion = 0  

        while posicion < num_pins:
            pin = self.pins[posicion]

            if pin == 'X':  # Strike
                self.score += int(ScoreCard.VALUE_X)  # Sumar 10 puntos por el strike

                # Sumar las dos posiciones siguientes, si existen
                for points in range(1, 3):
                    if posicion + points < num_pins: # Verificar que exista la posición, points toma los valores 1 y 2 que son las posiciones siguientes
                        next_pin = self.pins[posicion + points] # Obtiene el siguiente pin que se va a sumar
                        if next_pin == 'X':
                            self.score += int(ScoreCard.VALUE_X) if points == 1 else 10 
                        elif next_pin.isdigit():
                            self.score += int(next_pin)
                posicion += 1
            else:
                self.score += int(pin) # Sumar el valor del pin actual si no es un strike
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
        #agregalo a la lista, si el igual a '/',
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
        