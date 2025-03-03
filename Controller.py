import Analyzer as a
import DataManager as dm
import Visualizer as vl

class Controller(object):

    def __init__(self):
        print("Initializing an instance of the Controller class")
        self.analyzer = a.Analyzer()
        self.dataManager = dm.DataManager()
        self.visualizer = vl.Visualizer()

    def uploadData(self, pathToDataFile, nameForData):
        '''
        Calls the DataManager
        '''
        self.dataManager.importData(pathToDataFile, nameForData)
        # self.dataManager.readDataFromDB(nameForData)
        print("uploading data through the controller")

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


    def runRegressionAnalysis(self):
        '''
        Method to run the regression analysis
        '''
        print("Running the regression analysis")


    def runEvaluation(self):
        '''
        Method to run the evaluation on the regression analysis
        '''
        print("Running the evaluation")
