## 基本概念

TensorFlow 其實在意思上是要用兩個部分來解釋，Tensor 与 Flow：

Tensor：是中文翻譯是張量，其實就是一個n維度的陣列或列表。如一維 Tensor 就是向量，二維 Tensor 就是矩陣等等.
Flow：是指 Graph 運算過程中的資料流.

使用图 (graph) 来表示计算任务.
在被称之为 会话 (Session) 的上下文 (context) 中执行图.
使用 tensor 表示数据.
通过 变量 (Variable) 维护状态.
使用 feed 和 fetch 可以为任意的操作(arbitrary operation) 赋值或者从其中获取数据

在TensorFlow中，使用图（graphs）来表示计算任务，图（graphs）中的节点称之为op（operation），一个op获得0个或者多个tensor，执行计算，产生0个或多个tensor，tensor看作是一个n维的数组或列表。图必须在会话（session）里启动运行。

![TensorFlow结构](/_img/TensorFlow结构.png)
