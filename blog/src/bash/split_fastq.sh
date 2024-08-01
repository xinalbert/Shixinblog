#!/bin/bash
###
 # @Author: albertxin albert_xin@qq.com
 # @Date: 2024-08-01 13:00:18
 # @LastEditors: albertxin albert_xin@qq.com
 # @LastEditTime: 2024-08-01 13:51:06
 # @FilePath: /shixinblog/blog/src/bash/split_fastq.sh
 # Copyright (c) albertxin by albert_xin@qq.com, All Rights Reserved. 
### 

# 默认参数
input_file=""
num_parts=3
output_path=""

# 解析命令行参数
while getopts "i:n:o:" opt; do
  case ${opt} in
    i )
      input_file=$OPTARG
      ;;
    n )
      num_parts=$OPTARG
      ;;
    o )
      output_path=$OPTARG
      ;;
    \? )
      echo "Invalid option: -$OPTARG" 1>&2
      exit 1
      ;;
    : )
      echo "Invalid option: -$OPTARG requires an argument" 1>&2
      exit 1
      ;;
  esac
done
shift $((OPTIND -1))

# 检查必要的参数
if [ -z "$input_file" ] || [ -z "$output_path" ]; then
    echo "Usage: $0 -i <input_file.fq> -n <num_parts> -o <output_path>"
    exit 1
fi

# 创建输出路径
mkdir -p "$output_path"

# 获取输入文件名（不包括扩展名）
input_base=$(basename "$input_file" .fq)

# 计算总行数和每个部分的行数
total_lines=$(wc -l < "$input_file")
lines_per_part=$((total_lines / num_parts / 4 * 4))

# 使用 split 命令拆分文件
split -l $lines_per_part "$input_file" "$output_path/split_part_"

# 重命名拆分后的文件

for i in $(seq 1 $num_parts); do
    part_file=$(ls $output_path/split_part_* | head -n $i | tail -n 1)
    mv $part_file $output_path/${input_base}_part${i}.fq
done

echo "Split $input_file into $num_parts parts in $output_path."
