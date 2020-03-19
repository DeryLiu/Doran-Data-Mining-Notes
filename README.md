Doran的数据挖掘笔记
===
[**Gitlab** 地址](https://github.com/DeryLiu/Doran-Data-Mining-Notes)

[**在线阅读地址**](https://deryliu.github.io/Doran-Data-Mining-Notes/)

**说明**（2020-02-26）：本文档是Doran的学习进阶笔记。**`不对外负责`**

---

## RoadMap
* [100_基础知识](100_基础知识/README.md)
   * [110_SQL技能](100_基础知识/110_SQL技能/README.md)
     - [111_简单SQL](100_基础知识/111_简单SQL/README.md)
     - [112_中等SQL](100_基础知识/112_中等SQL/README.md)
   * [120_Python技能](100_基础知识/120_Python技能/README.md)
     - [121_Python基础](100_基础知识/121_Python基础/README.md)
     - [122_Python简单OJ](100_基础知识/122_Python简单OJ/README.md)
   * [130_机器学习](100_基础知识/130_机器学习/README.md)
     - [131_机器学习基础](100_基础知识/130_机器学习/131_机器学习基础.md)
     - [132_机器学习实践](100_基础知识/130_机器学习/132_机器学习实践.md)
     - [133_机器学习算法](100_基础知识/130_机器学习/133_机器学习算法.md)
   * [140_深度学习](100_基础知识/140_深度学习/README.md)
   * [150_自然语言处理](100_基础知识/150_自然语言处理/README.md)
   * [160_数学基础](100_基础知识/160_数学基础/README.md)
* [200_算法推导](200_算法推导/README.md)
   * [210_算法专题](200_算法推导/210_算法专题/README.md)
* [300_框架工具](300_框架工具/README.md)
   * [310_Echart](300_框架工具/310_Echart/README.md)
   * [320_XGBoost](300_框架工具/320_XGBoost/README.md)
   * [330_Tensorflow](300_框架工具/330_Tensorflow/README.md)
     - [331_TensorFlow基本概念](300_框架工具/330_Tensorflow/331_TensorFlow基本概念.md)
* [400_项目案例](400_项目案例/README.md)
   * [410_Kaggle](400_项目案例/410_Kaggle/README.md)
   * [440_量化交易](400_项目案例/440_量化交易/README.md)
     - [441_环境配置](400_项目案例/440_量化交易/441_环境配置.md)
* [500_面试准备](500_面试准备/README.md)
   * [510_数据库面试](500_面试准备/510_数据库面试/README.md)
     - [01_数据库初级](500_面试准备/510_数据库面试/01_数据库初级.md)
   * [520_数据挖掘面试](500_面试准备/520_数据挖掘面试/README.md)
     - [01_数据挖掘工程师面试_选择题](500_面试准备/520_数据挖掘面试/01_数据挖掘工程师面试_选择题.md)
     - [02_数据挖掘工程师面试_简答题](500_面试准备/520_数据挖掘面试/02_数据挖掘工程师面试_简答题.md)
     - [03_数据挖掘150道试题](500_面试准备/520_数据挖掘面试/03_数据挖掘150道试题.md)
   * [530_Python面试](500_面试准备/530_Python面试/README.md)
     - [01_阿里巴巴Python工程师真题](500_面试准备/530_Python面试/01_阿里巴巴Python工程师真题.md)
     - [02_面试必备25条Python知识点](500_面试准备/530_Python面试/02_面试必备25条Python知识点.md)
   * [540_Spark面试](500_面试准备/540_Spark面试/README.md)
     - [01_Spark问答合集](500_面试准备/540_Spark面试/01_Spark问答合集.md)
   * [550_机器学习面试](500_面试准备/550_机器学习面试/README.md)
   * [560_笔试面经经验](500_面试准备/560_笔试面经经验/README.md)
* [600_其它资料](600_其它资料/README.md)
   * [01_Gitlab配置](600_其它资料/01_Gitlab配置.md)

工具
---
- 在线 LaTeX 公式编辑器 http://www.codecogs.com/latex/eqneditor.php
- 在线表格转 HTML 语言 http://www.tablesgenerator.com/html_tables

常用命令
---
- 文件初始化 `gitbook init`
- 下载新插件 `gitbook install ./`
- 书籍编译 `gitbook build`
- 网页端查看 `gitbook serve`
- 生成pdf文件 `gitbook pdf`
- 打包文件 `gitbook build Doran-Data-Mining-Notes/outbook`
- html文件不能调转 修改outbook/gitbook/theme.js的`if(m)for(n.handler&&`
- 新建gh-pages分支 `git checkout -b gh-pages`
- 将分支push到仓库 `git push -u origin gh-pages`
- 切换到主分支 `git checkout master`
- 将book推送到分支 `git subtree push --prefix=_book origin gh-pages`
