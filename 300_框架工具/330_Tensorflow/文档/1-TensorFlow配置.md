## 环境配置安装

### 云配置

#### Google Cloud

##### CPU配置
- 系统：Ubuntu 18.04 LTS
- 防火墙：允许HTTP和HTTPS流量
- 外部IP：VPC网络-外部IP地址-类型由临时改为静态
- 创建防火墙规则：
    1. 目标：网络中所有的实例
    2. 来源IP地址范围：0.0.0.0/0
    3. tcp端口号：6000-6500
    
- 安装python环境
```shell script
sudo apt-get install python3
sudo apt-get install software-properties-common
sudo apt-add-repository uniserse
sudo apt-get update
sudo apt-get install python3-pip
```
- 安装虚拟环境
```shell script
sudo pip3 install -U virtualenv
mkdir doranEnv
cd doranEnv
virtualenv --system-site-packages -p python3 ./tf_py3
source tf_py3/bin/activate
```
- 安装TensorFlow
```shell script
pip install tensorflow
pip install numpy pandas matplotlib sklearn jupyter
```

- 配置jupyter
```shell script
jupyter notebook --generate-config
vim ./jupyter/jupyter_notebook_config.py
```
```markdown
c = get_config()
c.NorebookApp.ip = '*'
c.NorebookApp.open_browser = False
c.NorebookApp.port = 6003

c.NorebookApp.allow_remote_access = True
```

##### GPU配置

- [TensorFlow支持](https://www.tensorflow.org/install/gpu)

- 选择对应系统的支持代码复制成脚本去安装
```shell script
sh +x install.sh
``` 

- 其余步骤一致

#### AWS Cloud

```shell script
``` 