nosql 讲解 
# 为什么使用Nosql
## 1、 为什么使用nosql

大数据时代，一般的数据库无法进行分析处理了
2006 hadoop
spring boot，spring cloud

90年代，一个基本的问题就是访问量一般不会太大，单个数据库完全足够。那个时候更多的是使用静态的HTML。

思考一下：这种情况，整个网站的瓶颈是什么？

> 1、数据量如果太大，一个机器放不下
>
> 2、数据的索引（B+tree），一个机器内存放不下
>
> 3、访问量（读写混合），一个服务器受不了

## 2、缓存  Memcache + Mysql + 垂直拆分(读写分离)

网站80%的时间都是在查数据，每次都要出查询数据库的话十分的麻烦，我们希望减轻数据库的压力，可以使用缓存来保证效率！

发展过程：优化数据库结构和索引---文件缓存I/O -Memcache(当前最热门的技术)

![1589349397740](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1589349397740.png)

## 3、读写分离+水平拆分+mysql集群

== 本质：数据库就是读和写 ==

myisam：表锁

Innodb：行锁

## 4、如今最近的时代

mysql等关系型数据库不够用了，数据量大，变化快。

关系型数据库和菲关系型数据库的差别？

目前互联网基本项目

![1589350411834](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1589350411834.png)

为什么使用nosql

# 什么是nosql

nosql = not only sql (不仅仅是sql)

关系型数据库：表格 行 列 （POI）

数据类型，个人信息、社交网络、地理位置，需要横向扩展 Map<String, Object>

## nosql 特点

> 1、方便扩展（数据之间没有关系）
>
> 2、大数据高性能（redis 8万/s nosql的缓存记录集
>
> 3、数据类型是多样性的（不需要事先设计数据库！睡去随用！4、RDBMS nosql）
>
> > RDBMS
> >
> > - 结构化数据
> > - sql
> > - 数据和关系都存在单独的表中
> > - 严格的一致性
>
> > nosql
> >
> > - 不仅仅是数据
> > - 没有固定的查询语言
> > - 键值对存储列存储
> > - CAP 原理和BASE
> > - 高可用 高性能 高可扩

3V+3高

海量 多样 实时



# 阿里巴巴演进模式

敏捷开发 极限编程

![1589352279437](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1589352279437.png)

没有什么是加一层解决不了的

```html
1、商品的基本信息
名称 截个 商家信息学 关系型数据库就可以解决了 mysql oracle IOE？ - 王坚 《阿里云的这群疯子》
2、商品的描述 评论 （文字比较多）
文档型数据中，mongoDB
3、图片
分布式文件系统fastDFS，google的gfs hadoop 的hdfs 阿里云的 oss
4、商品的关键字 
搜索引擎 solr elasticsearch
Isearch 多隆（了解一些技术大佬）
所有牛逼的人都有一点苦逼的岁月，但是你只要想sb意向去坚持，终将牛逼
5、商品热门的信息
内存数据库 redis tair memcache
6、是商品的交易，外部的字符接口
三方应用
```

大型互联网的应用问题

- 数据类型太多了
- 数据源繁多 经常重构

![1589352732915](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1589352732915.png)

![1589352765469](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1589352765469.png)

# nosql的四大分类

KV键值对：

- 新浪：redis
- 美团：redis tair 
- 阿里 百度 redismemcache

文档信息数据库（bson json一样）

- mongodb 是一个基于分布式文件存储的数据库 c++编写，主要主要用来处理大量的文档！
- mongodb是一个基于关系型数据库和菲关系型数据中的中间产品，mongodb是菲关系型数据库功能最丰富的的，最像关系型数据库

列存储数据库

- hbase
- 分布式文件系统

图关系型数据库

- 他不是村图形，放的是关系， 

![1589353090727](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\1589353090727.png)

追求幸福 探索未知（努力学习不要被社会抛弃）

