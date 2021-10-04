# 请求体嵌套
# 可以将请求体的属性值类型设置为列表、元组，列表里面的元素可以是正常的数据类型，也可以是请求体模型。
# 当然，请求体的属性值也可以设置为请求体模型。这种现象我们称之为模型的嵌套

from typing import List, Set

from fastapi import FastAPI
from pydantic import BaseModel, UrlStr

app = FastAPI()

class Image(BaseModel):
    url: UrlStr
    name: str

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []  # 表示属性值的类型为元组，元组中元素的类型为字符串
    images: List[Image] = None # 嵌套了另一个请求体模型

@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# 此时期望的请求体格式为：
'''
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": [
        "rock",
        "metal",
        "bar"
    ],
    "images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
    ]
}

'''