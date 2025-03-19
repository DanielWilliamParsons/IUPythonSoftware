import numpy as np
import pandas as pd

class Analyzer(object):
    '''
    The Analyzer class performs operations
    on data.
    These operations include selecting an ideal function
    and categorizing the test data.
    '''

    def __init__ (self):
        '''
        Initialize the Analyzer class.
        '''

    def selectIdealFunction(self, idealFunctions, trainingData):
        '''
        Selects the ideal function for the data
        It also calls an algorithm to calculate the maximum deviation on each training dataset
        :param idealFunctions: a pandas dataframe containing the ideal functions
        :param trainingData: a pandas dataframe containing the training data
        :return: a pandas dataframe containing the ideal functions for each trainingData along with its maximum deviation
        '''
        idealFunctionsData = pd.DataFrame()
        print('Selecting the idea function')
        return idealFunctionsData

    def categorizeTestData(self, idealFunctions, trainingData, idealFunctionsData, testData):
        '''
        Map the test data to the correct ideal function
        :param idealFunctions: a pandas dataframe containing the ideal functions
        :param trainingData: a pandas dataframe containing the training data
        :param idealFunctionsData: a pandas dataframe containing the ideal functions for each trainingData along with its maximum deviation
        :param testData: a pandas dataframe containing the test data
        :return: a pandas dataframe containing the test data mapped to the correct ideal function
        '''
        mappedTestData = pd.DataFrame()
        print("Categorizing the test data.")
        return mappedTestData