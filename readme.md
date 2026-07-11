this is basic crud based task management app with authentication using jwt token 

this is the file structure that is the basic template for creating any backend app in fastapi 

we have to create a main.py like server.js in mern 
then we have to create some file for processing such as -

router.py
controller.py
models.py
dtos.py

and we have to include a - __init__.py file as well 

and then there are some utils files such as -
db.py 
helpers.py
and others 

for database setup with fastapi such as postgress -

we have to install the SQLAlchemy using pip install SQLAlchemy command  for setting up the database and then we have to install the pydantic_settings using pip install pydantic_settings

we also need install psycopg using pip install "psycopg[binary]" for macos
 
and then in code , we have to define base by using declarative_base and also localsession by using sessionmaker from sqlalchemy.org, engine by using create_engine imported from sqlalchemy

and then bind the engine in base

and then create the localsession 

and then create a function for providing the session where 
we will have a refrence for localsession and then in try 
we will yield the session and in finally 
we will close the session 