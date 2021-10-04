from fastapi import FastAPI

from enum import Enum
# Enum
# Generic enumeration. Derive from this class to define new enumerations.
# 通用的枚举。从该类派生来定义新的枚举。


# 限制路径参数,此例子为限制为传递几个固定值,可以通过改变class内容实现其它限制能力
class Hjx_Class_name(str, Enum):
    Name = 'huangjunx'
    Year = 18
    Id = '20153201072'
    student = True


app = FastAPI()


@app.get('/hjx/{hjx_man}')
def root(hjx_man: Hjx_Class_name):

    # 可以在root函数里面调用这个类的类属性。通过Hjx_Class_name.Name进行调用
    return {'status': Hjx_Class_name.Name}


'''
假设现在你有一个路径操作：/files/{file_path}，但是你需要 file_path 本身包含一个 路径， 比如 home/johndoe/myfile.txt.
因此, 文件路径可能是: /files/home/johndoe/myfile.txt
在这种情况，我们使用Path转换器就可以进行转换了。使用以下方法声明值是路径的路径参数
参数的名字是 file_path，:path说明参数file_path对应的类型是 path 类型.
'''
@app.get("/files/{file_path:path}")
def read_user_me(file_path):
    return {"file_path": file_path}