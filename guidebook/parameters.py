from fastapi import FastAPI

ex1 = FastAPI()

@ex1.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id":item_id}

ex2 = FastAPI()

@ex2.get("/items/{item_id}")
async def read_item(item_id:int): # int로 제한
    return {"item_id":item_id}

ex3 = FastAPI()

@ex3.get("/users/{user_id}")
async def read_user(user_id:str):
    return {"user_id":user_id}

@ex3.get("/users/me")
async def read_user_me():
    return {"user_id":"the current user"}

from enum import Enum

class ModelName(str,Enum):
    alexnet="alexnet"
    resnet="resnet"
    lenet="lenet"

ex4 = FastAPI()
@ex4.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

ex5 = FastAPI()
@ex5.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path":file_path}

ex6 = FastAPI()

fake_items_db = [{"item_name":"Foo"}, {"item_name":"Bar"}, {"item_name":"Baz"}]

@ex6.get("/items/")
async def read_item(skip:int=0, limit:int=10):
    return fake_items_db[skip : skip+limit]

from typing import Union

ex7 = FastAPI()

@ex7.get("/items/{item_id}")
async def read_item(item_id:int, q:Union[str,None]=None):
    if q:
        return {"item_id":item_id, "q":q}
    else:
        return {"item_id":item_id}
    
from typing import Union

ex8 = FastAPI()
@ex8.get("/items/{item_id}")
async def read_item(item_id:int, q:Union[str,None]=None, short:bool=False):
    item = {"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"This is an amazing item that has a long description"})
    return item

from typing import Union
ex9 = FastAPI()
@ex9.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id:int, item_id:str, q:Union[str,None]=None, short:bool=False):
    item = {"item_id":item_id, "owner_id":user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item

ex10 = FastAPI()
@ex10.get("/items/{item_id}")
async def read_item(item_id:str, needy:str):
    item = {"item_id":item_id, "needy":needy}
    return item