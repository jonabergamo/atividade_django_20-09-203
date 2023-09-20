# API de Gerenciamento de Estudantes e Tarefas

## Descrição

Esta é uma API construída com o Django REST Framework. Ela é responsável pelo gerenciamento de estudantes, matérias e tarefas associadas aos estudantes.

## Requisitos

- Python 3.x
- Django 3.x
- Django REST Framework
- drf-yasg (para documentação Swagger)

## Instalação

1. Clone este repositório

   `git clone https://seu_repositorio.git`

2. Crie um ambiente virtual e ative-o

   `python3 -m venv venv`

   `venv\Scripts\activate`

3. Instale as dependências

   `pip install -r requirements.txt`

4. Prepare o banco de dados

`python manage.py makemigrations`

`python manage.py migrate`

## Como Usar

Execute o servidor de desenvolvimento do Django:

`python manage.py runserver`

Agora a API deve estar rodando em `http://127.0.0.1:8000/`.

### Endpoints

Os endpoints da API estão configurados da seguinte forma:

- `GET /api/alunos/` - Lista todos os alunos.
- `POST /api/alunos/` - Cria um novo aluno.
- `GET /api/alunos/<id>/` - Exibe detalhes de um aluno específico.
- `PUT /api/alunos/<id>/` - Atualiza um aluno específico.
- `DELETE /api/alunos/<id>/` - Deleta um aluno específico.

- `GET /api/disciplinas/` - Lista todas as disciplinas.
- `POST /api/disciplinas/` - Cria uma nova disciplina.
- `GET /api/disciplinas/<id>/` - Exibe detalhes de uma disciplina específica.
- `PUT /api/disciplinas/<id>/` - Atualiza uma disciplina específica.
- `DELETE /api/disciplinas/<id>/` - Deleta uma disciplina específica.

- `GET /api/tarefas/` - Lista todas as tarefas.
- `POST /api/tarefas/` - Cria uma nova tarefa.
- `GET /api/tarefas/<id>/` - Exibe detalhes de uma tarefa específica.
- `PUT /api/tarefas/<id>/` - Atualiza uma tarefa específica.
- `DELETE /api/tarefas/<id>/` - Deleta uma tarefa específica.

- `GET /api/alunos/<student_id>/tarefas/` - Lista as tarefas de um aluno específico.

### Documentação Swagger

A documentação Swagger da API está disponível em

`http://127.0.0.1:8000/swagger/`.
