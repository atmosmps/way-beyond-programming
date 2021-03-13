"""
Regras do Fizzbuzz

1. Se a posição dor múltipla de 3: fizz
2. Se a posição dor múltipla de 5: buzz
3. Se a posição dor múltipla de 3 e 5: fizzbuzz
4. Para qualquer outra posição fale o próprio número
"""

"""
Quando acontece um AssertionError, significa que houve uma falha no teste.
Quando acontece um Erro de qualquer outro Tipo, significa que houve um problema
de código.
"""

FIZZ = 'fizz'
BUZZ = 'buzz'
FIZZBUZZ = 'fizzbuzz'


multiple_of = lambda base, num: num % base == 0


def robot(pos: int = None):
    say = str(pos)

    if multiple_of(base=3, num=pos) and multiple_of(base=5, num=pos):
        say = FIZZBUZZ
    elif multiple_of(base=3, num=pos):
        say = FIZZ
    elif multiple_of(base=5, num=pos):
        say = BUZZ

    return say


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
