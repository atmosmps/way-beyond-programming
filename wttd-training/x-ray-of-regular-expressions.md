# Raio X das Expressões Regulares

É uma forma de encontrar e extrair padrões em textos;

`match` - busca um padrão a partir do inico de uma string
`search` - busca um padrão em qualquer parte da string
`findAll` - busca todas as ocorrencias dentro de uma string

## Metacaractere `"."`

Representa qualquer caractere.

### Metacaracteres de Ancoras(^, $)

Representam o inicio e o fim da string respectivamente.

```
findall('^.', 'abc\nefg\nhi')
->['a']

findall('^.', 'abc\nefg\nhi', re.MULTILINE)
-> ['a', 'n', 'h']

findall('.$', 'abc\nefg\nhi')
->['i']

findall('.$', 'abc\nefg\nhi', re.MULTILINE)
->['c', 'g', 'i']

'^.$' - reconhece qualquer texto com apenas um caractere
    match('^.$', 'a')

'^$' - esse padrão só funciona para strings vazias,
pois a unica forma de o inicio encontrar o final é sem nenum caractere entre eles.
    match('^$', '')

findall(^$, '\n', re.MULTILINE)
```

## Classes de Caracteres

[] - declaração de classes de caracteres é feita com colchetes.

```
Dentro da classe de caracteres, ele tenta filtrar para cada elemento de uma vez,
como se fosse uma série de 'ORs';

    findall('[aeiou]', 'Atmos Maciel')
    -> ['A', 'o', 'a', 'i', 'e']

Usando a classe de caracteres como negação, basta usar o "^" dentro dos colchetes,
somente dentro dos colchetes o caractere "^" tem sentido de negação.

    findall('[^aeiou]', 'Atmos Maciel')

Para usar ranges basta usar o hífen("-"),
vai filtrar por todos os caracteres estabelecidos dentro do range.

    findall('[a-f]', 'Atmos Maciel')  

Multiplus Ranges
    findall('[a-fA-Z]', 'Atmos Maciel')

findall('[a-zA-Z0-9]', 'Atmos Maciel')

[a-zA-Z0-9] - conjunto de caracteres aceitáveis em palavras
[a-zA-Z0-9] === \w
```

### Sequencias de caracteres especiais
    
    \d == [0-9]
    \D == [^0-9]
    \s == [\t\n\r\f\w]
    \S == [^\t\n\r\f\w]
    \w == [a-zA-Z0-9_]
    \W == [^a-zA-Z0-9_]

## Raw String

As rows string indicam para o python que dada string é realmente literal e não possue caracteres de controle.

`match(r'\\section', '\\section\n')`

## Metacactere Pipe ( | ) == OR

`match('a|b', 'cde')`

## Repetições

### Quantidades específicas

```
Usa-se as chaves( `"{}"` ) para indicar o número de repetições.

    match(r'\d{4}', '1234')
    -> 1234

match(r'\d{4}', '123')
-> None

match(r'\d{4}', '12345')
-> 1234
```

### Quantidades mínimas

```
É no mínimo dois ou mais. Usa-se a vírgula para determinar o minimo.

    match(r'\d{2,}', '12')
    -> 12

match(r'\d{2,}', '122345')
-> 12345

match(r'\d{2,}', '1')
-> None

A "?" é um modificador da repetição, que modifica seu comportamento,
e transforma uma repetição ganancioasa em preguiçosa.

    match(r'\d{2,}?', '12345')
```

### Min e Máx

```
match(r'\d{2,4}', '12345')
->1234

match(r'\d{2,4}', '1234')
->1234

match(r'\d{2,4}', '123')
->123

match(r'\d{2,4}', '12')
->12

match(r'\d{2,4}', '1')
->None

match(r'\d{2,4}?', '12345')
->12
```

### 0 ou 1 ocorrência

```
match(r'\d{0,1}', '12345')
-> 1

match(r'\d{,1}', '12345')
-> 1

Não retornou nenhum, pois pega o minimo possível e o mínimo é zero.
    match(r'\d{,1}?', '12345')
    -> ''

Realiza a operação 0 ou 1.
    match(r'\d?', '12345')
    -> 1

A primeira interrogação é o modificador de repetição e repete o que vem antes,
a segunda interrogação é o modificador do operador de repetição,
transformando de ganancioso para preguiçoso.
    match(r'\d??', '12345')

```

### 0 ou mais vezes/ocorrências
    
`match(r'\d{0,}', '12345')`

### 1 ou mais vezes/ocorrências

```
match(r'\d{1,}', '12345')
-> 12345

Exige no minimo uma ocorrencia dos digitos passados.
    match(r'\d+', '12345')
    -> 12345

match(r'\d+?', '12345')
```

### Match Object

### Grupos de captura

Grupos de não captura são indicados por `?:`

### Named Groups (extensão específica do Python)
