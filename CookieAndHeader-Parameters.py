# Cookie参数和Query Path参数一样定义 所有适用于他俩的验证和参数也都适用Cookie
from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(
    *,


    ads_id: str = Cookie(None)


):
    return {"ads_id": ads_id}

# 若不用Cookie()方法 同样该参数会被莫认为Query


# Header参数同上
from fastapi import FastAPI, Header

app = FastAPI()

@app.get("/items/")
async def read_items(
    *,


    user_agent: str = Header(None)


):
    return {"User-Agent": user_agent}
