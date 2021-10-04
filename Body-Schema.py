# 我们可以使用Schema模型，在定义请求体模型的类属性的时候，给类属性添加默认值或者验证
from fastapi import Body, FastAPI
from pydantic import BaseModel, Schema

app = FastAPI()

class Item(BaseModel):
    name: str

    # 此处:
    description: str = Schema(None, title="The description of the item", max_length=300)
    price: float = Schema(..., gt=0, description="The price must be greater than zero")
    tax: float = None

@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item = Body(..., embed=True)

        # Body()中有个参数 example :
        # example={ "name": "Foo", "description": "A very nice Item", "price": 35.4, "tax": 3.2, }
        # 此时即给了item的格式例子
):
    results = {"item_id": item_id, "item": item}
    return results
