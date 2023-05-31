from typing import List , Dict
def UserOutAllSchema(item)-> Dict:
    return { "id":  str(item["_id"]),
        "Icd10" :  item["CODE-10"],
        "Icd9" :  item["CODE-9"],
        "Icd10Grouped" :  item["CIM10-GROUPED"],
        "Icd10GroupedPlus":  item["CIM10-GROUPED+"],
        "ServiceMacro" :  item["SERVICES-MACRO"],
        "ServiceMicro" :  item["SERVICES-MINI+"],
        "ShortDescription":  item["SHORTDESCRIPTION"],
        "LongDescription" :  item["DESCRIPTION"],
        "LongDescriptionPlus" :  item["DESCRIPTION-GROUPED+"],
        "DescriptionGrouped":  item["DESCRIPTION-GROUPED"],
        "McoHad" :  item["MCO/HAD"],
        "Ssr" :  item["SSR"],
        "Psy":  item["PSY"]}

def UsersOutAllSchema(items)-> List[Dict]:

    return [UserOutAllSchema(item) for item in items]

def Icd9ToIcd10Schema(item)->Dict:
    return {"Icd9" :  item["CODE-9"],
        "Icd10" :  item["CODE-10"],
        "Icd10Grouped" :  item["CIM10-GROUPED"],
        "Icd10GroupedPlus":  item["CIM10-GROUPED+"],
        "ServiceMacro" :  item["SERVICES-MACRO"],
        "ServiceMicro" :  item["SERVICES-MINI+"],
        "ShortDescription":  item["SHORTDESCRIPTION"],
        "LongDescription" :  item["DESCRIPTION"],
        "LongDescriptionPlus" :  item["DESCRIPTION-GROUPED+"],
        "DescriptionGrouped":  item["DESCRIPTION-GROUPED"],
        "McoHad" :  item["MCO/HAD"],
        "Ssr" :  item["SSR"],
        "Psy":  item["PSY"]
        }
def Icd9ToIcd10OutSchema(items)-> List[Dict]:

    return [Icd9ToIcd10Schema(item) for item in items]

def Icd10ToIcd9Schema(item)->Dict:
    return {
        "Icd10" :  item["CODE-10"],
        "Icd9" :  item["CODE-9"],
        "Icd10Grouped" :  item["CIM10-GROUPED"],
        "Icd10GroupedPlus":  item["CIM10-GROUPED+"],
        "ServiceMacro" :  item["SERVICES-MACRO"],
        "ServiceMicro" :  item["SERVICES-MINI+"],
        "ShortDescription":  item["SHORTDESCRIPTION"],
        "LongDescription" :  item["DESCRIPTION"],
        "LongDescriptionPlus" :  item["DESCRIPTION-GROUPED+"],
        "DescriptionGrouped":  item["DESCRIPTION-GROUPED"],
        "McoHad" :  item["MCO/HAD"],
        "Ssr" :  item["SSR"],
        "Psy":  item["PSY"]
        }
def Icd10ToIcd9OutSchema(items)-> List[Dict]:

    return [Icd10ToIcd9Schema(item) for item in items]


def Icd9ToIcd10MLSchema(item)->Dict:
    return {
        "Score" : item["SCORE"],
        "Icd10" :  item["CODE-10"],
        "Icd9" :  item["CODE-9"],
        "Icd10Grouped" :  item["CIM10-GROUPED"],
        "Icd10GroupedPlus":  item["CIM10-GROUPED+"],
        "ServiceMacro" :  item["SERVICES-MACRO"],
        "ServiceMicro" :  item["SERVICES-MINI+"],
        "ShortDescription":  item["SHORTDESCRIPTION"],
        "LongDescription" :  item["DESCRIPTION"],
        "LongDescriptionPlus" :  item["DESCRIPTION-GROUPED+"],
        "DescriptionGrouped":  item["DESCRIPTION-GROUPED"],
        "McoHad" :  item["MCO/HAD"],
        "Ssr" :  item["SSR"],
        "Psy":  item["PSY"]
        }
def Icd9ToIcd10OutMLSchema(items)-> List[Dict]:

    return [Icd9ToIcd10MLSchema(item) for item in items] 

def Icd10ToIcd9MLSchema(item)->Dict:
    return {
        "Score" : item["SCORE"],
        "Icd10" :  item["CODE-10"],
        "Icd9" :  item["CODE-9"],
        "Icd10Grouped" :  item["CIM10-GROUPED"],
        "Icd10GroupedPlus":  item["CIM10-GROUPED+"],
        "ServiceMacro" :  item["SERVICES-MACRO"],
        "ServiceMicro" :  item["SERVICES-MINI+"],
        "ShortDescription":  item["SHORTDESCRIPTION"],
        "LongDescription" :  item["DESCRIPTION"],
        "LongDescriptionPlus" :  item["DESCRIPTION-GROUPED+"],
        "DescriptionGrouped":  item["DESCRIPTION-GROUPED"],
        "McoHad" :  item["MCO/HAD"],
        "Ssr" :  item["SSR"],
        "Psy":  item["PSY"]
        }
def Icd10ToIcd9OutMLSchema(items)-> List[Dict]:

    return [Icd10ToIcd9MLSchema(item) for item in items]