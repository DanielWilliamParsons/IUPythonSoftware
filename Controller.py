import Analyzer as a
import DataManager as dm
import Visualizer as vl

class CategorizerController(object):

    def __init__(self):
        print("Initializing an instance of the Controller class")
        self.analyzer = a.Analyzer()
        self.trainingDataManager = dm.DataManager("training")
        self.testDataManager = dm.DataManager("test")
        self.idealDataManager = dm.DataManager("ideal")
        self.dataManager = dm.DataManager()
        self.visualizer = vl.Visualizer()

    def uploadData(self, pathToDataFile, nameForData):
        '''
        Calls the DataManager
        '''
        self.dataManager.importData(pathToDataFile, nameForData)
        print("uploading data through the controller")

    def loadDataToMemory(self):
        '''
        Method to load training, test and ideal data into memory
        '''
        print("Loading data to memory")
        self.trainingDataManager.readDataFromDB()
        self.testDataManager.readDataFromDB()
        self.idealDataManager.readDataFromDB()

    def deleteDataWithName(self, dataName):
        '''
        Method to delete data from the database
        :param dataName: string to identify the data
        '''
        print("Deleting data with name: ", dataName)
        self.dataManager.deleteData(dataName)

    def selectIdealFunction(self):
        '''
        Method to run the regression analysis
        '''
        idealFunctionsData = self.analyzer.selectIdealFunction()
        print("Running the regression analysis")


    def categorizeTestData(self):
        '''
        Method to call the Analyzer to categorize the test data
        '''
        mappedTestData = self.analyzer.categorizeTestData()
        print("Categorizing the test data")

    def visualizeData(self, chartType):
        '''
        Method to visualize the data
        :param chartType: string to indicate which visualization type to invoke
        '''
        method = getattr(self.visualizer, chartType, None)
        if callable(method):
            method(self.dataManager)
        else:
            print(f"Error: '{chartType}' is not a valid visualization method.")
            # Handle the error for the user
        print("Visualizing data through the controller")