
# 使用Body方法定义单值的请求体参数

"""

扩展之前的模型，之前的模型还需要额外增加一个参数：需要importance在请求体中:
@app.get("/items/{item_id}")
async def read_items(

    *,
    q: str = Query(None),
    item_id: int = Path(..., title="The ID of the item to get",ge=0,le=100),
    size: float = Query(...,gt=0,lt=100)

    # 需要参数importance在这里
    # 并且importance是个单值 不想让其是Path和size 而是一个关键字
    # 如果你直接定义它，因为他是一个单值，FastAPI会默认将其定义为query参数。
    # 但是你可以使用Body方法，让FastAPI将其视为请求体的key：
    importance: int = Body(...)
):

"""
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}

    return results


# uvicorn parameter-Body:app --reload

# 这是多个请求体参数时的请求体body 每个参数都时key:value 形式 其中value是字典形式
'''
请求体如下
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}

'''

# 单个请求体参数时就需要这样写:
'''
{
    
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
}
'''
# 若想单个请求体参数也以key:value形式 可以和上面importance一样使用Body()
# async def update_item(
#     *,
#     item_id: int,
#     item: Item = Body(..., embed=True)# 此处为固定写法
# ):

# 此时请求体就是:
'''
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
'''