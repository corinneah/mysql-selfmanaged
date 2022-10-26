# import packages 
import pandas as pd 
import os 
from sqlalchemy import create_engine
from dotenv import load_dotenv

# load variables 
load_dotenv()

#login/user information 
MYSQL_HOSTNAME = os.getenv('MYSQL_HOSTNAME')
  
MYSQL_USER = os.getenv('MYSQL_USERNAME') 
  
MYSQL_PASSWORD = os.getenv('_Passwordmysql') 
  
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

# connecitng to a database(db)
connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
db = create_engine(connection_string)

