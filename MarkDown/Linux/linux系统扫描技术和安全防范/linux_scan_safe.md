# Linux系统扫描和安全防范

# 源码包的编译过程
![](./pictures/binaryPackage.png)
|编译方式|命令|产物|
|----|----|----|
|检测配置|./configure|Makefile|
|编译|make|二进制可执行文件|
|安装|make install |安装到指定目录|
# 主机扫描技术

## fping
### 安装
1、下载fping的源码包，官方网站为：http://fping.org/  
2、解压后进入该目录  
3、进行源码包安装过程  

### 作用和特点
作用：批量的给目标主机发送ping请求，测试主机是否存活。    
特点：并行发送，结果易读。  

### 操作
......

## hping

### 特点
支持使用的TCP/IP数据包组装分析工具

### 安装
1、源码包下载，下载地址 http://www.hping.org/  
2、`./configure--->make---->make install`(hping依赖libpacp-devel)  
3、可能在安装的过程中会遇见错误  

- 报错1：
```
libpcap_stuff.c:19:21: error: net/bpf.h: No such file or directory
make: *** [libpcap_stuff.o] Error 1
```  
解决办法：ln -sf /usr/include/pcap-bpf.h /usr/include/net/bpf.h  
- 报错2：
```
al/lib -lpcap  -ltcl -lm -lpthread
/usr/bin/ld: cannot find -ltcl
collect2: ld returned 1 exit status
make: *** [hping3] Error 1
```
解决办法：yum -y install tcl tcl-devel


# 路由扫描技术

## traceroute
### 操作
## mtr


# 批量服务扫描技术

## nmap

## ncat

# 预防恶意的扫描和攻击

## 1、SYN攻击

## 2、DDOS攻击

## 3、恶意攻击
----------------------
tracert
nmap
nc

主机扫描
fping 批量ping相应主机
-a 存活的主机
-u 没有存活的主机
-g 主机段
-f fping一个文件，里面保存了主机抵质

hping
-p 

路由扫描  
查询一个主机到另外一个主机的经过的路由的跳数，及数据延迟情况。  
traceroute mtr  
-T -p -I -n

nmap ncat
ping 扫描
TCP 半扫描
TCP 全扫描
UDP扫描

wzv