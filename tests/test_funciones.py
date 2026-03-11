from src.funciones import promedio_notas

def test_promedio_lista_vacia():
    assert promedio_notas([]) == 0

def test_promedio_notas_validas():
    assert promedio_notas([3,4,5]) == 4

def test_promedio_rango():
    assert promedio_notas([0,5]) == 2.5


