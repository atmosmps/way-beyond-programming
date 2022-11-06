# Python Views

> "Python View são objetos Python Callables(executáveis, chamáveis),
> que recebem como primeiro parâmetro posicional uma instância de HTTP Request
> e retorna necessariamente uma instância de HTTP Response."

---

### Alias para o `manage.py`

In `$HOME/.zshrc`, includ the `alias`:

`alias manage-wbp="python $HOME/Workspace/personal-projects/way-beyond-programming/manage.py"`

---

# Eventex Notes

## Messages Lib

`messages` é o pacote de mensagens do Django.

Essa mensagem deve ser exibida no Template do Formulário e lá deve
ser configurada também.

O Django já adiciona as messages automaticamente no contexto
do formulário quando existe, através de um context processor.

**Success Feedback**

`messages.success(request, "Inscrição realizada com sucesso!")`

---

## Django ORM

- `create()` retorna a instancia criada;
- O `save()` não retorna a instancia criada, retorna None;
- `bulk_create()` -> permite persistir vários objetos de uma única vez, passando uma lista de instâncias para o objeto alvo;
- Quando um Objeto do model é criado em memória o ID é None, pois ainda não está salvo no Banco. Quando o save é chamado, ele verifica se o ID é NOne, se for ele salva, se não for, ele atualiza. Por isso, se eu tiver um objeto existente no banco e atualizar oID para None, na próxima instância ele irá criar um novo Objeto;
- Quando estamos manipulando os models, somente no momento do `save()` os dados são persistidos;
- O `create()` é o contrário. Ele pega os dados passados e salva direto no banco e retorna a instancia esta instancia salva no banco;

Se for necessário tomar decisões para definir o estado do modelo, o caminho a ser usado é o save(); Porque primeiro você realiza todas as manipulações que precisar e só depis chama o save;

Mais se você já possui os dados que precisa, nesse caso é um bom caminho usar o create diretamente;

### Existem 4 tipos fundamentais no ORM do Django

`s = Subscription(data=data)`

```
type(s) -> Uma instância do modelo é sempre uma linha; representa uma linha da tabela;
eventex.subscriptions.models.Subscription

type(Subscription) -> O modelo em si Subscription, reflete a tabela inteira; Descreve a estrutura da tabela;
django.db.models.base.ModelBase

type(Subscription.objects) -> É um manager. Um manager é quem sabe manipular a tabela; O manager é o intermediador, que consegue criar querysets para aquele modelo especifico daquele banco de dados; É uma ligação entre o modelo criado e o ORM do Django;
django.db.models.manager.Manager

type(Subscription.objects.all()) -> É o motor, o coração do ORM do Django; É a API do ORM do Django;
django.db.models.query.QuerySet
```

**Assim é possível separar as responsabilidades**

- Se estiver manipulando com uma linha, está usando a instancia do modelo;
- Se está descrevendo a tabela, está usando o modelo em si;
- Se está manipulando o conteúdo da tabela, está no universo do Manager;
- Se está construindo querys interfaceando com o ORM do Django, está no universo do queryset

### Querysets

Querysets são preguiçosos, só vão no banco quando se tenta acessar o conteúdo deles; Enquanto isso não acontece, qualquer construção com  `objects()` só retorna uma instância de `QuerySet()`;

Objeto Queryset que referencia um select * from em Subscription, esse objeto está em memória e não foi executado no banco ainda:

`qs = Subscription.objects.all()`

Quando fazemos `print(qs)` isso vai chamar o `__repr__` do Model que vai forçar a avaliação(`evaluate`) do queryset, que vai fazer com que a query seja feita no banco de dados para mostrar o conteúdo do banco;

O queryset faz cache dos dados, uma vez que ele faz o `fetch` dos dados dos banco, ele usa esse cache para trabalhar com dados que foram retornados na primeira consulta do objeto;

Existem casos aonde o Django realiza a consulta no Banco sem usar o cache, como por exemplo:

`qs[0]`

Nesse caso, o que ele está fazendo é: `qs.__getitem__(0)` e isso faz o `evalute` da queryset novamente;

Queryset suporta o `slice`; Mas somente para as manipulações que usam `limit` e `offset`;

**Update e delete com querysets**

Estas operações realizam o `evalute` assim que chamadas;

```
qs = Subscription.objects.all()
qs.update(cpf='00000000001')

--> 4 -> retorna a quantidade de elementos atualizados
```

**Consultas SQL diretamente(na mão)**

**raw queryset**

```
qs = Subscription.objects.raw('select id, name from subscriptions_subscription')
--> django.db.models.query.RawQuerySet

qs[0]
--> <Subscrption_deferred_cpf_created_at_email_phone: Atmos Maciel> -> como estamos filtrando somente o ID e nome no select, o retorno do objeto informa que os demais campos estão deferred(adiados/ignorados), ou seja, não foram retornados na consulta.

Se eu tentar acessar um atributo que não foi retornado na consulta, como por exemplo: qs.phone o Django irá realizar a consulta no banco novamente só para buscar essa informação.
```

**cursors**

```
from django.db import connection
cursor = connection.cursor()

cursor.execute('select name from subscriptions_subscription where email=%s', [henrique@gmail.com])
--> retorna um objeto SQLiteCursorWrapper

cursor.fetchone()
-->('Atmos Maciel',)
```

---

## URL Configuration

URL -> Uniform Resource Locator

---

## Django Template System

- Engine
- Template
  - Template Variables
  - Template Filters
  - Template Tags
  - Template Nodes
- Context
- Loader

---

## Django Forms

- Bounded: conectado a dados(preenchido com dados, contém dados). Somente estes podem ser validados.
- Unbounded: não conectado com dados(sem dados, vazio)

### Forms Architecture

- Forms: Responsável pelo pipeline de validação;
- Fields: Valida dados da requisição e os converte para tipos python;
- Widgets: Expõe os dados como controles html e sabe como obter os dados da requisição para pipeline;

### Validção

**form.is_valid()**

1. Se Form for bounded
2. Form full_clean()
3. Para cada field é executado:
   1. clean() do field;
      1. to_python
      2. validators
   2. método clean_* se esxistir no Form
4. Form clean()
5. errors ou cleaned_data
