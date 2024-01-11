def process_items(items:list[str]): # the variables in a list is a str
    for item in items: print(item)

from typing import List
def process_items(items:List[str]):
    for item in items: print(item)

def process_items(items_t:tuple[int,int,str], items_s:set[bytes]):
    return items_t, items_s

def process_items(prices:dict[str,float]):
    for item_name,item_price in prices.items():
        print(item_name)
        print(item_price)

def process_item(item:int|str): # Union : item could be int or str
    print(item)

from typing import Optional
def say_hi(name:Optional[str]=None): # Optional : Shortcut of Union[Something, None]
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

say_hi()
say_hi("John")

class Person:
    def __init__(self, name:str):
        self.name = name

def get_person_name(one_person:Person):
    return one_person.name

# Pydantic Models
# FastAPI is all based on Pydantic
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str="John Doe"
    signup_ts:datetime|None=None
    friends:list[int]=[]

external_data = {
    "id":"123",
    "signup_ts":"2017-06-01 12:22",
    "friends":[1,"2",b"3"]
}
user = User(**external_data)
print(user)
print(user.id)