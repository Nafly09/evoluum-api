# Evoluum API

Uma aplicação de Todo baseada em FastAPI com recursos de autenticação.

## Funcionalidades

- API RESTful construída com FastAPI
- Sistema de autenticação
- Gerenciamento de itens Todo
- Integração com banco de dados PostgreSQL
- Suporte a Docker
- Migrações de banco de dados com Alembic

## Tecnologias Utilizadas

- **Framework Backend**: FastAPI
- **Banco de Dados**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrações de Banco**: Alembic
- **Containerização**: Docker
- **Documentação da API**: Swagger UI integrado ao FastAPI

## Pré-requisitos

- Python 3.8+
- Docker e Docker Compose
- PostgreSQL

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd evoluum-api
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/evoluum
```

## Executando a Aplicação

### Usando Docker (Recomendado)

1. Construa e inicie os containers:
```bash
make up
```

2. Para parar os containers:
```bash
make down
```

3. Para atualizar as migrações do banco de dados:
```bash
make update-migration
```

4. A API estará disponível em `http://localhost:8000`

### Executando Localmente

1. Inicie o banco de dados PostgreSQL:
```bash
docker-compose up db
```

2. Execute a aplicação:
```bash
uvicorn main:app --reload
```

3. A API estará disponível em `http://localhost:8000`

## Documentação da API

Quando a aplicação estiver em execução, você pode acessar a documentação da API em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Estrutura do Projeto

```
evoluum-api/
├── alembic/              # Migrações do banco de dados
├── app/                  # Código da aplicação
│   ├── auth/            # Módulo de autenticação
│   ├── todo/            # Módulo de Todo
│   ├── core/            # Configurações principais
│   └── utils/           # Funções utilitárias
├── main.py              # Ponto de entrada da aplicação
├── requirements.txt     # Dependências Python
├── Dockerfile          # Configuração do Docker
├── docker-compose.yml  # Configuração do Docker Compose
└── alembic.ini         # Configuração do Alembic
```

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes. 