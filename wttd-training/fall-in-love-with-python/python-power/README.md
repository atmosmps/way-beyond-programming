# Notes

- Quando o Python executa um arquivo/módulo ele carrega o aquivo, ler o arquivo, gera os bytecodes e executa;

- No momento que eu faço um import, para ser usado em outro arquivo, ele tambem faz o carregamento do arquivo, executa ele e depois passa o controle para o módulo atual realizar a execução;

- O import não só processa o arquivo, como também executa o corpo do módulo e só depois passa o controle para o arquivo atual;

- Quando um modulo python é o entrypoint do programa, ponto de entrada, a *dunder* function `__name__` (que mostra a localização do módulo)é sobrescrita pra `__main__` ;

----------------------------------------------

O trecho de código abaixo:

```md
if __name__ == '__main__':
    pass
```

Nada mais é do que um teste para determinar se o arquivo sendo executado é um entrypoint ou um módulo. Ele verifica se o módulo atual é o entrypoint, se for, o `__name__` será igual a `__main__`;

----------------------------------------------

- No Python 3 toda string é unicode

```md
'asdf'.encode()

b'asdf' -> o "b" no começo indica que a string em questão são bytes;
```

----------------------------------------------

## Simplifique tudo com Sequências

### Tamanho de uma string

```md
name = 'asdf'
name[len(name)-1] -> 5
name - 1 -> 5
```

*slice* == fatia

```md
slice[0:4]        -> Pega do índice 0 até o indice 4, mas não inclui o indice 4;
name[1:len(nome)] -> retorna toda a string até a ultima;
nome[1:]          -> retorna toda a string até a ultima;
```

### Pega em passos(steps)

```md
name[start:stop:step] -> comeco, parada, passo(passo determina de aonde até aonde ve ser feito o slice);
name[1:3:2]           -> percorre de 1 a 3 de dois em dois;
```

----------------------------------------------

## Listas

- Strings no python, não são uma sequência de bytes em memória e sim objetos de alto nível que implementam toda complexidade do Unicode;

- Strings no python são imutáveis. Operações feitas em strings, não alteram a estrutura da string, mas geram novas strings a partir da primeira(original);

```md
name = 'asdf'

name.upper() -> 'asdf'
name         -> 'asdf'
```

```md
'\n'.join(['Qwert', 'Zxcv']) -> Qwert
                                Zxcv
```

```md
[] = listas são sequências mutáveis - é possvel alterar o valor/estado interno da string, alterando sua estrutura. Tanto é que após uma alteração no terminal por exemplo, uma lista não retorna nada pois seu estado original foi alterado.
```

*No python tudo é referência*

----------------------------------------------

## Tuplas

*O Python ama tuplas*

- Tuplas são sequências imutáveis, ou seja, cada alteração realizada nelas, vai gerar um novo objeto com os dados alterados;

- Quando eu faço uma atribuição de uma tupla para outra variável, ele faz a referência para o mesmo objeto, não criando um novo objeto. Diferente das listas;

- Muitas pessoas acham que o que determina uma tupla, são os parênteses, mas na verdade, são as vírgulas, parênteses não uasados para precedência de operadores;

- `('A',)` - aqui é a vírgula que cria a tupla, a vírgula indica a criação de uma tupla;

----------------------------------------------

## Dicionários

- Dicionários são hashmaps, armazenam pares de {chave: valor};

- Para acessar o índice/chave de um dicionário se usa `colchete['nome_do_indice']`;

- Dicts são objetos mutáveis;

```md
Atualizar um dict

d['nome'] = "Novo valor para o indice 'nome'"
```

```md
'asdf' in d          -> verifica se a chave está no dicionário;
'asdf' in d.values() -> verifica se o valor está no dicionário;
```

```md
Para acessar o valor de uma chave, usar o get();

d.get('name')
d.get('indece_do_dict', 'valor_padrao_caso_a_chave_nao_exista')
```

```md
Operações que retornam os valores como tuplas

d.keys()       - retorna as chaves do dict;
d.values()     - retorna os valores de dict;
d.items()      - retorna os pares em tuplas;
d.pop('chave') - deletar o valor e retorna ele;
```

- Para remover, usar comando `del`;

----------------------------------------------

## O Sistema de Tipos: Dinâmico e Forte

- É Dinâmico porque o tipo é identificado em tempo de execução;
- É forte porque o Python não modifica o tipo da variável em tempo de execução, isso tem que ser explicitado;

```md
- int('1') -> o python cria um NOVO objeto inteiro com base na string '1';
- str(1)   -> o python cria um NOVO objeto string  com base no inteiro 1;
```

- O python não converte um tipo em outro. O python não converte um tipo em outro em tempo de excução, por isso é forte;

- Interpolação: `'Olá, %s' % 'Asdf' -> 'Olá, Asdf'`;

----------------------------------------------

```md
- range()     -> função que armazena um intervalo de valores;
- enumerate() -> adiciona os indices a uma sequência(cadeia de caracteres);
- next()      -> return o próximo item;
```

```md
nome = 'QwertZxcv'

for i, c in enumerate(nome):
    print (i, c)
```

----------------------------------------------

## Faça mágica com atribuições inteligentes

```md
- *args    -> retornar uma tupla de valores, como argumentos posicionais em argumentos de função;
- **kwargs -> retona um dicionário quando passado para funções com parametros nomeados em funções;
```
