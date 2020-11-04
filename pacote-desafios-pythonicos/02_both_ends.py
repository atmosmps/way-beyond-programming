"""
02. both_ends

Dada uma string s, retorne uma string feita com os dois primeiros
e os dois ultimos caracteres da string original.
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
for menor que 2, retorne uma string vazia.
"""


def both_ends(s):
    # Solution 1
    # return '' if len(s) < 2 else s[:2] + s[-2:]

    # Solution 2
    # length = len(s)
    # first = s[:2]
    # last = s[-2:]
    #
    # if length < 2:
    #     return ''
    #
    # return first + last

    # Solution 3
    is_one_word_str = isinstance(s, str) and len(s.split()) == 1
    output = []
    if is_one_word_str:
        slength = len(s)
        if slength > 1:
            count = 0
            first_part, last_part = [], []
            while count < slength:
                if count < 2:
                    first_part.append(s[count])
                if count > (slength - 3):
                    last_part.append(s[count])
                count += 1
            output.extend([*first_part, *last_part])

    return ''.join(output)


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
    test(both_ends, 'spring', 'spng')
    test(both_ends, 'Hello', 'Helo')
    test(both_ends, 'a', '')
    test(both_ends, 'xyz', 'xyyz')
