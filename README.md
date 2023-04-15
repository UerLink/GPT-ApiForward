# GPT-ApiForward
使用Frask框架制作一个接口，将openai的接口经过转发到没有外网的环境中使用

```
openai -> 外网服务器 -> 客户端
```
**项目起因：** 
GPT很好用，但是使用openai提供的接口，又必须开魔法，用着不太方便，干脆弄一个外网服务器当中间人，帮忙转发问题和回答。

**项目缺点：**
1. 其实可以直接进行转发的，但是我不会
2. 流式传输用不了
3. 上下文回答没了（其实这个还好，这个项目是为另一个项目打基础，所以不太需要上下文回答）


### 服务器端部署步骤

#### 安装python和虚拟环境(venv)
```shell
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
```

#### 创建虚拟环境
1. 新建一个空白文件夹，并进入
```shell
mkdir flask_app && cd flask_app
```
2. 创建一个名为venv的虚拟环境
```shell
python3 -m venv venv
```

#### 进入/退出 虚拟环境
- 进入
```shell
source venv/bin/activate
```
- 退出
```shell
deactivate
```

#### 下载Flask
1. 进入虚拟环境，使用pip工具安装flask
```shell
pip install Flask
```
2. 验证安装是否成功
```shell
python -m flask --version
```

3. 安装代码运行需要的第三方库
```shell
pip install json
pip install requests
pip install openai
```


#### 部署
1. 拷贝服务器代码的main.py 到 flask_app 内

2. 设置**FLASK_APP**环境变量
```shell
export FLASK_APP=main.py
```
3. 运行应用
```shell
python3 main.py
```
4. 搞定

### 客户端部署步骤
#### 安装python和第三方库
```shell
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-json
sudo apt install python3-requests
```
#### 拷贝客户端代码文件 client.py 执行命令
```shell
python3 client.py
```
