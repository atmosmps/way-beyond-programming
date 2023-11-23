# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone este repositório.
2. Crie um virtualenv com Python 3.7
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
https://github.com/atmosmps/way-beyond-programming
cd way-beyond-programming
python -m venv .way-beyond-programming
source .way-beyond-programming/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o Deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python secret contrib/secret_gen.py`
heroku config:set DEBUG=False

# configurar email
git push heroku master --force
```

## Estrutura dos Models

[Models Strucuture](../models-structure.png)
