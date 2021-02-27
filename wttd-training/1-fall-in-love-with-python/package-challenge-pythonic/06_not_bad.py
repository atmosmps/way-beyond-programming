"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""


def find_position(string: str, word: str):
    for i in range(len(string) - len(word) + 1):
        if string[i:i + len(word)] == word:
            return i

    raise ValueError


def not_bad(s):
    """
    REGULAR EXPRESSIONS RECOMMENDED

    Other Cases

    - not not bad
    - not bad not bad
    - bad not bad
    """

    find_position(s, 'not')

    # Solution 1
    to_replace = 'good'

    if not (('not' in s) and ('bad' in s)):
        return s

    if s.index('bad') < s.index('not'):
        return s

    if s.index('bad') > s.index('not'):
        pattern = s[s.index('not'):s.index('bad') + len('not')]
        return s.replace(pattern, to_replace)

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
