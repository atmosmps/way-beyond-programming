"""
03. fix_start

Dada uma string s, retorne uma string onde
todas as ocorrências do primeiro caracter de s
foram substituidas por '*', exceto a primeira.

Exemplo: 'babble' retorna 'ba**le'

Assuma que a string tem tamanho 1 ou maior.

Dica: s.replace(stra, strb) retorna uma versão da string s
onde todas as instancias de stra foram substituidas por strb.
"""


def replace_occurrence(
    sentence: str = None, occurrence: str = None, target: str = None
):
    if (sentence or occurrence or target) is None:
        return None

    sentence_list = []
    sentence_list[:0] = sentence

    for index, value in enumerate(sentence_list):
        if value == occurrence:
            sentence_list[index] = target

    result = "".join(sentence_list)
    return result


def fix_start_in_line(s):
    return s[0] + s.replace(s[0], "*")[1:]


def fix_start(s):
    return s[0] + replace_occurrence(s, s[0], "*")[1:]


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---


def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = "✅"
        info = ""
    else:
        sign = "❌"
        info = f"e o correto é {expected!r}"

    print(f"{sign} {f.__name__}({in_!r}) retornou {out!r} {info}")


if __name__ == "__main__":
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(fix_start_in_line, "babble", "ba**le")
    test(fix_start_in_line, "aardvark", "a*rdv*rk")
    test(fix_start_in_line, "google", "goo*le")
    test(fix_start_in_line, "donut", "donut")

    test(fix_start, "babble", "ba**le")
    test(fix_start, "aardvark", "a*rdv*rk")
    test(fix_start, "google", "goo*le")
    test(fix_start, "donut", "donut")
