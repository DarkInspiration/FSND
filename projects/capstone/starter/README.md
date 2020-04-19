# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for:
    - Barista
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 2 users - assign the Barista role to one and Manager role to the other.
    - Sign into each account and make note of the JWT.
    ```Manager: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpWYXFaMnRjbkpCVTZqcDVoaEgxZyJ9.eyJpc3MiOiJodHRwczovL2RhcmtpbnNwaXJhdGlvbi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU4ZjY0ODZjNDYyZDcwYzBkYzA5MjRlIiwiYXVkIjoiY29mZmVlX3Nob3AiLCJpYXQiOjE1ODY1MDI5ODEsImV4cCI6MTU4NjU4OTM4MSwiYXpwIjoiczZMUkU3dTlhUzdTU3kzT2E5TWxNRE9DNjMwbW5GSHYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsInBhdGNoOmRyaW5rcyIsInBvc3Q6ZHJpbmtzIl19.MnKxE0OfnpkaWJcpi4LhiqTVDKUIRViqg6uHH0PNVFeTrcyBEiPl8GrXRaa2r2I1dVTYrYZdG4oPH9s2Eodxn5CE6NNQyiqlT4yQOkp5mZhybZvr3yBuF5e6O8KyHNUXDmUwuPmhRUjvxx_Y7KgHA2TAXRUmlNaER5gZaOwdLrHkRm0C_lNSVr74xVJiRmj5MIB-VTPdFWc0vttjPU_s4dVXlxjA8YrfodC1Py2-1HIAaTB8erj51-rWyj3O1JuctiUoIzwnWbcx5gF9DJ-nur-iOf7bwlLBId2bMf2Y4eTFrE4WLLoT8Ottaoew-FMEpXSXauiRphD9WEqFZP-v1g```
    ```Barista: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpWYXFaMnRjbkpCVTZqcDVoaEgxZyJ9.eyJpc3MiOiJodHRwczovL2RhcmtpbnNwaXJhdGlvbi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU4ZjY0MzljNDYyZDcwYzBkYzA5MWM1IiwiYXVkIjoiY29mZmVlX3Nob3AiLCJpYXQiOjE1ODY1MDMwNDgsImV4cCI6MTU4NjU4OTQ0OCwiYXpwIjoiczZMUkU3dTlhUzdTU3kzT2E5TWxNRE9DNjMwbW5GSHYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MtZGV0YWlsIl19.Fa6k9-fqdt2vOtHOdQ4aSjnUTIXQ9X3LbXCN4r2PRRiJRD8OrILba4hDo486AhXeaPdb9aixQ_tVh8NDW9twL_o0pGreSXFnUIDY_6Fkiqi-lHSYvtf7hJmLkk-bD-pKY0Sne4rPpy1zAAXrA2T_1b8gnNZX9J2xaTG7IfJeiDJp_ben_i4W5rQfIvGzffHkfkcBvkSFiAjJXkHHlbdJNVwmqtn2aLZskOkd6fQZuN5VaX00UYEhUpZpHq3CGONeG58ls1V4GsSZNlKVuHKC6HDmAC-gKNFcJlQh76p5tmxoi_T8QKQ65bhG3BJ-aOI6bMhLTOLKxC7w6myIamKnZw```
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json`
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review!

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`
