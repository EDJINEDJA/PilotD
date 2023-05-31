"""
  In this file, we are going to create an object called "preprocessing" 
  that will load data from the "data/raw" directory and return the data in the form of a list of dictionaries, called "db".
  This returned object will be used to insert data into the ICD database.
"""


from distutils.command.config import config
from db.client import Client
import json
import os
from pathlib import Path
from typing import List , Dict , TypeVar , Any
import pandas as pd

class PreProcessing():
    def __init__(self, Config  : Any) -> None:
        self.Config  = Config

    def Loading(self)-> None:
        
        #Load file from data/raw
        raw  = pd.read_csv(self.Config["RawData"]["Path"],index_col=False)
        #As we are working with data, there may be several other variables that are not needed for our project.
        #  We should delete all the variables that are not required.
        raw.drop(self.Config["RawData"]["Columns4Drop"],axis=1, inplace=True)

        #Use to dict methode for turn dataframe obeject into list of dict 
        data = raw.to_dict(orient='records')
        
        #Save the list of dict in form of json variable
        if not os.path.exists( self.Config["ProcessedData"]["ProcessedFile"]):
            with open(self.Config["ProcessedData"]["ProcessedFile"] , mode="w") as stream:
                json.dump(data, stream)

        print("Ok done ....")

    def Build(self)-> None:
        try:
            Client.admin.command('ping')
            collection=Client[self.Config["Db"]["DbName"]][self.Config["Db"]["DbName"]]

            #Load the json file
            with open(self.Config["ProcessedData"]["ProcessedFile"] , mode="r") as f:
                data = json.load(f)
                f.close

            #Insert it into the dataframe
            collection.insert_many(data)
            print("Pinged your deployment. You successfully post to MongoDB!")
        except Exception as e:
            print(e)

    def Test(self)-> None:
        try:
            Client.admin.command('ping')
            collection=Client[self.Config["Db"]["DbName"]][self.Config["Db"]["DbName"]]
            #Retrieval all data that the databases store
            print(collection.find({})[0])
            print("Ok ...")
        except Exception as e:
            print(e)


