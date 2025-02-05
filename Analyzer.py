import numpy as np

class Analyzer(object):
    '''
    The Analyzer class performs operations
    on data.
    These operations include regression analysis and evaluation of best fit model
    '''

    def __init__ (self):
        '''
        Initialize the Analyzer class.
        '''

    def simpleLinearRegression(self, pandasTable):
        '''
        Runs a regression analysis on data in the pandasTable.
        Note, since the pandasTable is mutable, it is modified in place
        so no need to return a value here.
        :param pandasTable: property of DataManager instance.
        '''
        print("Running a simple linear regression")

    def evaluateRegression(self):
        '''
        Evaluates the regression
        '''
        print("Evaluating the simple linear regression")