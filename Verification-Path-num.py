# 与上一节使用 Query 声明查询参数的更多验证和元数据的方法相同，也可以通过Path声明路径参数的相同类型的验证和元数据
from fastapi import FastAPI, Path, Query
# 导入Path

# item_id: int = Path(..., title="The ID of the item to get")
# Path声明的元数据可以使用所有Query参数：title alias description min_length等等

app = FastAPI()


@app.get("/")
async def root():   # 此定义应该紧跟着装饰器
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_items(
    # 在这里使用* 表示其后的参数(item_id q)都是关键字参数 即kwargs 即使它们没有默认值(即 可以没有 = ).
    #   并且item_id 和 q的顺序可以随意
    *,

    q: str = Query(None),

    # 因为Path 参数是必须的（它是路径URL的一部分），因此需要用...声明标志这是必需参数
    # 参数ge le
    # ge 只能比较整数 限制item_id 大于等于ge值
    # le 只能比较整数 限制item_id 小于等于le值
    item_id: int = Path(..., title="The ID of the item to get",ge=0,le=100),

    # gt 能比较float 限制size 大于gt值
    # lt 能比较float 限制size 小于lt值
    size: float = Query(...,gt=0,lt=100)


):
    results = {"item_id": item_id,"size": size}
    # results = {"size": size}
    if q:
        results.update({"q": q})
    return results



# uvicorn Query-verification-num:app --reload

# http://127.0.0.1:8000/items/3  # 注意 item_id 参数 不能 item_id=3 这样,直接写个数字就行

# http://127.0.0.1:8000/items/?q=dsfsd&size=3.34 # 注意 Query的参数不用在装饰器@app.get("/items/")中