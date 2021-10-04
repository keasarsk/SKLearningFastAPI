# 响应模型
# 可以在任何路径操作中使用参数 response_model 声明用于响应的模型

# response_model是（get，post等）“ decorator”方法的参数，该参数接受一个模型类。
# 它接收的类型与您为Pydantic模型属性声明的类型相同，因此它可以是Pydantic模型，但也可以是例如 一个Pydantic模型的清单，例如List [Item]。

# response_model功能：
# 最重要的功能：将输出数据限制为模型的数据。从而可以将输出数据转换为其类型声明，并且可以验证数据最后将由自动文档系统进行使用
# 应用:
# 将请求体的部分响应回去
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.types import EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None

@app.post("/user/", response_model=UserOut)
async def create_user(
    *,
    user: UserIn
):
    return user
