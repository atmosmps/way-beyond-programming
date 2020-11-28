# Raio X da Orientação à Objetos

No Python Objetos possuem valor(value), identidade(id) e tipo(type).

Alan Kay - Criador do Conceito de Orientação a Objetos.

## Classes, atributos e métodos no Python

Quando uma classe é escrita, o python constrói esta classe, durante a construção,
em tempo de execução, ele roda a classe, para contruir a estrutura da classe.

### Atributos de classe

`Car.name, Car.portas` 

### Atributos de instância

Estão em valores diferentes da memória, mas do mesmo tipo da instância de Car.

```
c = Car()
c.name, c.portas
```
 
Todo objeto tem um método `__dict__`

`Car.__dict__`

Quando se tenta acessar um atributo que não existe em uma intância,
o python faz um `fallback` e pergunta a instância Pai se aquele método existe,
ele faz toda verificação na árvore de hierarquia de objetos;
Se chegar na classe base `object`, retorna um `AttributeError`;

Toda classe possui um atributo `__class__`;

`c.__clas__.name`

```python
class Car:
    name = 'Ferrari'

    # Constructor
    def __init__(self, model):
        self.model = model
```

### Atributos de classe e atributos de instância;

```
atributos de classe - é o atributo de instância da classe;
atributos de instância - é o atributo de um objetto instanciado a aprtir de uma classe definida;
```
