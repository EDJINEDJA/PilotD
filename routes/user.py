from email import parser
from typing import List
from urllib import response
from fastapi import APIRouter
import re

from db.models.user import (UserIn , UserOut ,UsersOut, UserOutAll)
from db.client import Client
from db.schema.user import UsersOutAllSchema, Icd10ToIcd9OutSchema, Icd10ToIcd9OutMLSchema, Icd9ToIcd10OutMLSchema
from src.utils import Utils

user = APIRouter()

@user.get('/')
async def home():
    return "Welcome to my REST API"

@user.get('/icds/{SizeMin}/{sizeMax}/', response_model=UsersOut)
async def GetIcds(SizeMin : int , SizeMax : int):
    
    collection=Client["icdv1"]["icdv1"]
    request = collection.find({})
    NbrDocuments=collection.count_documents({})
    if SizeMax >= NbrDocuments:
        SizeMax=NbrDocuments
    return {"icds":UsersOutAllSchema(request[SizeMin:SizeMax])}


@user.get('/icd/icd9toicd10/{Icd9}/')
async def Icd9ToIcd10(Icd9 : str):
    collection=Client["icdv1"]["icdv1"]

    #pattern creation
    pattern = re.compile(".*{}.*".format(re.escape(Icd9)), re.IGNORECASE)
   
    request = collection.find({"CODE-9": str(Icd9)})
    try :
        if collection.count_documents({"CODE-9": str(Icd10)})==0:
            #Request lauched over the list containning dictionnary
            request = collection.find({"CODE-9": pattern})
            result= Utils().processing(list(request) , Icd9,attribut="CODE-9")
        
            return Icd9ToIcd10OutMLSchema(result)
        else: 
            return Icd10ToIcd9OutSchema(request)
    except:
        return {"Not" : "Found"}



@user.get('/icd/icd10toicd9/{Icd10}/')
async def Icd10ToIcd9(Icd10 : str):
    collection=Client["icdv1"]["icdv1"]

    #pattern creation
    pattern = re.compile(".*{}.*".format(re.escape(Icd10)), re.IGNORECASE)
    request = collection.find({"CODE-10": str(Icd10)})

    try :
        if collection.count_documents({"CODE-10": str(Icd10)})==0:
            #Request lauched over the list containning dictionnary
            request = collection.find({"CODE-10": pattern})
            result = Utils().processing(list(request) , Icd10, attribut="CODE-10")
        
            return Icd10ToIcd9OutMLSchema(result)
        else: 
            return Icd10ToIcd9OutSchema(request)
    except :
        return {"Not" : "Found"}

        
@user.get('/icd/icd10/{Description}/')
async def Icd10(Description : str):
    try:
        collection=Client["icdv1"]["icdv1"]
        #pattern creation
        pattern = re.compile(".*{}.*".format(re.escape(Description.lower())), re.IGNORECASE)
        #find all dictionnary related to collection
        request = collection.find({'DESCRIPTION': pattern})
        FirstResult = list(request)
        if len(FirstResult)==0:
           SecondResult = list(collection.find({'DESCRIPTION-GROUPED+': pattern}))
           FinalResult = FirstResult + SecondResult

           #return according the best score
           result = Utils().processing(FinalResult , Description.lower(), attribut="DESCRIPTION")
        else:
           #return according the best score
           result = Utils().processing(FirstResult , Description.lower(), attribut="DESCRIPTION")
        
        return Icd10ToIcd9OutMLSchema(result)
    except:
        return {"Not" : "Found"}


