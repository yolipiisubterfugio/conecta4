from juego_functions import tablero
from juego_functions import juega

def test_crear_tablero():
    tab = tablero(4,3)
    assert tab == [["__", "__", "__", "__"],["__", "__", "__", "__"],["__", "__", "__", "__"]]
def test_anyadir_ficha_a_tablero():
    tab = tablero(4,3)
    
    juega(tab, 2, 'x')
    assert tab == [
        ["__", "__", "__", "__"],
        ["__", "__", "__", "__"],
        ["__", "__", "__", 'x']
    ]
    
    juega(tab, 2, 'x')
    assert tab == [
        ["__", "__", "__", "__"],
        ["__", "__", "__", "__"],
        ["__", "__", "__", 'x']
    ]
    
def test_comprobar_columna_llena():
    tab = tablero(4,3)
    juega(tab, 2, 'x')
    juega(tab, 2, 'x')                   
    juega(tab, 2, 'x')    
    juega(tab, 2, 'x')
    
    assert test_comprobar_columna_llena(tab, 2) == True
