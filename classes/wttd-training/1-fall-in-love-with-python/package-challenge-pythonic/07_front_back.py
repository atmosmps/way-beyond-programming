from math import ceil

"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

"""
math.seal
usar o módulo para caucular o indice

Esta usando o calculo do a e b separadamente tem alguma coisa que eu posso fazer pra juntar isso?
"""


def split_characteres(a: str = None, b: str = None):
    lena = int((len(a) / 2))
    lenb = int((len(b) / 2))

    if ((len(a) % 2) == 0) and not ((len(b) % 2) == 0):
        result = split_even_odd_characteres(a=a, b=b, lena=lena, lenb=lenb)
    elif ((len(a) % 2) == 0) and ((len(b) % 2) == 0):
        result = split_even_characteres(a=a, b=b, lena=lena, lenb=lenb)
    else:
        result = split_odd_characteres(a=a, b=b, lena=lena, lenb=lenb)

    return result


def split_even_odd_characteres(
    a: str = None, b: str = None, lena: int = None, lenb: int = None
):
    stra = a[:lena], a[lena:]
    strb = b[:lenb + 1], b[lenb + 1:]

    return stra, strb


def split_even_characteres(
    a: str = None, b: str = None, lena: int = None, lenb: int = None
):
    stra = a[:lena], a[lena:]
    strb = b[:lenb], b[lenb:]

    return stra, strb


def split_odd_characteres(
    a: str = None, b: str = None, lena: int = None, lenb: int = None
):
    stra = a[:lena + 1], a[lena + 1:]
    strb = b[:lenb + 1], b[lenb + 1:]

    return stra, strb


def odd(string: str = None):
    return string[:int(len(string)/2)+1], string[(int(len(string)/2)+1):]


def pair(string: str = None):
    return string[:int(len(string)/2)], string[int(len(string)/2):]


def split_in_half_pair(string: str = None):
    return pair(string=string) if len(string) % 2 == 0 else odd(string=string)


def split_in_half_ceil(string: str):
    result = ceil(len(string)/2)
    return result


def lengths(a, b):
    return split_in_half_ceil(a), split_in_half_ceil(b)


def mark0(a, b):
    formatted_result = split_characteres(a, b)
    return formatted_result[0][0] + formatted_result[1][0] + formatted_result[0][1] + formatted_result[1][1]  # noqa


def mark1(a, b):
    formatted_result = split_characteres(a, b)
    # join() statement is more fast than using concatenation
    return ''.join([formatted_result[0][0], formatted_result[1][0], formatted_result[0][1], formatted_result[1][1]])  # noqa


def front_back_string_formatted(a, b):
    return mark0(a, b)


def front_back_string_join(a, b):
    return mark1(a, b)


def front_back_multiple_attribution(a, b):
    half_a, half_b = lengths(a, b)
    return ''.join([a[:half_a], b[:half_b], a[half_a:], b[half_b:]])


def front_back(a, b):
    front_a, back_a = split_in_half_pair(a)
    front_b, back_b = split_in_half_pair(b)
    return ''.join([front_a, front_b, back_a, back_b])

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')

    test(front_back_string_formatted, ('abcd', 'xy'), 'abxcdy')
    test(front_back_string_formatted, ('abcde', 'xyz'), 'abcxydez')
    test(front_back_string_formatted, ('Kitten', 'Donut'), 'KitDontenut')

    test(front_back_string_join, ('abcd', 'xy'), 'abxcdy')
    test(front_back_string_join, ('abcde', 'xyz'), 'abcxydez')
    test(front_back_string_join, ('Kitten', 'Donut'), 'KitDontenut')

    test(front_back_multiple_attribution, ('abcd', 'xy'), 'abxcdy')
    test(front_back_multiple_attribution, ('abcde', 'xyz'), 'abcxydez')
    test(front_back_multiple_attribution, ('Kitten', 'Donut'), 'KitDontenut')
