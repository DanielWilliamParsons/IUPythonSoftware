import sqlalchemy
import pymysql
import sqlalchemy as db

class DBHandler(object):

    def __init__(self):
        print("Initializing the database handler instance")

    def createTable(self):
        print("Creating a new table")

    def insertData(self):
        print("Inserting data into the table")

    def readData(self):
        print("Reading data from the table")