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
        '''
        Initialize a DBHandler object.
        Create a database connection and store the connection as an instance variable.
        If the database does not exist, it will get created here.
        '''
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

    def createTableAndInsertData(self, pandasDataFrame, nameForData):
        '''
        Check that a table with the nameForData name does not already exist
        If it does not, create a new table with the nameForData name and insert the data from the pandas dataframe into the table.
        If it does, skip creating the table and return.
        :param pandasDataFrame: a pandas dataframe containing the data to be stored in the table
        :param nameForData: a string identifier for the name of the table in the database
        '''
        # Check that a table with the nameForDataname does not already exist
        inspector = db.inspect(self.engine)
        tables = inspector.get_table_names()
        if nameForData not in tables:
            # Create a new table
            print("Creating a new table")
            pandasDataFrame.to_sql(nameForData, self.engine)
        else:
            print("Table already exists. Skipping table creation.")

        return

    def insertData(self):
        print("Inserting data into the table")

    def readData(self):
        print("Reading data from the table")