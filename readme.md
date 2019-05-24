# 网络聊天室

## 功能
### 1. 用户注册和登录
* 用户凭借用户名和密码登录
* 用户利用用户名和密码进行注册
* 用户名唯一且不可更改
* 用户名和密码保存到数据库中

### 2. 用户添加好友和查看好友列表
* 可以通过用户名搜索用户，并添加好友
* 可以接收对方添加好友请求，决定接受还是拒绝
* 将好友资料保存到数据库中
* 查看好友列表

### 3. 用户与好友聊天和传输文件
* 点击好友头像发起聊天
* 与好友间收发消息
* 点击按钮与好友传输文件
* 群聊功能
* 群共享文件
* 将聊天记录保存到数据库中

### 4. 查看聊天记录
* 点击按钮进入查看聊天记录界面
* 通过时间查找聊天记录
* 通过关键字查找聊天记录
* 通过用户名查找聊天记录

### 5. 图形界面
* 登录界面
* 注册界面
* 好友列表及聊天窗口
* 个人设置界面
* 传输文件
* 查看聊天记录

## 设计
* 套接字：TCP
* 并发方案：多进程 Multiprocessing
* 数据库：
>* 用户表： id name passwd
>* 好友表：
>* 聊天记录表：
* 结构设计：
>* 封装方法：面向对象
>* 功能模块：Model及数据库，View图形界面， Control逻辑处理

## 具体实现
注册
> 客户端：点击注册，输入用户名和密码，发送登录消息