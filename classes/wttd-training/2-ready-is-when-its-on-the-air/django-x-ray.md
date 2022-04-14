# Raio X do Django

Um *Callable* é uma classe que se comporta como função, que pode ser chamada como um função. Estas classes contém um método especial `__call__()`.

## Views

Um callable que recebe uma intância de `HttpRequest` e retorna uma instância de `HttpResponse`.

**OBS: Não é um Controller**

### Anti Patterns in Views

- Views Grandes
- Conversões de dados na View
- Pilhas de Decoradores
- Uso de funções auxiliares que instanciam o `HttpResponse`
- Contextos de templates gigantes
