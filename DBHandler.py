import sqlalchemy
import pymysql
import sqlalchemy as db
import os
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from dotenv import load_dotenv

load_dotenv()

class DBHandler(object):

    def __init__(self):
        self.username = os.getenv('DB_USERNAME', 'root')
        self.password = os.getenv('DB_PASSWORD', '')
        self.database_name = 'regression'
        print("Initializing the database handler instance")

        try:
            # Connect to the database without specifying the database to check it exists and create it if not
            temp_engine = db.create_engine(f'mysql+pymysql://{self.username}:{self.password}@localhost')
            temp_connection = temp_engine.connect()
            temp_connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {self.database_name}"))
            temp_connection.close()

            # Now connect to the specific database
            self.engine = db.create_engine(f'mysql+pymysql://{self.username}:{self.password}@localhost/{self.database_name}')
            self.connection = self.engine.connect()
            self.metadata = db.MetaData()
            print("Connected to the MySQL database successfully.")
        except OperationalError as e:
            print("Unable to connect to MySQL.")
            print("Error:", e)
            print("Make sure that MySQL is installed and running on your machine.")
            print("You can install MySQL with:")
            print("    - macOS: brew install mysql")
            print("    - Ubuntu: sudo apt-get install mysql-server")
            print("    - Windows: Download from https://dev.mysql.com/downloads/installer/")
            exit(1)


        

    def createTable(self):
        print("Creating a new table")

    def insertData(self):
        print("Inserting data into the table")

    def readData(self):
        print("Reading data from the table")