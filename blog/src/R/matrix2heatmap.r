#!/usr/bin/env Rscript

# 加载必要的包
library(optparse)

# 定义命令行选项
option_list <- list(
  make_option(c("-i", "--infile"), type="character", default=NULL, 
              help="Input file name", metavar="character"),
  make_option(c("-o", "--outfig"), type="character", default="sample.IBD.heatmap.pdf", 
              help="Output figure file name [default= %default]", metavar="character")
)

# 解析命令行参数
opt_parser <- OptionParser(option_list=option_list)
opt <- parse_args(opt_parser)

# 检查是否提供了输入文件
if (is.null(opt$infile)){
  print_help(opt_parser)
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
}

# 读取IBD矩阵数据
ibd_matrix <- as.matrix(read.csv(opt$infile, row.names = 1, header = TRUE))

# 自定义颜色映射（红到白到蓝）
my_palette <- colorRampPalette(c("#f0f6fd", "#4b95c5", "#0a3169"))(100)

# 打开图形设备
pdf(file = opt$outfig, width = 11.7, height = 8.3)

# 绘制热图
heatmap(ibd_matrix, 
        col = my_palette, 
        scale = "none", 
        # margins = c(10, 10),
        main = "IBD Heatmap")

# 关闭图形设备
dev.off()

print(paste("Heatmap saved to", opt$outfig))
