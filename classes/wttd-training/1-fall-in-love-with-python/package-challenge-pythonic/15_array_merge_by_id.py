"""
Dado duas listas [] de quaisquer tipo de valores,

una as listas de modo que o indice da primeira seja adicionado em uma lista
com o índice da segunda de maneira consecutiva.

exemplo:

lista_a = [1, 2, 3, 4, 5]
lista_b = ['a', 'b', 'c', 'd', 'e']

resultado esperado: [[1, 'a'], [2, 'b'], [3, 'c'], [4, 'd'], [5, 'e']]
"""


def zippy():
    x = [1, 2, 3, 4, 5]
    y = ["a", "b", "c", "d", "e"]
    zipper = []

    for i in range(len(x)):
        zipper.append([x[i], y[i]])
    print(zipper)

    # using list comprehension:
    # return [(x[i], y[i]) for i in range(len(x))]


def main():
    # Solution 1
    # list_a = [1, 2, 3, 4, 5]
    # list_b = ['a', 'b', 'c', 'd', 'e']
    #
    # print([[a, b] for a, b in zip(list_a, list_b)])

    zippy()


if __name__ == "__main__":
    main()
