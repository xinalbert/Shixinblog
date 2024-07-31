<!--
 * @Author: albertxin albert_xin@qq.com
 * @Date: 2024-07-26 16:06:00
 * @LastEditors: albertxin albert_xin@qq.com
 * @LastEditTime: 2024-07-30 15:27:38
 * @FilePath: /shixinblog/blog/linux巧用.md
 * Copyright (c) albertxin by albert_xin@qq.com, All Rights Reserved. 
-->
# Linux 巧用


## 利用两个仅含一列字符的文件求交际
```bash
sort file1.txt file2.txt |uniq -d
```

## 利用cat sort uniq求并集
```bash
cat file1.txt file2.txt | sort | uniq
```
## 并集都有了当然差集也不能少
```bash
sort fileA.txt >fileA.txt.sorted
sort fileB.txt >fileB.txt.sorted

#只在A中不在B中的元素
comm -23 fileA.txt.sorted fileB.txt.sorted
# 只在B中不在A中的元素
comm -13 fileA.txt.sorted fileB.txt.sorted

```
## 利用sed替换字符串
```bash
sed 's/old/new/g' file.txt
```

## 利用awk取第一列
```bash
awk  '{print $1}' file.txt
```

## 查找特定格式文件的真实地址
```bash
find ./data/2.clean_data/ -type f -name "*.fq.gz"| while read id ;do rr $id ;done >rr_datapath.txt
```