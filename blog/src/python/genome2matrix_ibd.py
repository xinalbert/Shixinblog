'''
Author: albertxin albert_xin@qq.com
Date: 2024-08-01 10:12:36
LastEditors: albertxin albert_xin@qq.com
LastEditTime: 2024-08-01 10:14:09
FilePath: /shixinblog/python/genome2matrix_ibd.py
Copyright (c) albertxin by albert_xin@qq.com, All Rights Reserved. 
'''
import pandas as pd
import numpy as np
import sys


def genome2matrix(filein, outpath):
# 读取 .genome 文件
    genome_file = filein
    data = pd.read_csv(genome_file, delim_whitespace=True)
    
    # 按照列排序
    def sort_str_num(pddata,colns=[]):
        import re
        ncol = []
        for i in colns:
            inum = i +'num'
            ncol.append(inum)
            pddata[inum] = pddata[i].apply(lambda x : int(re.findall(r'\d+', x)[0]))
        
        pddata_sort  = pddata.sort_values(by=ncol)
        return pddata_sort
        
    colns = ['IID1','IID2']
    data = sort_str_num(data,colns)
    
    # 提取 IID1, IID2 和 PI_HAT 列
    ibd_data = data[['IID1', 'IID2', 'PI_HAT']]
    
    # 获取所有唯一的个体ID
    unique_ids = pd.unique(ibd_data[['IID1', 'IID2']].values.ravel('K'))
    
    # 创建一个空的 DataFrame 用于存储矩阵数据
    ibd_matrix = pd.DataFrame(np.zeros((len(unique_ids), len(unique_ids))), index=unique_ids, columns=unique_ids)
    
    # 填充矩阵
    for row in ibd_data.itertuples():
        ibd_matrix.at[row.IID1, row.IID2] = row.PI_HAT
        ibd_matrix.at[row.IID2, row.IID1] = row.PI_HAT
    
    # 对角线设置为 1（个体与自身的相似度）
    np.fill_diagonal(ibd_matrix.values, 1)
    
    # 保存矩阵到文件
    ibd_matrix.to_csv(outpath, #index = False
                     )

def main():
    if len(sys.argv) != 3:
        print("""Usage: python genome2matrix_ibd.py <.genome file> <output file>
              The file only from plink --genome output.!!!
              Any qustion, please contact albert_xin@qq.com.
              """)
        sys.exit(1)

    filein = sys.argv[1]
    outpath = sys.argv[2]

    genome2matrix(filein, outpath)

if __name__ == '__main__':
    main()