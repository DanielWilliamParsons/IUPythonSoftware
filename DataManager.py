import pandas as pd
import DBHandler as db
class DataManager(object):
    '''
    A class to read data from a file, from a database,
    and allow data to be stored in memory before and after manipulation
    '''

    def __init__(self, nameForData=None):
        '''
        Initialize the class
        :param self.database: an instance of the DBHandler class to handle CRUD operations
        :param nameForData: a string identifier for the name of the data in the database
        :param data: a pandas dataframe containing a copy of the data from the database
        '''
        self.database = db.DBHandler()
        self.nameForData = nameForData
        self.data = "" # TODO update this
        self.outputData = "" # TODO update this
        print("Initializing the DataManager")

    def importData(self, pathToFile, nameForData):
        '''
        Method to read data from a file and store it in the database with a name to identify the data.
        Sets the nameForData parameter
        Sets the data parameter itself
        :param pathToFile: identifies the file in the local system where the data is located
        :param nameForData: user provides a name to identify the data in the database
        '''
        self.data = pd.read_csv(pathToFile)
        print(self.data)
        self.nameForData = nameForData
        print("Importing the data")

    def readDataFromDB(self, nameForData=None):
        '''
        Method to read data from the database and store it locally
        :param nameForData: Optional variable to find the data in the database.
        '''
        if self.nameForData is None and nameForData is None:
            # Handle the error - insist the user passes a name for the data
            foo=0 # Delete this
        print("Reading the data")

        

    def exportData(fileName=None):
        '''
        Method to export outputData to a file
        :param fileName: user provides a fileName or default file name is results.csv
        '''
        if fileName == None:
            fileName = "results.csv"

        print("Exporting the data")

        # Save self.outputData to a file