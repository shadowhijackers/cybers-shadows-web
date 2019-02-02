import os
import json
from services.errorHandler.errorHandler import ErrorHandler


class FileService:

    APP_ROOT = None

    def __init__(self):

        print "FILE SERVICE MODULE LOADED"
        self.APP_ROOT = os.path.dirname(os.path.abspath(__file__))

    def readJSONDATAFromFile(self, path):
        try:
            fileData = open(self.APP_ROOT + path, "r")
            datas = json.loads(fileData.read())
            return datas
        except Exception:
            ErrorHandler.handle(Exception)




FileInstanse = FileService()