import pandas as pd
import DBHandler as db
class DataManager(object):
    '''
    A class to read data from a file, from a database,
    and allow data to be stored in memory before and after manipulation
    '''

    def __init__(self, nameForData):
        '''
        Initialize the class
        :param self.database: an instance of the DBHandler class to handle CRUD operations
        :param nameForData: a string identifier for the name of the table in the database
        :param data: a pandas dataframe containing a copy of the data from the database
        '''
        print("Initializing the DataManager")
        self.database = db.DBHandler()
        self.nameForData = nameForData
        self.data = "" # Initializes an empty data variable

    def importData(self, pathToFile, nameForData):
        '''
        Method to read data from a file and store it in the database with a name to identify the data.
        Sets the nameForData parameter
        Sets the data parameter itself
        No data is stored in the self.data variable when importing data from a file.
        :param self.database: an instance of the DBHandler class to handle CRUD operations
        :param pathToFile: identifies the file in the local system where the data is located
        :param nameForData: user provides a name to identify the data in the database
        '''
        self.data = pd.read_csv(pathToFile)
        print("Importing the data")
        print(self.data)
        self.nameForData = nameForData
        self.database.createTableAndInsertData(self.data, self.nameForData)
        # Empty the self.data variable
        self.data = ""

    def readDataFromDB(self):
        '''
        Method to read data from the database and store it locally.
        Permanently stores the data in the self.data variable.
        :param nameForData: Optional variable to find the data in the database.
        '''
        # Read the data from the database
        print("Reading the data")
        self.data = self.database.readData(self.nameForData)

    def exportData(self):
        '''
        Method to export outputData to a file
        :param fileName: user provides a fileName or default file name is results.csv
        '''

        print("Exporting the data")

        # Save self.outputData to a file
    
    def deleteData(self, dataName=None):
        '''
        Method to delete data from the database
        '''
        print("Deleting data")
        if dataName:
            self.database.deleteData(dataName)
        else:
            self.database.deleteData(self.nameForData)