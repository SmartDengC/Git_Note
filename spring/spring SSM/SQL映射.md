## 1、#与$的区别
一、#{}将传入的数据都当成一个字符串，会对自动传入的数据加一个双引号，例如：
```
ordder by #{id}
// 如果传入的id是11， 则sql解析为
order by "11"
```
二、${} 将传入的数据直接显示生成在sql中，例如：
```
order by ${id}
// 若果传入的id是11，则sql解析成
order by 11
```
三、#方式能够很大程度的防止sql注入，$方式无法防止sql注入
`#`为什么能够防止sql注入？

## 2、resultMap
```java
<resultMap id = "userMap" type="AyUser">
    <id property="id" column="id"/> // 数据的id/>
    <result property="name" column="name"/>
    <result property="password" column="password"/>
</resultMap>
```