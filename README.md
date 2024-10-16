# WK Seguros

> Aplicação se seguros em desenvolvimento:
> Tecnologias que serão usadas:
> - Flask
> - FastAPI
> - SQLAlchemy
> - Alembic
> - Pydantic
>
> Padrão de projeto: repository pattern

## Estrutura futura do projeto

~~~yaml
/wkseguros
│
├── /alembic
├── /backend
│   ├── /api               # Backend APIs (FastAPI)
│   │   ├── /v1
│   │   │   ├── __init__.py
│   │   │   ├── cotacao_api.py
│   │   │   ├── contrato_api.py
│   │   │   ├── proposta_api.py
│   │   │   ├── apolice_api.py
│   │   │   └── pagamento_api.py
│   │
│   ├── /core              # Configurações e inicialização do banco
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── /models            # Modelos do banco de dados (SQLAlchemy)
│   │   ├── __init__.py
|   |   ├── user.py
│   │   ├── cliente.py
│   │   ├── apolice.py
│   │   ├── cotacao.py
│   │   └── sinistro.py
│   │
│   ├── /repositories      # Repositórios de persistência (Repository Pattern)
│   │   ├── __init__.py
|   |   ├── user_repository.py
│   │   ├── cliente_repository.py
│   │   └── apolice_repository.py
│   │
│   ├── /services          # Lógica de negócios
│   │   ├── __init__.py
|   |   ├── auth.py
│   │   ├── cotacao_service.py
│   │   └── apolice_service.py
│   │
│   ├── /schemas           # Schemas de entrada/saída (Pydantic)
│   │   ├── __init__.py
|   |   ├── user.py 
│   │   └── cotacao.py
|   |
│   │
│   ├── /migrations        # Migrações do banco de dados (Alembic)
│   └── main.py            # Ponto de entrada da API FastAPI
│
├── /frontend              # Frontend (Flask)
│   ├── /static            # Arquivos estáticos (CSS, JS, imagens)
│   │   ├── /css
│   │   └── /js
│   ├── /templates         # Templates HTML (Jinja2)
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── cotacao.html
│   │   └── contrato.html
│   ├── /routes            # Rotas do Flask (endpoints do frontend)
│   │   ├── __init__.py
│   │   └── views.py       # Lida com renderização e lógica da UI
│   ├── /forms             # Formularios de interação (Flask-WTF)
│   │   └── cotacao_form.py
│   └── app.py             # Ponto de entrada do Flask (servidor frontend)
│
├── /tests                 # Testes unitários e de integração
│   ├── test_cotacao.py
│   └── test_frontend.py
│
├── pyproject.toml       # Dependências do projeto (FastAPI, Flask, SQLAlchemy, etc.)
├── alembic.ini            # Configurações do Alembic para migrações
├── .env                   # Variáveis de ambiente
└── README.md              # Documentação do projeto
~~~



## Área de login

![Currency Converter](/wkseguros/frontend/static/img/logingif.gif)

## Dashboard principal

![Currency Converter](/wkseguros/frontend/static/img/dashboard.png)


