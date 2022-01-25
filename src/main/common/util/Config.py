import os
import configparser

class Config:
    def __init__(self):
        self.filename = os.path.dirname(os.path.abspath(__file__)) + '.\config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)

    def getConfig(self, first, second):
        return self.config[first][second]
