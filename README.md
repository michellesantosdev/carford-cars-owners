# carford-cars-owners
To-Do List App

Description
Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small
town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color,
‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
Carford car shop want a system where they can add car owners and cars. Car owners may
not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the
system without owners.

# Passo a passo para rodar a aplicação

Foi utilizado o Python 3.9

## Instalar dependências
```
pip install -r requirements.txt
```

## Subir base de dados Postgres
```
docker-compose up
```

## Executar aplicação
```
python manage.py runserver
```

# Endpoints
- Url base da aplicação: `http://127.0.0.1:8000/api/v1/`
- Cadastrar dono: POST - `http://127.0.0.1:8000/api/v1/owners/`
  - ```
    {
        "name": "Michelle"
    }
    ```

- Cadastrar carro: POST - `http://127.0.0.1:8000/api/v1/cars/`
  - ```
    {
      "name": "Fusca",
      "color": "YELLOW",
      "model": "HATCH",
      "owner": 1
    }
    ```

# Documentação da API
A documentação da api está disponível em `http://127.0.0.1:8000/swagger/`


# Convenções de código e testes
## Rodar convenção de código
```
flake8
```

## Rodar testes
```
pytest
```
