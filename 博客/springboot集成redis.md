# SpringBoot集成Redis

本博客内容，谨慎模仿！！属于不完全体。

## 1、创建SpringBoot项目

![image-20200901164752004](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200901164759.png)

前面的步骤我适当的省略了，选择这两个dependencles，就相当于与给项目pom.xml添加如下依赖：

```xml
		<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
```

这个时候你就得到了一个有web和data-redis的springboot项目了。

## 2、测试项目是否正常运行

这个时候找到项目的入口，玩springboot的童鞋应该都知道的。出现这个表示成功

![image-20200901165426969](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200901165427.png)

## 3、配置redis，并做测试

在application.properties中简单设置redis的host（服务地址）和port（端口）

```properties
spring.redis.host=192.168.44.178
spring.redis.port=6379
```

然后在springboot默认的测试类里面写代码测试

![image-20200901170224587](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200901170224.png)

## 4、Redis做缓存

### ① 编写一个City的实体类

```java
package com.jet5devil.springbootredistest.pojo;

import java.io.Serializable;

public class City implements Serializable {
    private int cityId;
    private String cityName;
    private String cityIntroduce;
    public City(int cityId, String cityName, String cityIntroduce) {
        this.cityId = cityId;
        this.cityName = cityName;
        this.cityIntroduce = cityIntroduce;
    }
    public City(String cityName, String cityIntroduce) {
        this.cityName = cityName;
        this.cityIntroduce = cityIntroduce;
    }
    public City() {
    }
    public int getCityId() {
        return cityId;
    }
    public void setCityId(int cityId) {
        this.cityId = cityId;
    }
    public String getCityName() {
        return cityName;
    }
    public void setCityName(String cityName) {
        this.cityName = cityName;
    }
    public String getCityIntroduce() {
        return cityIntroduce;
    }
    public void setCityIntroduce(String cityIntroduce) {
        this.cityIntroduce = cityIntroduce;
    }
}

```

### ② 定义一个RedisService类

```java
package com.jet5devil.springbootredistest.service;

import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.data.redis.serializer.RedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;
import org.springframework.stereotype.Service;
import javax.annotation.Resource;

@Service
public class RedisService {
    @Resource
    private RedisTemplate<String,Object> redisTemplate;
    public void set(String key, Object value) {
        //更改在redis里面查看key编码问题
        RedisSerializer redisSerializer =new StringRedisSerializer();
        redisTemplate.setKeySerializer(redisSerializer);
        ValueOperations<String,Object> vo = redisTemplate.opsForValue();
        vo.set(key, value);
    }
    public Object get(String key) {
        ValueOperations<String,Object> vo = redisTemplate.opsForValue();
        return vo.get(key);
    }
}

```



### ③ 编写一个CityController类

```java
package com.jet5devil.springbootredistest.controller;

import com.jet5devil.springbootredistest.pojo.City;
import com.jet5devil.springbootredistest.service.RedisService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CityController {

    @Autowired
    private RedisService redisService;
    
    //http://localhost:8888/saveCity?cityName=北京&cityIntroduce=中国首都&cityId=1
    @GetMapping(value = "saveCity")
    public String saveCity(int cityId,String cityName,String cityIntroduce){
        City city = new City(cityId,cityName,cityIntroduce);
        redisService.set(cityId+"",city);
        return "success";
    }

    //http://localhost:8888/getCityById?cityId=1
    @GetMapping(value = "getCityById")
    public City getCity(int cityId){
        City city = (City) redisService.get(cityId+"");
        return city;
    }
}
```



### ④ 编写一个RedisConfig类

```java
package com.jet5devil.springbootredistest.config;

import org.springframework.cache.annotation.CachingConfigurerSupport;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;

@EnableCaching
@Configuration
public class RedisConfig extends CachingConfigurerSupport  {
    @Bean
    public RedisTemplate<String, String> redisTemplate(RedisConnectionFactory factory) {
        RedisTemplate<String, String> redisTemplate = new RedisTemplate<String, String>();
        redisTemplate.setConnectionFactory(factory);
        return redisTemplate;
    }
}
```

### ⑤ 使用地址测试

- set

地址：http://localhost:8080/saveCity?cityName=北京&cityIntroduce=中国首都&cityId=2

![image-20200901171742990](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200901171743.png)

- get

地址：http://localhost:8080/getCityById?cityId=2

![image-20200901171825964](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200901171826.png)