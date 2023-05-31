from pydantic import BaseModel
from typing import (List , Dict , Optional, TypeVar)


class UserIn(BaseModel):
    desease: str

class UsersOut(BaseModel):
    icds : List[Dict]
    
class UserOut(BaseModel):
    Score : int
    Icd9 : str
    Icd10 : str
    Icd10Grouped : str
    Icd10GroupedPlus: str
    ServiceMacro : str
    ServiceMicro : str
    ShortDescription : str
    LongDescription : str
    LongDescriptionPlus : str
    DescriptionGrouped : str
    McoHad : str
    Ssr : str
    Psy: str

class UserOutAll(BaseModel):
    Icd9 : str
    Icd10 : str
    Icd10Grouped : str
    Icd10GroupedPlus: str
    ServiceMacro : str
    ServiceMicro : str
    ShortDescription : str
    LongDescription : str
    LongDescriptionPlus : str
    DescriptionGrouped : str
    McoHad : str
    Ssr : str
    Psy: str