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

Quando um AssertionError é lançado, ele interrompe a execução e não continua os
outros testes.
"""

"""
def assert_equal(result, expected):
    from sys import _getframe

    msg = "fail: line {} got {} expecting {}"

    if not result == expected:
        current = _getframe()
        caller = current.f_back
        line_no = caller.f_lineno
        print(msg.format(line_no, result, expected))


if __name__ == '__main__':
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(4), '4')

    assert_equal(robot(3), 'fizz')
    assert_equal(robot(6), 'fizz')
    assert_equal(robot(9), 'fizz')

    assert_equal(robot(5), 'buzz')
    assert_equal(robot(10), 'buzz')
    assert_equal(robot(20), 'buzz')

    assert_equal(robot(15), 'fizzbuzz')
    assert_equal(robot(30), 'fizzbuzz')
    assert_equal(robot(45), 'fizzbuzz')
"""

FIZZ = "fizz"
BUZZ = "buzz"
FIZZBUZZ = "fizzbuzz"


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
