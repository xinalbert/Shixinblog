# 安装r包devtools所遇到的问题
## 问题经理
最近我在安装R语言的包devtools时，遇到了一些问题，下面是我的解决过程。
## 问题描述

1. 下载devtools包时，提示下载失败，提示信息如下：
```
Warning in install.packages :Error: package ‘usethis’ 2.1.5 was found, but >= 2.1.6 is required by ‘devtools’
```
2. 尝试使用devtools::install_version("usethis")命令安装usethis包，提示信息如下：
```
Error: package ‘fs’ was installed before R 4.0.0: please re-install it
Execution halted
```
3.  尝试使用install.packages("fs")命令安装fs包，将fs安装成功后，继续安装usethis包，提示信息如下：
```Error: package ‘rlang’ was installed before R 4.0.0: please re-install it
Execution halted
```
4. 尝试使用install.packages("rlang")命令安装rlang包，将rlang安装成功后，继续安装usethis包，提示信息如下：
```Error: package ‘glue’ was installed before R 4.0.0: please re-install it
Execution halted
```
5. 尝试使用install.packages("glue")命令安装glue包，将glue安装成功后，继续安装usethis包，提示信息如下：
```
Error: package ‘lifecycle’ was installed before R 4.0.0: please re-install it
Execution halted
```
6.   尝试使用install.packages("lifecycle")命令安装lifecycle包，将lifecycle安装成功后，继续安装usethis包，提示信息如下：
```Error: package ‘purrr’ was installed before R 4.0.0: please re-install it
Execution halted
```
7. 尝试使用install.packages("purrr")命令安装purrr包，出现错误提示信息如下：
```
Error: package ‘cli’ was installed before R 4.0.0: please re-install it
Execution halted
```
8. 尝试使用install.packages("cli")命令安装cli包，安装成功，继续安装purrr包，提示信息如下：
```
Error: package ‘magrittr’ was installed before R 4.0.0: please re-install it
Execution halted
```
9. 尝试使用install.packages("magrittr")命令安装magrittr包，安装成功，继续安装purrr包，成功将purr包安装成功继续安装usethis包，成功将usthis包安装，继续安装devtools包，提示信息如下：
```
Error: package ‘ellipsis’ was installed before R 4.0.0: please re-install it
Execution halted
```
10. 尝试使用install.packages("ellipsis")命令安装ellipsis包，安装成功，继续安装devtools包，提示信息如下：
```
Warning message:
package ‘ellipsis’’ is not available for this version of R

A version of this package for your version of R might be available elsewhere,
see the ideas at
https://cran.r-project.org/doc/manuals/r-patched/R-admin.html#Installing-packages 
```
11. 尝试修改镜像重新安装改包 install.packages('ellipsis', dependencies=TRUE, repos='http://cran.rstudio.com/')，成功安装ellipsis包，继续安装devtools包，提示信息如下：
```
Error: package ‘memoise’ was installed before R 4.0.0: please re-install it
Execution halted
```
12. 尝试使用install.packages("memoise")命令安装memoise包，安装成功，继续安装devtools包，提示信息如下：
```
Error: package ‘cachem’ was installed before R 4.0.0: please re-install it
Execution halted
```
13. 尝试使用install.packages("cachem")命令安装cachem包，安装成功，继续安装memoise包，成功安装memoise包，继续安装devtools包，提示信息如下：
```Error: package ‘miniUI’ was installed before R 4.0.0: please re-install it
Execution halted
```
14. 尝试使用install.packages("miniUI")命令安装miniUI包，提示信息如下：
```
Error: package ‘shiny’ was installed before R 4.0.0: please re-install it
Execution halted
```
15. 尝试使用install.packages("shiny")命令安装shiny包，提示信息如下：
```ror: package ‘R6’ was installed before R 4.0.0: please re-install it
Execution halted
``` 
16. 尝试使用install.packages("R6")命令安装R6包，安转成功，继续安装shiniy包，提示信息如下：
```
Error: package ‘htmltools’ was installed before R 4.0.0: please re-install it
Execution halted
```
17. 尝试使用install.packages("htmltools")命令安装htmltools包，安装成功，继续安装shiny包，提示信息如下：
```
Error: package ‘httpuv’ was installed before R 4.0.0: please re-install it
Execution halted
```
18. 尝试使用install.packages("httpuv")命令安装httpuv包，提示信息如下：
```
Error: package ‘Rcpp’ was installed before R 4.0.0: please re-install it
Execution halted
```
19. 尝试使用install.packages("Rcpp")命令安装Rcpp包，提示信息如下：
```
Error : package ‘codetools’ was installed before R 4.0.0: please re-install it
Error: unable to load R code in package ‘Rcpp’
Execution halted
```
20. 尝试使用install.packages("codetools")命令安装codetools包，安装成功，继续安装Rcpp包，安装成功，继续安装httpuv包，提示信息如下：
```
Error: package ‘later’ was installed before R 4.0.0: please re-install it
Execution halted
```
21. 尝试使用install.packages("later")命令安装later包，安装成功，继续安装httpuv包，提示信息如下：
```
Error: package ‘promises’ was installed before R 4.0.0: please re-install it
Execution halted
```
22. 尝试使用install.packages("promises")命令安装promises包，安装成功，继续安装httpuv包，成功安装httpuv包，继续安装shiny包，提示信息如下：
```
Error: package ‘mime’ was installed before R 4.0.0: please re-install it
Execution halted
```
23. 尝试使用install.packages("mime")命令安装mime包，安装成功，继续安装shiny包，提示信息如下：
```
Error: package ‘xtable’ was installed before R 4.0.0: please re-install it
Execution halted
```
24. 尝试使用install.packages("xtable")命令安装xtable包，安装成功，继续安装shiny包，安装成功，继续安装miniUI，安装成功，继续安装devtools,提示信息如下：
```
Error: package ‘pkgbuild’ was installed before R 4.0.0: please re-install it
Execution halted
```
25. 尝试使用install.packages("pkgbuild")命令安装pkgbuild包，安装成功，继续安装devtools，提示信息如下：
```
Error: package ‘pkgload’ was installed before R 4.0.0: please re-install it
Execution halted
```
26. 尝试使用install.packages("pkgload")命令安装pkgload包，提示信息如下：
```
Error: package ‘withr’ was installed before R 4.0.0: please re-install it
Execution halted
```
27. 尝试使用install.packages("withr")命令安装withr包，安装成功，继续安装pkgload包，提示信息如下：
```
Error: package ‘testthat’ was installed before R 4.0.0: please re-install it
Execution halted
```
28. 尝试使用install.packages("testthat")命令安装testthat包，提示信息如下：
```
Error: package ‘brio’ was installed before R 4.0.0: please re-install it
Execution halted
```
29. 尝试使用install.packages("brio")命令安装brio包，安装成功，继续安装testthat包，安装成功，继续安装pkgload包，提示信息如下：
```
Error: package ‘desc’ was installed before R 4.0.0: please re-install it
Execution halted
```
30. 尝试使用install.packages("desc")命令安装desc包，安装成功，继续安装pkgload包，提示信息如下：
```
Error: package ‘rprojroot’ was installed before R 4.0.0: please re-install it
Execution halted
```
31. 尝试使用install.packages("rprojroot")命令安装rprojroot包，安装成功，继续安装pkgload包，安装成功，继续安装devtools，提示信息如下：
```
Error: package ‘htmlwidgets’ was installed before R 4.0.0: please re-install it
```
32. 尝试使用install.packages("htmlwidgets")命令安装htmlwidgets包，安装成功，继续安装devtools，提示信息如下：
```Error: package ‘stringr’ was installed before R 4.0.0: please re-install it
Execution halted
```
33. 尝试使用install.packages("stringr")命令安装stringr包，提示如下信息：
```
Error: package ‘stringi’ was installed before R 4.0.0: please re-install it
Execution halted
```
34. 尝试使用install.packages("stringi")命令安装stringi包，提示信息如下：
```
configure: error: in `/share/nas6/zhouxy/tmpdir/RtmpSKTwpn/R.INSTALL37114519c348e/stringi':
configure: error: C++ compiler cannot create executables
See `config.log' for more details
ERROR: configuration failed for package ‘stringi’
```
35. 尝试使用利用conda安装gcc和gxx，然后再次尝试安装，仍然失败，采用conda包管理进行安装conda install r-stringi -y，安装成功，继续安装devtools，提示信息如下：
```
Error: package ‘stringr’ was installed before R 4.0.0: please re-install it
Execution halted
```
36. 查阅资料后，利用 .libPaths()， 查看R包的位置，然后.libPaths(R.home("/home/zhushixin/R/x86_64-conda-linux-gnu-library/4.4"))更改到所用R语言的包位置，重新安装devtools，成功安装devtools，成功安装usethis包，成功安装devtools包。

## 总结
初始问题：在尝试安装devtools时，提示需要更新usethis包至2.1.6或更高版本。

依赖性问题：在尝试更新usethis包时，发现其依赖的多个包（如fs、rlang、glue、lifecycle、purrr等）需要更新或重新安装。

循环依赖：在尝试安装或更新这些依赖包的过程中，不断遇到新的依赖包需要更新或重新安装，形成了一个循环依赖链。

编译问题：在安装stringi包时，出现了编译错误，提示C++编译器无法创建可执行文件。

解决编译问题：您尝试使用conda安装了gcc和g++，但问题依旧存在。最后通过conda安装r-stringi包成功解决了编译问题。

环境设置：通过使用.libPaths()函数，更改了R包库的路径，指向了正确的R版本对应的库路径。

最终解决：在设置正确的库路径后，成功安装了devtools包以及之前失败的其他依赖包。

整个过程中，您遇到的问题提示了R包管理中的一些常见问题，如版本依赖、循环依赖、编译环境配置等。解决这些问题需要对R的包管理机制有深入的理解，并且能够适当地调整编译环境和包库路径。您的经历也展示了在面对复杂的软件依赖问题时，逐步排查和解决单个问题的重要性。