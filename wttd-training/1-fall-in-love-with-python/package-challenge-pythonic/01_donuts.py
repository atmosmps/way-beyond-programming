"""
01. donuts

Dado um contador inteiro do numero de donuts, retorne uma string
com o formato 'Number of donuts: <count>' onde <count> é o numero
recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many'
ao invés do contador.
Exemplo: donuts(5) retorna 'Number of donuts: 5'
e donuts(23) retorna 'Number of donuts: many'
"""


def donuts_solution_1(count):
    message = 'Number of donuts: {}'
    value = 'many' if count >= 10 else count
    return message.format(value)


def donuts_solution_2(count):
    value = 'many' if count >= 10 else count
    return 'Number of donuts: {}'.format(value)


def donuts_solution_3(count):
    return 'Number of donuts: {}'.format(count) if count < 10 else 'Number of donuts: many'  # noqa


def donuts_solution_4(count):
    message = 'Number of donuts: {}'
    return message.format(count) if count < 10 else message.format('many')


def donuts_solution_5(count):
    return f'Number of donuts: {count if count < 10 else "many"}'


def donuts(count):
    message = 'Number of donuts: {}'
    value = 'many' if count >= 10 else count

    if value == 'many':
        return message.format(value)

    return message.format(value)

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
    test(donuts, 4, 'Number of donuts: 4')
    test(donuts, 9, 'Number of donuts: 9')
    test(donuts, 10, 'Number of donuts: many')
    test(donuts, 99, 'Number of donuts: many')

    test(donuts_solution_1, 4, 'Number of donuts: 4')
    test(donuts_solution_1, 9, 'Number of donuts: 9')
    test(donuts_solution_1, 10, 'Number of donuts: many')
    test(donuts_solution_1, 99, 'Number of donuts: many')

    test(donuts_solution_2, 4, 'Number of donuts: 4')
    test(donuts_solution_2, 9, 'Number of donuts: 9')
    test(donuts_solution_2, 10, 'Number of donuts: many')
    test(donuts_solution_2, 99, 'Number of donuts: many')

    test(donuts_solution_3, 4, 'Number of donuts: 4')
    test(donuts_solution_3, 9, 'Number of donuts: 9')
    test(donuts_solution_3, 10, 'Number of donuts: many')
    test(donuts_solution_3, 99, 'Number of donuts: many')

    test(donuts_solution_4, 4, 'Number of donuts: 4')
    test(donuts_solution_4, 9, 'Number of donuts: 9')
    test(donuts_solution_4, 10, 'Number of donuts: many')
    test(donuts_solution_4, 99, 'Number of donuts: many')

    test(donuts_solution_5, 4, 'Number of donuts: 4')
    test(donuts_solution_5, 9, 'Number of donuts: 9')
    test(donuts_solution_5, 10, 'Number of donuts: many')
    test(donuts_solution_5, 99, 'Number of donuts: many')
