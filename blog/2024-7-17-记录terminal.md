<!--
 * @Author: albertxin albert_xin@qq.com
 * @Date: 2024-07-21 12:36:50
 * @LastEditors: albertxin albert_xin@qq.com
 * @LastEditTime: 2024-07-26 09:36:23
 * @FilePath: /shixinblog/blog/2024-7-17-记录terminal.md
 * Copyright (c) albertxin by albert_xin@qq.com, All Rights Reserved. 
-->
# 记录terminal

## 批量从ebi下载sra文件

在ebi中查找相应项目的bash下载文件，删除不需要的部分，然后利用axel命令下载。

```bash
#!/bin/bash
cat sra_link.txt |while read id ;do axel $id ;done
```

## 批量解压sra文件

使用fastq-dump命令解压sra文件，并将解压后的fastq文件存放在output文件夹下。其中--split-3参数表示对pair-end数据进行分割。

```bash
mkdir output 
ls ./sra_file/SRR*| while read file; do fastq-dump $file --split-3 -O ./output/;done
```

## 运行jupyter lab

这个是在运行环境之前，将jupyter环境中的路径添加到PATH中。不然直接运行会使用服务器中default的python环境。

```bash
export PATH=/home/zhushixin/miniconda3/envs/jupyter/bin:$PATH
jupyter-lab
```

## 对解压后的软件尝试进分析

利用pipline所配备的默认yaml配置文件进行分析。

## 利用jcvi绘制共显性图

```bash
python -m jcvi.graphics.karyotype seqids layout --keep-chrlabels --notex
```

## awk 选文件第一列无重复

```bash
awk '!seen[$1]++ {print $1}' Aly.filter.bed
```

## awk 替换字符

```bash
awk '{gsub(/banana/, "orange"); print}' input.txt > temp.txt 
```

## sed 替换字符

```bash
sed '
s/rep_EchE05G/#e8f6fb*EchE05G/
s/rep_EchE04G/#4db77d*EchE04G/
s/rep_EchE03G/#fff229*EchE03G/
s/rep_EchE02G/#f3ab45*EchE02G/
s/rep_EchE01G/#f0717b*EchE01G/
' input.txt > output.txt
```

## sed与awk结合使用

```bash
awk '{$1 ="rep_" $1;print}' Ech_vs_Min.jcvi.simple |sed 's/rep_EchE06G/#824b9f*EchE06G/g;s/rep_EchE05G/#009fda*EchE05G/g;s/rep_EchE04G/#4db77d*EchE04G/g;s/rep_EchE03G/#fff229*EchE03G/g;s/rep_EchE02G/#f3ab45*EchE02G/g;s/rep_EchE01G/#f0717b*EchE01G/g' |sed 's/rep_//g' >Ech_vs_Min.jcvi_c.simple
```