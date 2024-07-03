# 清空环境
rm(list=ls())

# 包导入
library(ggplot2)
library(reshape2)
library(data.table)
library(dplyr)

# 函数定义：读取和预处理数据
read_and_preprocess_data <- function(file_path) {
  # 读取数据
  data_load <- fread(file_path, sep = '\t', header = TRUE)
  # 替换列名中的点为空格
  colnames(data_load) <- gsub("\\.", " ", colnames(data_load))
  
  # 定义样本顺序
  order_str <- rev(c('Bni', 'Rsa', 'Bra', 'Ovi', 'Aal', 'Lal', 'Ech', 'Ath', 'Aly', 'Min', 'Aar'))
  
  # 选择需要的列并转换样本列为因子
  data_draw <- data_load %>%
    select(Samples, `Unique families`, `Single copy orthologs`, `Multiple copy orthologs`, `Other orthologs`, `Unassigned genes`) %>%
    mutate(Samples = factor(Samples, levels = order_str))
  
  # 将数据转换为长格式
  data_to_draw <- melt(data_draw, id.vars = 'Samples')
  data_to_draw$variable <- factor(data_to_draw$variable, levels = rev(c('Unique families', 'Single copy orthologs', 'Multiple copy orthologs', 'Other orthologs', 'Unassigned genes')))
  
  return(data_to_draw)
}

# 函数定义：绘制堆积图
plot_stacked_bar <- function(data_to_draw) {
  # 创建堆积图
  p1 <- ggplot(data_to_draw, aes(y = Samples, x = value, fill = variable)) +
    geom_bar(stat = 'identity', position = "stack", width = 0.6) +
    theme_classic() +
    labs(x = '', y = '') +
    scale_fill_manual(values = rev(c("#664497", "#e61f19", '#f39f16', '#3c81c4', '#2e8555'))) +
    theme(legend.title = element_blank())
  
  return(p1)
}

# 函数定义：保存图像
save_plots <- function(plot, file_name) {
  ggsave(paste0(file_name, '.svg'), height = 4, width = 7, plot = plot)
  ggsave(paste0(file_name, '.png'), height = 4, width = 7, plot = plot)
  ggsave(paste0(file_name, '.pdf'), height = 4, width = 7, plot = plot)
}

# 主函数
main <- function(file_path, output_file_name) {
  # 读取和预处理数据
  data_to_draw <- read_and_preprocess_data(file_path)
  
  # 绘制堆积图
  plot <- plot_stacked_bar(data_to_draw)
  
  # 保存图像
  save_plots(plot, output_file_name)
  
  # 关闭设备
  dev.off()
}

# 运行主函数
main("C:/Users/Administrator/Downloads/gene_family_stat.xls", "gene_family_stat")
