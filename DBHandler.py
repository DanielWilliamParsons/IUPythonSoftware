import sqlalchemy
import pymysql
import sqlalchemy as db
import os
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

load_dotenv()

class DBHandler(object):

    def __init__(self):
        self.username = os.getenv('DB_USERNAME', 'root')
        self.password = os.getenv('DB_PASSWORD', '')
        self.database_name = 'regression'
        print("Initializing the database handler instance")
        self.engine = db.create_engine(f'mysql+pymysql://{self.username}:{self.password}@localhost/{self.database_name}')
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

    def createTable(self):
        print("Creating a new table")

    def insertData(self):
        print("Inserting data into the table")

    def readData(self):
        print("Reading data from the table")