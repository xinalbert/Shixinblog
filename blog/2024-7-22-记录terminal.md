<!--
 * @Author: albertxin albert_xin@qq.com
 * @Date: 2024-07-23 15:39:15
 * @LastEditors: albertxin albert_xin@qq.com
 * @LastEditTime: 2024-07-26 09:36:12
 * @FilePath: /shixinblog/blog/2024-7-22-记录terminal.md
 * Copyright (c) albertxin by albert_xin@qq.com, All Rights Reserved. 
-->
# 利用bwa-mem2 进行比对

## 安装bwa-mem2

```bash
# 安装bwa-mem2
conda install -c bioconda bwa-mem2
```

## 对基因组建立索引

```bash
# 对基因组建立索引
bwa-mem2 index /path/to/reference.fa
```

## 对基因组建立faidx索引

```bash
# 对基因组建立faidx索引
samtools faidx /path/to/reference.fa
```

```bash
# 利用bwa-mem2 进行比对
bwa-mem2 mem -M -t 5 -R '@RG\tID:CSA\tLB:CSA\tPL:ILLUMINA\tSM:yourgenome' /path/to/reference.fa yourfastqfile_R1.fastq.gz yourfastqfile_R2.fastq.gz | samtools sort -O bam -@ 4 -o yourgenome_reseq.bam - && samtools index yourgenome_reseq.bam

Csa=yourgenome.fa
$bwa2 mem -M -t 5 -R '@RG\tID:CSA\tLB:CSA\tPL:ILLUMINA\tSM:$Csa' $Csa yourfastqfile_R1.fastq.gz yourfastqfile_R2.fastq.gz | samtools sort -O bam -@ 4 -o Csa_reseq.bam - && samtools index Csa_reseq.bam

Cfi=yourgenome.fa
$bwa2 mem -M -t 5 -R '@RG\tID:CSA\tLB:CSA\tPL:ILLUMINA\tSM:$Cfi' $Cfi yourfastqfile_R1.fastq.gz yourfastqfile_R2.fastq.gz | samtools sort -O bam -@ 4 -o Cfi_reseq.bam - && samtools index Cfi_reseq.bam
```


