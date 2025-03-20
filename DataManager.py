import pandas as pd
import DBHandler as db
class DataManager(object):
    '''
    A general class to read data to and from a file, to and from a database,
    and allow data to be stored in memory before and after manipulation
    The user must supply the name of a table in the database to access and store data in each of the methods
    '''

    def __init__(self):
        '''
        Initialize the class
        :param self.database: an instance of the DBHandler class to handle CRUD operations
        :param data: a pandas dataframe containing a copy of the data from the database
        '''
        print("Initializing the DataManager")
        self.database = db.DBHandler()
        self.data = "" # Initializes an empty data variable

    def importData(self, pathToFile, nameForData):
        '''
        Method to read data from a file and store it in the database with a name to identify the data.
        Sets the nameForData parameter
        Sets the data parameter itself
        No data is stored in the self.data variable when importing data from a file.
        :param pathToFile: identifies the file in the local system where the data is located
        :param nameForData: user provides a name to give to a table in the database
        '''
        self.data = pd.read_csv(pathToFile)
        print("Importing the data")
        print(self.data)
        self.database.createTableAndInsertData(self.data, nameForData)
        # Empty the self.data variable
        self.data = ""

    def readDataFromDB(self, nameForData):
        '''
        Method to read data from the database and store it locally.
        Permanently stores the data in the self.data variable.
        :param nameForData: Optional variable to find the data in the database.
        '''
        # Read the data from the database
        print("Reading the data")
        self.data = self.database.readData(nameForData)

    def exportData(self, fileName):
        '''
        Method to export outputData to a file
        :param fileName: user provides a fileName or default file name is results.csv
        '''

        print("Exporting the data")

        # Save self.outputData to a file
    
    def deleteData(self, nameForData):
        '''
        Method to delete data from the database
        '''
        print("Deleting data")
        self.database.deleteData(nameForData)

class DataManagerType(DataManager):
    '''
    A subclass to read data from a file and store it in memory
    This subclass allows the user to specify the type of data, e.g., training, testing, ideal
    so that it is semnatically easier to manage the data.
    '''
    def __init__(self, dataType):
        '''
        Initialize the DataManagerType class
        :param dataType: a string to identify the name of the SQL table containing the data
        '''
        print("Initializing the DataManagerType")
        super().__init__("")
        self.dataType = dataType

    def getDataType(self):
        '''
        Method to return the dataType
        '''
        return self.dataType

    def importData(self, pathToFile):
        '''
        Method to read data from a file and store it in the database with a name to identify the data.
        Sets the nameForData parameter
        Sets the data parameter itself
        No data is stored in the self.data variable when importing data from a file.
        :param pathToFile: identifies the file in the local system where the data is located
        '''
        self.data = pd.read_csv(pathToFile)
        print("Importing the data")
        print(self.data)
        self.database.createTableAndInsertData(self.data, self.dataType)
        # Empty the self.data variable
        self.data = ""

    def readDataFromDB(self):
        '''
        Method to read data from the database and store it locally.
        Permanently stores the data in the self.data variable.
        '''
        # Read the data from the database
        print("Reading the data")
        self.data = self.database.readData(self.dataType)

    def deleteData(self):
        '''
        Method to delete data from the database
        '''
        print("Deleting data")
        self.database.deleteData(self.dataType)
    