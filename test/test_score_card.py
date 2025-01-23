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
    assert card.total_score() == 60

#PERFECT GAME (12 STRIKES)
def test_strike():
    PINS = '2222XXXXXXX-2'
    card = ScoreCard(PINS)
    assert card.strike() == 192

#FRAMES SPARES (10 PINES EN LOS DOS INTENTOS DEL FRAME)
def test_spares():
    PINS = '5/5/5/5/5/5/5/5/5/5/'
    card = ScoreCard(PINS)
    assert card.spares() == 150      

#DESAMOR 9 PINES POR FRAME
def test_heartbreak():
    PINS = '9-9-9-9-9-9-9-9-9-9-'
    card = ScoreCard(PINS)
    assert card.heartbreak() == 90