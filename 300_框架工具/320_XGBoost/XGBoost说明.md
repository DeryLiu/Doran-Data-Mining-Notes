## XGBoost 简介
XGBoost：eXtreme Gradient Boosting
Gradient Boosting Machines(GBM) 的C++优化实现，快速有效
–深盟分布式机器学习开源平台(Distributed Machine Learning
Community， DMLC)的一个分支。

### 参数设置
#### 设置训练参数
```param = {'max_depth':2, 'eta':1, 'silent':0, 'objective':'binary:logistic' }```
- max_depth： 树的最大深度。缺省值为6，取值范围为：[1,∞]
- eta：为了防止过拟合，更新过程中用到的收缩步长。eta通过缩减特征
的权重使提升计算过程更加保守。缺省值为0.3，取值范围为：[0,1]
- silent: 0表示打印出运行时信息，取1时表示以缄默方式运行，不打印
运行时信息。缺省值为0
- objective： 定义学习任务及相应的学习目标，“binary:logistic” 表示
二分类的逻辑回归问题，输出为概率。

#### 设置boosting迭代计算次数
- num_round = 2
- bst = xgb.train(param, dtrain, num_round)
26