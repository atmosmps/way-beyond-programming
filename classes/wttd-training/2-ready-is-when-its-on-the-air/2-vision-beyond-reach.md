## Visão além do alcançe

### Mindset

- Uso o modo interativo para experimentar ciclos de feedbacks curtos
    - Testar hipóteses de maneira rápida para tomar decisões com base em fatos do que foi experimentado

- Navegue pelo ecossistema com iPython

- Foco no negócio do cliente
    - a pergunta chave pro cliente é: qual é o seu problema?
    - o que você não tem hoje e o que você está impedido de fazer poque você não tem a tecnologia disponível hoje?

- Prazo o cliente define. Qualidade é intríseca ao seu trabalho. Escopo é negociável.

## Live Software (Software como organismo vivo)

- Projeto embrionário

- Execução de ponta a ponta
    - hoje em dia isso se chama Full Cycle Developer
    
- decida apenas o necessário

- o fluxo de execução revela a estrutura
    - o banco tem que ser tão maleável quanto o software
    - quanto mais difícil for mudar o software em qualquer parte dele,
      mais cara será a manutenção,
      mais difícil será a entrega de valor e consequentemente, maior será o risco do projeto.

- a realidade revela a necessidade

## Programe como um chefe de cozinha

- só otimizo aquilo que eu consigo medir

- Layout do projeto
    - diretório de trabalho -> contém coisas que são satélites ao projeto.
    - diretório do projeto
    
- se está difícil, está errado

- Autonomation

## Pronto é quando está no ar

- 1 código N instâncias

- deploy tem risco arquitetural

- simplicidade do deploy impacta a frequência

- Heroku é barato

## Arma secreta do Tony Stark

- o poder por trás da sintaxe simples
- alto nível além dos bits e bytes
- tratar código como mensagem
- conceitos e abstrações poderosas

### Configurações do projeto

São aquelas inerentes ao código fonte, relacionadas ao codebase.

### Configurações de instância

São aquelas que não são inerentes ao projeto.

"Um único codebase para várias instâncias"

---

## Static x Media

### Static

Fazem parte do código fonte do projeto. Estão ligadas ao código fonte.

- `assets`
    - `css`
    - `javascript`
    - `...`

- Entram no sistema quando o programador faz deploy.

### Media

- Arquivos enviados ao sistema pelo usuário.
- Entram no sistema quando o usuário faz upload.
    - isso é uma diferença de momento. Significa que o ciclo de vida de um static está ligado a alterações
      feitas no código fonte e o processo de deploy, está ligado ao ciclo de desenvolvimento.
      Ja o Media precisa estar consistente e disponível o tempo inteiro, entre as releases do sistema.
