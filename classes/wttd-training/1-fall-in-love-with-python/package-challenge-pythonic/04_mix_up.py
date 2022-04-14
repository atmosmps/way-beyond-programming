"""
04. mix_up

Dadas as strings a e b, retorne uma string com a e b separados
por um espaço '<a> <b>', além disso, troque os 2 primeiros caracteres
das duas strings.

Exemplo:
    'mix', 'pod' -> 'pox mid'
    'dog, 'dinner' -> 'dig donner'

Old rule: Assuma que a e b tem tamanho 2 ou maior.
New rule: Assuma que a e b são strings não vazias e não Nulas.
"""


def mix_up_slice(a, b):
    mix_first_a = a.replace(a[:2], b[:2])
    mix_first_b = b.replace(b[:2], a[:2])

    mix_up_slice = '{} {}'.format(mix_first_a, mix_first_b)
    return mix_up_slice


def mix_up_in_line(a, b):
    return '{} {}'.format(a.replace(a[:2], b[:2]), b.replace(b[:2], a[:2]))


def mix_up(a, b):
    return (
        ''.join(
            'Ambas as strings estão vazias ou são Nulas, ou apenas uma delas está vazia, ou é nula.'  # noqa
        ) if (
                ((a == '') or (b == '')) or ((a is None) or (b is None))
        ) else ' '.join((a.replace(a[0:2], b[:2]), b.replace(b[0:2], a[:2])))
    )


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
    test(mix_up, ('mix', 'pod'), 'pox mid')
    test(mix_up, ('dog', 'dinner'), 'dig donner')
    test(mix_up, ('gnash', 'sport'), 'spash gnort')
    test(mix_up, ('pezzy', 'firm'), 'fizzy perm')
    test(mix_up, ('a', 't'), 't a')
    test(mix_up, ('at', 'm'), 'm at')
    test(mix_up, ('a', 'tm'), 'tm a')
    test(mix_up, ('', ''), 'Ambas as strings estão vazias ou são Nulas, ou apenas uma delas está vazia, ou é nula.')  # noqa
    test(mix_up, ('a', ''), 'Ambas as strings estão vazias ou são Nulas, ou apenas uma delas está vazia, ou é nula.')  # noqa
    test(mix_up, ('', 't'), 'Ambas as strings estão vazias ou são Nulas, ou apenas uma delas está vazia, ou é nula.')  # noqa
    test(mix_up, (None, None), 'Ambas as strings estão vazias ou são Nulas, ou apenas uma delas está vazia, ou é nula.')  # noqa

    test(mix_up_slice, ('mix', 'pod'), 'pox mid')
    test(mix_up_slice, ('dog', 'dinner'), 'dig donner')
    test(mix_up_slice, ('gnash', 'sport'), 'spash gnort')
    test(mix_up_slice, ('pezzy', 'firm'), 'fizzy perm')
    test(mix_up_slice, ('a', 't'), 't a')
    test(mix_up_slice, ('at', 'm'), 'm at')
    test(mix_up_slice, ('a', 'tm'), 'tm a')

    test(mix_up_in_line, ('mix', 'pod'), 'pox mid')
    test(mix_up_in_line, ('dog', 'dinner'), 'dig donner')
    test(mix_up_in_line, ('gnash', 'sport'), 'spash gnort')
    test(mix_up_in_line, ('pezzy', 'firm'), 'fizzy perm')
    test(mix_up_in_line, ('a', 't'), 't a')
    test(mix_up_in_line, ('at', 'm'), 'm at')
    test(mix_up_in_line, ('a', 'tm'), 'tm a')
