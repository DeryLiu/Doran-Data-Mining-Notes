
set -e

cd /home/powerop/work/

kinit -kt /etc/keytab/权限名.keytab 权限名

echo `date`" start the python script."

#执行算法
CurrentDate=`date +%Y-%m-01`

# python ./文件.py

ifPyOK=`echo $?`
echo ${ifPyOK}

if [ ${ifPyOK} != 0 ];then 
   echo "python script is wrong,please check."
   exit ${ifPyOK}
fi

hive -e "use 库;ALTER TABLE 表 DROP if exists PARTITION (preddate='${CurrentDate}');" --define CurrentDate=${CurrentDate}
{
  #mkdir dir
  hadoop fs -mkdir hdfs://ns/user/hive/warehouse/库.db/表/preddate=${CurrentDate}
}

#上传文件到hdfs
hadoop fs -put ./文件.txt hdfs://ns/user/hive/warehouse/库.db/表/preddate=${CurrentDate}
hadoop fs -chmod -R 777 hdfs://ns/user/hive/warehouse/库.db/表/preddate=${CurrentDate}
hadoop fs -ls hdfs://ns/user/hive/warehouse/库.db/表/preddate=${CurrentDate}
echo "检查点ok！"

#映射文件
hive -e "use 库;alter table 表 add if not exists partition (preddate='${CurrentDate}')  
location 'hdfs://ns/user/hive/warehouse/库.db/表/preddate=${CurrentDate}';" --define CurrentDate=${CurrentDate}

echo "映射文件:OK"
