from fastapi import FastAPI
from fastapi import Query
# 导入Query
# 为查询参数设置字符串验证
app = FastAPI()

@app.get("/items/")
# async def read_items(q: str = None):# 最简单的验证参数定义
# async def read_items(q: List[str] = Query(["foo", "bar"])):# q可以有多个值 以列表形式 此时“foo“,"bar"即q1 q2的默认值
async def read_items(
    q: str = Query(
        ...,# None代表q参数可选 若是... ，则url就必须给出该值
        alias="item-query",# alias 别名
        title="Query string",# 设置标题
        description="Query string for the items to search in the database that have a good match",# 设置参数q的描述
        min_length=3,# 最小字符长度
        max_length=50,# 最大长度
        regex="^fixedquery$",# 正则表达式
        deprecated=True,    # 标记这个参数是否已经被弃用
)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q}) # 给字典results添加一个健值对{"q": q}
    return results



# # uvicorn Query-verification-str:app --reload