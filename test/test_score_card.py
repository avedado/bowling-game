from src.scoreCard import ScoreCard

#OBJETO CREADO CORRECTAMENTE
def test_score_card():
    card = ScoreCard('12345123451234512345')
    assert card 

#TIRADAS ALMACENADAS CORRECTAMENTE
def test_frame_pins():
    PINS = '12345123451234512345'
    card = ScoreCard(PINS)
    assert card.get_pins() == PINS

#JUGADA SIMPLE (PUNTUACIÓN 60)
def test_total_score():
    PINS = '12345123451234512345'
    card = ScoreCard(PINS)
    assert 60 == card.total_score()  

#PERFECT GAME (12 STRIKES)       
def test_strike():
    PINS = 'XXXXXXXXXXXX'
    card = ScoreCard(PINS)
    assert 300 == card.strike()      

#FRAMES SPARES (10 PINES EN LOS DOS INTENTOS DEL FRAME)
def test_spares():
    PINS = '5/5/5/5/5/5/5/5/5/5/5'
    card = ScoreCard(PINS)
    assert 150 == card.spares()      

#DESAMOR 9 PINES POR FRAME
def test_heartbreak():
    PINS = '9-9-9-9-9-9-9-9-9-9-'  
    card = ScoreCard(PINS)
    assert card.heartbreak() == 90    