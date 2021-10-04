from fastapi import FastAPI
from pydantic import BaseModel
'''
请求体(Request body)是客户端发送到您的API的数据。 响应体是您的API发送给客户端的数据。
API几乎总是必须发送一个响应体，但是客户端并不需要一直发送请求体。

定义请求体，需要使用 Pydantic 模型。注意以下几点
    不能通过GET请求发送请求体
    发送请求体数据，必须使用以下几种方法之一：POST（最常见）、PUT、DELETE、PATCH

'''

'''
声明请求体数据模型为一个类，且该类继承 BaseModel。所有的属性都用标准Python类。
和查询参数一样：数据类型的属性如果不是必须的话，可以拥有一个默认值或者是可选None。否则，该属性就是必须的。
'''
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


@app.get("/")
async def root():   # 此定义应该紧跟着装饰器
    return {"message": "Hello World!!"}



@app.post("/items/")
async def create_item(item: Item):
    return item

# uvicorn Request-body:app --reload
# 打开postman 选择post模式 输入http://127.0.0.1:8000/items/
#    在body中选择raw 并且选择JSON语言 输入：
#   {
#     "name": "Foo",
#     "description": "An optional description",
#     "price": 45.2,
#     "tax": 3.5
#   }