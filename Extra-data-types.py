'''
除了下面常见的几种数据类型之外，

int
float
str
bool
fastAPI还提供了其它更复杂的数据类型:

1	UUID	一个标准的“通用唯一标识符”，在许多数据库和系统中通常作为ID使用。
            在请求和响应中将以str表示。
2	datetime.datetime	Python的日期时间类型: datetime.datetime.
            在请求和响应中，将以ISO 8601格式的str表示, 比如: 2008-09-15T15:53:00+05:00.
3	datetime.date	python的日期类型: datetime.date.
            在请求和响应中，将以ISO 8601格式的str表示, 比如: 2008-09-15.
4	datetime.time	Python的时间类型： datetime.time.
            在请求和响应中，将以ISO 8601格式的str表示, 比如: 14:23:55.003.
5	datetime.timedelta	Python的时间增量类型： datetime.timedelta.
            在请求和响应中，将以float表示总秒数.
6	frozenset	在请求和响应中, 格式与 set相同:
            在请求中，将读取列表，消除重复，并将其转换为“集合”.
            在响应中，set将会被转化为list.
7	bytes	Python标准类型： bytes.
            在请求和响应中将被视为str。
            生成的Schema将指定它是带有binary“格式”的str
8	Decimal	Python标准类型： Decimal.
            在请求和响应中，将以float格式.
'''