# FastAPI_Crossfit_DIO
API assíncrona de competição de crossfit
### Quem é o FastAPi?
Framework FastAPI, alta performance, fácil de aprender, fácil de codar, pronto para produção.
FastAPI é um moderno e rápido (alta performance) framework web para construção de APIs com Python 3.6 ou superior, baseado nos type hints padrões do Python.

### Async
Código assíncrono apenas significa que a linguagem tem um jeito de dizer para o computador / programa que em certo ponto, ele terá que esperar por algo para finalizar em outro lugar

# Projeto
## WorkoutAPI

Esta é uma API de competição de crossfit chamada WorkoutAPI (isso mesmo rs, eu acabei unificando duas coisas que gosto: codar e treinar). É uma API pequena, devido a ser um projeto mais hands-on e simplificado nós desenvolveremos uma API de poucas tabelas, mas com o necessário para você aprender como utilizar o FastAPI.

## Modelagem de entidade e relacionamento - MER
![MER](/mer.jpg "Modelagem de entidade e relacionamento")

## Stack da API

A API foi desenvolvida utilizando o `fastapi` (async), junto das seguintes libs: `alembic`, `SQLAlchemy`, `pydantic`. Para salvar os dados está sendo utilizando o `postgres`, por meio do `docker`.

### Execução da API

Para executar utilizei gerenciador de pacote pip.


```bash
pip install -r requirements.txt
```
### Para o Windows é necessário esta instalado o [Docker Desktop](https://www.docker.com/products/docker-desktop/) e o mesmo estar em execução, apos isso execute o comado abaixo:

```bash
docker-compose up -d
```

Listar os containers em execução:

```bash
docker-compose ps
```

Para criar o banco de dados, execute:

```bash
alembic upgrade head
```

## API

Para subir a API, execute:
```bash
uvicorn workout_api.main:app --reload
```
e acesse: http://127.0.0.1:8000/docs

# Desafio Final
    - adicionar query parameters nos endpoints
        - atleta
            - nome
            - cpf
    - customizar response de retorno de endpoints
        - get all
            - atleta
                - nome
                - centro_treinamento
                - categoria
    - Manipular exceção de integridade dos dados em cada módulo/tabela
        - sqlalchemy.exc.IntegrityError e devolver a seguinte mensagem: “Já existe um atleta cadastrado com o cpf: x”
        - status_code: 303
    - Adicionar paginação utilizando a lib: fastapi-pagination
        - limit e offset
# Referências

FastAPI: https://fastapi.tiangolo.com/

Pydantic: https://docs.pydantic.dev/latest/

SQLAlchemy: https://docs.sqlalchemy.org/en/20/

Alembic: https://alembic.sqlalchemy.org/en/latest/

Fastapi-pagination: https://uriyyo-fastapi-pagination.netlify.app/

### Estrutura banco de dados
![Estrutura do banco de dados DBaever](<IMAGENS/Captura de tela 2024-05-24 095919.png>)

### Tabela Atleta
![Tabela Atleta](<IMAGENS/Captura de tela 2024-05-24 100048.png>)

### Tabela Contro Treinamento
![Tabela Centro Treinamento](<IMAGENS/Captura de tela 2024-05-24 100036.png>)

### Tabela Categoria
![Tabela Categoria](<IMAGENS/Captura de tela 2024-05-24 100022.png>)

### Container Docker fastapi_crossfit_dio
![Container Docker](<IMAGENS/Captura de tela 2024-05-24 100117.png>)

### Terminal Api workout
![Terminal Api workou](<IMAGENS/Captura de tela 2024-05-24 100229.png>)

### Api workout docs
![Api workout docs](<IMAGENS/Captura de tela 2024-05-24 100311.png>)

### Api workout paginação
![Api workout paginação](<IMAGENS/Captura de tela 2024-05-24 100335.png>)

### Api workout get cpf
![get cpf](<IMAGENS/Captura de tela 2024-05-24 100446.png>)

### Api workout get nome
![get nome](<IMAGENS/Captura de tela 2024-05-24 100500.png>)

### Manipular exceção de integridade post atleta
![Manipular exceção de integridade post atleta](<IMAGENS/Captura de tela 2024-05-24 100518.png>)