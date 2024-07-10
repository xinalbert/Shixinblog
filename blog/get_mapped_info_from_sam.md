# 获比对文件信息从sam文件中

```python
#coding=UTF-8 


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


def extract_aligned_read_ids(sam_file, output_file):
    with open(sam_file, 'r') as file:
        with open(output_file, 'w') as out_file:
            for line in file:
                # 跳过SAM文件的头部注释行
                if line.startswith('@'):
                    continue
                
                # 解析SAM记录
                fields = line.strip().split('\t')
                read_id = fields[0]
                flag = int(fields[1])
                
                # 检查比对是否成功
                if flag & 4 == 0: # 4 means unmapped
                    out_file.write(f"{read_id}\n")



if __name__ == "__main__":
    
    import sys
    import datetime

    if len(sys.argv) != 3:
        print("Usage: python script.py your_samfile.sam output_mapped_info.txt")
        sys.exit(1)
    
    # 示例文件路径
    sam_file = sys.argv[1]
    output_file = sys.argv[1]
    
    begin = datetime.datetime.now()
    time_start = sub_format_datetime(begin)
    print("Start Time :[{}]".format(time_start))
    
    # 调用函数  
    extract_aligned_read_ids(sam_file, output_file)

    
    time_end = sub_format_datetime(datetime.datetime.now())
    print("End Time :[{}]".format(time_end))
    runtime(begin)
```

# 使用方法

```
python script.py your_samfile.sam output_mapped_info.txt
``` 

# 运行结果

```
Start Time :[2021-11-16 15:35:31]
End Time :[2021-11-16 15:35:31]
Runtime: 0:00:00.000000
```     

# 说明

本脚本可以从sam文件中提取比对成功的read_id，并输出到文件中。     

# 注意事项 

- 脚本中使用了datetime模块，需要先安装。
- 脚本中使用了sys模块，需要先安装。
- 脚本中使用了sam文件，需要先比对或者下载。