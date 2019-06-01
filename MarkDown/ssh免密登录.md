

# 目的
为了不知每次登录服务器的时候都输入密码，实现ssh免密登录是一个很好地选择

# 理想操作
1.使用 `ssh-keygen`  命令在本地生成一对秘钥（Public/Private key）
2.使用 `ssh-copy-id username@your-service-ip` 命令将本地公钥拷贝到远程服务器上
3.使用 `ssh username@your-service-ip` 命令来连接远程服务器




