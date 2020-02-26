酒店底层表说明文档
===
[**Gitlab** 地址](http://git.dev.sh.ctripcorp.com/Commerce_platform/hotel_database_manual)

[**在线阅读地址**](http://10.32.195.37:8001)

[**PDF版下载地址**](http://git.dev.sh.ctripcorp.com/Commerce_platform/hotel_database_manual/blob/master/outbook/book.pdf)

[**HTML下载地址**](http://git.dev.sh.ctripcorp.com/Commerce_platform/hotel_database_manual/blob/master/outbook)

**说明**（2020-02-21）：本文档是酒店(国内外)底层数据表的整理和说明。**`不建议外传`**

---

## RoadMap
* [序言](chapter00/preface.md)
* [一、基础业务](chapter01/README.md)
   * [01_海外业务](chapter01/01_海外业务.md)
   * [02_国内业务](chapter01/02_国内业务.md)
* [二、逻辑说明](chapter02/README.md)
   * [01_基础逻辑](chapter02/01_基础逻辑.md)
   * [02_订单结算](chapter02/02_订单结算.md)
   * [03_爬虫方案](chapter02/03_爬虫方案.md)
   * [04_比价覆盖房态](chapter02/04_比价覆盖房态.md)
* [三、静态信息](chapter03/README.md)
   * [01_静态信息](chapter03/01_静态信息.md)
* [四、数据字典](chapter04/README.md)
   * [01_基础表说明](chapter04/01_基础表说明.md)
   * [02_酒店房型数据字典](chapter04/02_酒店房型数据字典.md)
   * [03_动态信息数据字典](chapter04/03_动态信息数据字典.md)
   * [04_静态信息数据字典](chapter04/04_静态信息数据字典.md)
* [五、附录文件](chapter05/README.md)
   * [01_Gitlab配置](chapter05/01_Gitlab配置.md)

工具
---
- 在线 LaTeX 公式编辑器 http://www.codecogs.com/latex/eqneditor.php
- 在线表格转 HTML 语言 http://www.tablesgenerator.com/html_tables

常用命令
---
- 文件初始化 gitbook init
- 下载新插件 gitbook install ./
- 书籍编译 gitbook build
- 网页端查看 gitbook serve
- 生成pdf文件 gitbook pdf
- 打包文件 gitbook build hotel_database_manual hotel_database_manual/outbook
- html文件不能调转
  - outbook/gitbook/theme.js
  - 将 `if(m)for(n.handler&&` 修改为 `if(false)for(n.handler&&`
