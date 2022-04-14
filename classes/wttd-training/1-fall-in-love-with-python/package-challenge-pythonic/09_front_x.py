"""
09. front_x

Dada uma lista de strings, retorne a lista com as strings
ordenadas, porém agrupe todas as strings que começam com 'x' primeiro.

Exemplo: ['mix', 'banana' ,'xyz', 'apple', 'xanadu', 'aardvark']
Irá retornar: ['xanadu', 'xyz', 'aardvark', 'apple', 'banana' ,'mix']

Dica: Isso pode ser resolvido criando 2 listas e ordenando cada uma
antes de combina-las.
"""


# def front_x_list_comprehension(words):
def front_x(words):
    # result = sorted(words, key=lambda kv: kv[0])

    words.sort(reverse=True, key=lambda kv: kv[0] + kv[1])
    x_list = []
    no_x_list = []
    for i in words:
        if i[0:1] is 'x':
            x_list.append(i)
        else:
            no_x_list.append(i)
    return x_list + no_x_list

    # ----
    # x_list = []
    # no_x_list = []
    # for i in words:
    #     if i[0:1] is 'x':
    #         x_list.append(i)
    #     else:
    #         no_x_list.append(i)
    # x_list.sort()
    # no_x_list.sort()
    # return x_list + no_x_list


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
    test(front_x, ['bbb', 'ccc', 'axx', 'xzz', 'xaa'], ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])  # noqa
    test(front_x, ['ccc', 'bbb', 'aaa', 'xcc', 'xaa'], ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])  # noqa
    test(front_x, ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'], ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])  # noqa
