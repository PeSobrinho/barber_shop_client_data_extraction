import psycopg2
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT', '5432')
database = os.getenv('DATABASE')
schema = os.getenv('SCHEMA')

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

import pandas as pd

with open('sql/clientes_insatisfeitos.sql', 'r') as file:
    query = file.read()

clients_data = pd.read_sql(query, engine)

print(clients_data)
