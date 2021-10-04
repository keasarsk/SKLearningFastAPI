from fastapi import FastAPI

app = FastAPI()

# 编写一个 路径操作装饰器
# 可以将get操作方法更改成@app.post()、@app.put()、@app.delete()等方法
# 可以更改相应的路径（"/"）为自己想要的
@app.get("/")
async def root():   # 此定义应该紧跟着装饰器
    return {"message": "Hello World"}

'''
然后使用终端开启uvicorn服务
    uvicorn main:app --reload
    
uvicorn main:app 命令指:
    main: main.py 文件(也可理解为Python模块).
    app: main.py 中app = FastAPI()语句创建的app对象.
    --reload: 在代码改变后重启服务器，只能在开发的时候使用
    
可以自己指定要运行的服务器ip和端口号:
例如：uvicorn main:app --host 127.0.0.1 --port 8001 --reload
'''

'''
然后打开浏览器，输入： http://127.0.0.1:8000。看看有没有打印出："message": "Hello World" 这句话，如果有，表示安装成功。

访问 http://127.0.0.1:8000/docs。你将会看到自动生成的API交互文档。这点很重要，也是fastapi的一个优点。
'''
