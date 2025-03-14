# BE Development Template 

This is a simple backend developing template with flask / mongo / sql 

# Venv Setup

```
python -m venv .venv
source .venv/bin/activate
```

# Requirements
```
pip install -r requirements.txt
```

Creating Requirements: 

```
pip freeze > requirements.txt
```

# Running the flask server

```
flask run --debug 
```

OR 

```
flask shell
```

# Postgres: 

To disable postgres, just comment out the postgres commands in `__init__.py` 

```
brew services start postgresql
brew services stop postgresql # To stop
```

