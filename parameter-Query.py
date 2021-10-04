from fastapi import FastAPI

app = FastAPI()


@app.get("/files/")
def add(num1: int=1, num2: int=2):
    return {"num1 + num2 = ": num1 + num2}

'''
query参数类不是path中固定的一部分，所以他们是可选的，并且可以有默认值。

例如上面的例子，当你使用浏览器访问http://127.0.0.1:8001/files/?num1=2&num2=3，你会得到：{"num1 + num2 = ":10}

默认值也可以设置none
'''

# uvicorn parameter-Query:app --reload