'''
Author: albertxin albert_xin@qq.com
Date: 2024-09-03 09:09:53
LastEditors: albertxin albert_xin@qq.com
LastEditTime: 2024-09-03 11:26:30
FilePath: /shixinblog/blog/src/python/tools.py
Copyright (c) albertxin by albert_xin@qq.com, All Rights Reserved. 
'''
def get_column(file_path, column_num=1, delimiter='\t'):
    """
    This function reads a file and returns a list of the specified column.
    
    Parameters:
    file_path (str): The path of the file to be read.
    column_num (int): The number of the column to be returned (1-based index).
    delimiter (str): The delimiter used to split the file.
    
    Returns:
    list: A list containing the values of the specified column.
    """
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(delimiter)
            if len(parts) >= column_num:
                yield parts[column_num-1]
            else:
                raise IndexError(f"Line does not have enough columns: {line.strip()}")

def contrast(list_in:list):
    """
    This function calculates the contrast of a list of str.

    Parameters:
    list_in (list): A list of str.


    Returns:
    list: The contrast of the list of str.

    """
    list_out = []
    for i in list_in:
        for j in list_in:
            if i<j:
                list_out.append(f"{i}_{j}")
    return list_out