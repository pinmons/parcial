from notas import maxima_nota

def test_lista_vacia():
    assert maxima_nota([]) == 0

def test_notas_validas():
    assert maxima_nota([3,4,5,2]) == 5

def test_rango_notas():
    assert maxima_nota([0,5,3]) == 5

