import Analyzer as A
import DBHandler as D

class Controller(object):

    def __init__(self):
        db = D.DBHandler()
        analyzer = A.Analyzer()