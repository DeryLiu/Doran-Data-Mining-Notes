[面试题地址](https://developer.aliyun.com/ask/135906?utm_content=g_1000088313)

1. 如何使用spark将kafka主题中的writeStream数据写入hdfs？
```scala
spark.read
.format("kafka")
.option("kafka.bootstrap.servers", url)
.option("subscribe", topic)
.load()
.selectExpr("CAST(value AS String)")
.write
.format(fileFormat)
.save(filePath)
```
