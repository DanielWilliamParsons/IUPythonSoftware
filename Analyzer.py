import numpy as np
import pandas as pd

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

    def simpleLinearRegression(self, pandasTable, indVar, depVar):
        '''
        Runs a regression analysis on data in the pandasTable.
        Note, since the pandasTable is mutable, it is modified in place
        so no need to return a value here.
        :param pandasTable: property of DataManager instance.
        :param indVar: independent variable
        :param depVar: dependent variable
        '''
        print("Running a simple linear regression")
        X = np.c_[np.ones(pandasTable[indVar].shape[0]), pandasTable[indVar]]
        y = pandasTable[depVar].values
        beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y) # Normal Equation
        print(f"Regression Coefficients: {beta}")
        pandasTable['regression'] = beta[0] + beta[1] * pandasTable[indVar]

    def evaluateRegression(self):
        '''
        Evaluates the regression
        '''
        print("Evaluating the simple linear regression")