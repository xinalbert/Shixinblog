# 使用Python记录你的函数所花时间

```python
import sys
import datetime


def sub_format_datetime(dt):
    """
    格式化日期时间。

    :param dt: datetime对象
    :return: 格式化后的日期时间字符串
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def runtime(start_time):
    """
    计算运行时间。

    :param start_time: 开始时间
    """
    end_time = datetime.datetime.now()
    print(f"Runtime: {end_time - start_time}")

def timepro(your_func, *args, **kwargs):
    """
    计算函数运行时间的装饰器。

    :param your_func: 需要计算运行时间的函数
    :param args: 位置参数
    :param kwargs: 关键字参数
    """
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = your_func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f"Function '{your_func.__name__}' ran in: {end_time - start_time}")
        return result
    return wrapper

```

使用方法：  
```python    
@timepro
def your_func():
    # your code here
    pass


your_func()
``` 

