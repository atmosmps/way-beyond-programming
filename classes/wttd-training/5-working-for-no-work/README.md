# Working for no work

# O Django e o Banco estão desalinhados

Isso pode ocorrer, quando, por exemplo, ocorre um IntegrityError. Significa que o código escrito em Django e o Banco 
estão falando coisas diferentes, estão desalinhados. Por exemplo, eu tenho no banco uma restrição de que um Banco não 
pode ser nulo, porém no Django está definido que o código pode tentar salvar este mesmo valor como nulo.

- *t0* modelo `Talk` com `start` `null=False` e `blank=False`
- *t1* criamos a migração 0005
- *t2* criamos a **tabela** `Talk` no banco com `start` **not null**
- *t3* modelo `Talk` com `start` `null=False`, mas `blank=True`
- *t4* *IntegrityError* ao tentar salvar o `Talk` com `start` **vazio**

Para consertar o problema, precisamos

- *t5* modelo `Talk` com `start` null=True e `blank=True`
- *t6* criar e aplicar a migração 0006 para **alinhar** django e banco

# Django Managers Topics
