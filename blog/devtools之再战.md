1. 安装devtools又出现问题，提示如下：
```
rror: package or namespace load failed for ‘gert’ in dyn.load(file, DLLpath = DLLpath, ...):
 unable to load shared object '/home/zhushixin/miniconda3/envs/jupyter_lab/lib/R/library/00LOCK-gert/00new/gert/libs/gert.so':
  /home/zhushixin/miniconda3/envs/jupyter_lab/lib/R/library/00LOCK-gert/00new/gert/libs/gert.so: undefined symbol: getentropy
Error: loading failed
Execution halted
```
2. 尝试用conda安装部分依赖：conda install -c conda-forge libgit2，发现还是不行，最终放弃，使用conda安装devtools，成功！
```                                  
conda install conda-forge::r-devtools    
```
还得是conda，折腾一下午了！终于成功了！