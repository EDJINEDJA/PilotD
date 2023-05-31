def UserOutAllSchema(item)-> dict:
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

def UsersOutAllSchema(items)-> list[dict]:

    return [UserOutAllSchema(item) for item in items]

def Icd9ToIcd10Schema(item)->dict:
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
def Icd9ToIcd10OutSchema(items)-> list[dict]:

    return [Icd9ToIcd10Schema(item) for item in items]

def Icd10ToIcd9Schema(item)->dict:
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
def Icd10ToIcd9OutSchema(items)-> list[dict]:

    return [Icd10ToIcd9Schema(item) for item in items]


def Icd9ToIcd10MLSchema(item)->dict:
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
def Icd9ToIcd10OutMLSchema(items)-> list[dict]:

    return [Icd9ToIcd10MLSchema(item) for item in items] 

def Icd10ToIcd9MLSchema(item)->dict:
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
def Icd10ToIcd9OutMLSchema(items)-> list[dict]:

    return [Icd10ToIcd9MLSchema(item) for item in items]