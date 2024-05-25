# Projeto CRUD com Python, Flask e MySQL

Este projeto é um exemplo de aplicação web CRUD (Create, Read, Update, Delete) utilizando Python, Flask e MySQL. A aplicação permite gerenciar informações de clientes, incluindo criação, leitura, atualização e exclusão de registros.

## Requisitos

- Python 3.x
- MySQL
- Flask
- Flask-SQLAlchemy
- mysql-connector-python

## Instalação

1. Clone o repositório:

   ```sh
   git clone https://github.com/giordanGarci/python-crud-flask.git
   cd crud-python-flask
   ```

2. Crie um ambiente virtual:

   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

4. Configure o banco de dados MySQL:

   - Crie um banco de dados chamado `crud-python`.
   - Atualize a URI de conexão com o banco de dados em `app.config['SQLALCHEMY_DATABASE_URI']` conforme necessário.

5. Crie as tabelas no banco de dados:

   ```sh
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

## Estrutura do Projeto

- `app.py`: Arquivo principal que contém a aplicação Flask e as rotas.
- `templates/`: Diretório que contém os templates HTML.
  - `index.html`: Página inicial com links para cadastro e listagem de clientes.
  - `create.html`: Página de cadastro de clientes.
  - `list.html`: Página de listagem de clientes.
  - `update.html`: Página de atualização de informações de clientes.

## Uso

1. Inicie a aplicação:

   ```sh
   python app.py
   ```

2. Acesse a aplicação em seu navegador:

   ```
   http://127.0.0.1:5000/index
   ```

## Rotas

- `/index`: Página inicial.
- `/create`: Página de cadastro de clientes.
- `/cadastrar`: Rota para cadastrar um novo cliente (métodos GET e POST).
- `/list`: Página de listagem de clientes.
- `/update/<int:id>`: Página para atualizar as informações de um cliente específico (métodos GET e POST).
- `/delete/<int:id>`: Rota para excluir um cliente específico.


## Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

