import os
import json
from fileService import FileInstanse, FileService
class AppProdEnvironment:

    def __init__(self):
        print "PRODUCTION ENVIRONMENT LOADED"
        self.__loadDEVJSONFILE()


    def __loadDEVJSONFILE(self):

        try:
            self.datas = FileInstanse.readJSONDATAFromFile('/config/json/app_prod_env.json')
            print  self.datas
        except IOError:
            ErrorHandler.handle(IOError)


    def URL(self):
        return self.datas["URL"]

    def HOST(self):
        return self.datas["HOST"]

    def PORT(self):
        return self.datas["PORT"]

    def NAME(self):
        return self.datas["NAME"]

    def VERSION(self):
        return self.datas["VERSION"]

    def URL_WITH_PORT(self):
        return self.datas["URL_WITH_PORT"]

    def REDIS_HOST(self):
        return self.datas["REDIS_HOST"]
