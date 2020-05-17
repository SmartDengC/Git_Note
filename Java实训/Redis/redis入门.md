# Redis 



##  Redis 能干什么？

1、内存存储、持久化、内存中断点即丢失，所以说持久化很重要（rdb、aof）

2、效率高，可用于高速缓存

3、发布订阅系统

4、地图信息分析

5、计时器，计数器（浏览量）

6、.....

## Redis 特性

1、多样的数据类型

2、持久化

3、集群

4、事务

## 学习中需要用到的东西

1、公众号

2、官网：redis.cn

redis 推荐在linux服务器上搭建

默认端口：6379

## Linux 安装Redis

1、下载安装包

2、解压

3、yum install gcc-c++

4、make  make install

5、redis默认的安装路径 /usr/local/bin

6、redis默认不是后台启动，需要修改redis.conf  daemonize yes （为后台启动）

7、启动redis服务redis-server /kconfig/redis.conf