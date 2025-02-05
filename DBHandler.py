import sqlalchemy
import pymysql
import sqlalchemy as db

class DBHandler(object):

    def __init__(self):
        self.username = 'root'
        self.password = ""
        self.database_name = ''
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