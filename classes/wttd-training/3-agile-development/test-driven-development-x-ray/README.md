### Test All the Fucking Time! (TAFT)

- Entregar software é HARD!
- "A grande coragem, para mim é a prudência." Eurípedes

### Desenvolvedor Corajoso

INPUT -> PROCESSAMENTO -> OUTPUT

### Desenvolvedor Prudente

INPUT <- PROCESSAMENTO <- OUTPUT = TDD

**O cliente vê valor no output**

### Kata: A arte marcial na programação

```markdown
Movimentos praticados no treino de artes marciais,
realizados em conjunto ou individualmente.
```

### O que faz o unittest?

O que acontece quando eu executo o comando unittest?

- A partir do diretório corrente, o TestRunner:
    - procura e carrega o [módulo/package test*.py (Suítes de Teste)]
    - identifica cada [Cenário de Teste (TestCase)]
    - identifica [cada test (TestMethod)] nos cenários de Test
    - executa setUp(monta o contexto), Test, e tearDown(limpa os efeitos colaterais do teste) para casa test

### Como o Django executa os testes?

```markdown
$ manage test
$ manage test eventext.core
$ manage test eventext.core.tests.HomeTest
$ manage test eventext.core.tests.HomeTest.test_get
```
