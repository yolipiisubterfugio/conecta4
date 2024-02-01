from juego_fucntions import tablero
from juego_fucntions import juega

def test_crear_tablero():
    tab = tablero(4,3)
    assert tab == [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
def test_anyadir_ficha_a_tablero():
    tab = tablero(4,3)
    
    juega(tab, 2, 1)
    assert tab == [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 1]]
    
    juega(tab, 2, 2)
    assert tab == [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 1]]
                   
    

