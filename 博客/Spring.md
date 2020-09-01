知识汇总图

netty 是什么？

Netty是一个高性能的异步时间驱动的网络通信框架，

ORM object Relation Mapping 对象关系映射，把面向对象的概念跟数据库中的表概念对应起来。

RPC 框架是什么？

### 5个常见的spring框架

1 spring framework

ioc context bean 管理 springmvc

2 spring boot

3 spring data

数据访问及操作的工具，封装了多种数据源的操作能力 jdbc redis

4 spring cloud

微服务的集合

5 spring security

![image-20200829052702810](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200829052702.png)

IOC

context 上下文和bean

aop

aop的实现是通过代理实现的。

jdk代理 和 CGLIB代理



![image-20200829053026637](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200829053026.png)

### spring中的机制和实现

1、aop

2、placeHolder动态替换

3、事务

4、核心接口类

applicationContext ioc的真格应用上下文

beanFactory

BeanWrapper

FactoryBean

5 、scope

单例 多例 http session global-session

6、事件机制

### spring应用相关

#### 注解

a 类型注解

controller service

其中Component和Bean的区别

- @Component注解在类上使用表明这个类是个组件类，需要Spring为这个类创建bean。
- @Bean注解使用在方法上，告诉Spring这个方法将会返回一个Bean对象，需要把返回的对象注册到Spring的应用上下文中。

b 设置类注解

@Autowire 和@Qualifier

c web类注解

@RequestMapping @GetMapping @PostMapping

自动装配机制



