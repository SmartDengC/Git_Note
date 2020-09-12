# SpringBoot中的CURD使用的技术

==本篇文章仅供参考，是自己对于这个过程中学习技术的记录==

## 一、自定义数据

### ①实体类的定义

现在自己编码，没有后台数据，所有就使用代码自己创建出数据。

这里我定义了两个pojo类，一个是`Employee`，一个是`Department`，他们的具体信息如下（这里只给出Employee的相关操作（所以说你们是没有办法还原博客内容的）：

- Employee

```java
package com.jet5devil.springbootemp.pojo;

import lombok.Data;
import lombok.NoArgsConstructor;
import java.util.Date;

@Data
@NoArgsConstructor
public class Employee {
    public Integer id;
    public String lastName;
    public String email;
    public Integer gender;// 0 woman 1 man
    public Department department;
    public Date date;

    public Employee(Integer id, String lastName, String email, Integer gender, Department department) {
        this.id = id;
        this.lastName = lastName;
        this.email = email;
        this.gender = gender;
        this.department = department;
        this.date = new Date();
    }
}
```

这里在创建对象的时候date这个使用的是new Date()，目的就是自动使用当前的时间，进行对象属性的赋值。

### ② 数据的创建

这里就是使用map这个数据结构来存数据，静态代码块只执行一次的特性。然后给他们定义查、增、删的操作。

- EmployeeDao

```java
package com.jet5devil.springbootemp.dao;

import com.jet5devil.springbootemp.pojo.Department;
import com.jet5devil.springbootemp.pojo.Employee;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

@Repository
public class EmployeeDao {
    public static Map<Integer, Employee> employees = null;
    @Autowired
    private DepartmentDao departmentDao;

    static{
        employees = new HashMap<Integer, Employee>();
        employees.put(101,new Employee(101, "aa", "a7297702123@qq.com", 0, new Department(1001,"市场部")));
        employees.put(102,new Employee(102, "bb", "b7297702123@qq.com", 1, new Department(1001,"销售部")));
        employees.put(103,new Employee(103, "cc", "c7297702123@qq.com", 0, new Department(1001,"财务部")));
        employees.put(104,new Employee(104, "dd", "d7297702123@qq.com", 1, new Department(1001,"营销部")));
        employees.put(105,new Employee(105, "ee", "e7297702123@qq.com", 0, new Department(1001,"产品部")));
    }
    private static Integer initId = 1006;
    /**
     * 添加一个员工
     */
    public void save(Employee employee){
        if (employee.id == null){
            employee.setId(initId++);
        }
        employee.setDepartment(departmentDao.getDepartmentById(employee.getDepartment().getId()));
        employees.put(employee.getId(), employee);
    }
    /**
     * 查询所有员工
     */
    public Collection<Employee> getAll(){
        return employees.values();
    }
    /**
     * 通过id查员工
     */
    public Employee getEmployeeById(Integer id){
        return employees.get(id);
    }
    /**
     * 删除一个员工
     */
    public void delete(Integer id){
        employees.remove(id);
    }
}

```

## 二、MVC的配置

在springboot中重写mvc的配置，需要实现webmvcconfigurer 接口，里面有添加视图控制的方法addviewController，也有拦截器类的方法addInterceptor，配置的话就能实现相应的功能。

```java
package com.jet5devil.springbootemp.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;


@Configuration
public class MyMvcConfig implements WebMvcConfigurer {
    @Override
    public void addViewControllers(ViewControllerRegistry registry) {
        registry.addViewController("/sign-in.html").setViewName("sign-in");
        registry.addViewController("/sign-up.html").setViewName("sign-up");
        registry.addViewController("/main.html").setViewName("index");
        registry.addViewController("/tables.html").setViewName("tables");
    }
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new LoginHandlerInterceptor())
                .addPathPatterns("/**")
                .excludePathPatterns("/","/user/login","/sign-in.html", "/sign-up.html", "/css/**", "/fonts/**", "/i/**", "/img/**", "/js/**");
    }
}


```

## 三、拦截器类

在这里也到了一些问题，就是登陆不进去的问题，因为自己把/user/login的路径也拦截了，导致一直在login界面循环，一直进不去。

```java
package com.jet5devil.springbootemp.config;

import org.springframework.web.servlet.HandlerInterceptor;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


public class LoginHandlerInterceptor implements HandlerInterceptor {
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        Object loginUser = request.getSession().getAttribute("loginUser");
        if (loginUser == null){
            request.setAttribute("msg", "没有权限查看");
            // 请求转发
            request.getRequestDispatcher("/sign-in.html").forward(request, response);
            return false;
        }
        else{
            return true;
        }
    }
}
```

## 四、Model内容，视图跳转

①model内容

大多数时会给model里面添加属性。及attribute，但是获取了？

```java
@RequestMapping("/emps")
public String list(Model model){
    Collection<Employee> employees = employeeDao.getAll();
    model.addAttribute("emps", employees);
    return "emp/list";

}
```

这里开始的时候，使用${emps}​ 总是找不到上面定义的属性，这是因为我没有写@Controller注解，第二次没有办法获取好像是因为，我写的返回路径多了一个/ ,导致找不到那个界面，然后就没有办法映射。

第三：路由使用`@`，变量使用`$`

```html
<tr th:each="emp:${emps}">
    <td th:text="${emp.getId()}"></td>
    <td th:text="${emp.getLastName()}"></td>
    <td th:text="${emp.getEmail()}"></td>
    <td th:text="${emp.getGender()==0?'女':'男'}"></td>
    <td th:text="${emp.department.getDepartmentName()}"></td>
    <td th:text="${#dates.format(emp.getDate(), 'yyyy-MM-dd')}"></td>
    <td>
        <a class="" th:href="@{/emp/}+${emp.getId()}"> 编辑</a>
        <a class="" th:href="@{/delemp/}+${emp.getId()}"> 删除</a>
    </td>
</tr>
```

## 五、界面意淫技巧

 ① 巧用

使用 `th:fragment` 和`th:inser`t 或者`th:replace`实现代码的复用。

```html
<!--header-->
<header th:fragment="headerbar">...</header>
```

```html
<!--header-->
<header th:replace="~{commons/commons::headerbar}">...</header>
```

② 不知道

在springboot+thymeleaf中引用静态资源的方式

```html
<link rel="stylesheet" th:href="@{/css/app.css}">
<script th:src="@{/js/jquery.min.js}"></script>
```

 ③ 知识点吧

单选框 `th:checked`

```html
<input th:checked="${emp.getGender()==1}" class="form-check-input" type="radio" name="gender" value="1">
```

复选框 `th:selected`

```html
<option th:selected="${dept.getId()==emp.getDepartment().getId()}" th:each="dept:${departments}" th:text="${dept.getDepartmentName()}" th:value="${dept.getId()}"></option>
```

日期格式化`#dates.format(xxx, 'yyyy-MM-dd')`

```html
<input th:value="${#dates.format(emp.getDate(), 'yyyy-MM-dd')}" type="text" class="form-control" name="birth" placeholder="2020-5-22">
```

字符判断为空 `#strings.isEmpty()`

```html
<form class="am-form tpl-form-line-form" th:action="@{/user/login}">
</form>
    <p style="color:red;text-align: center" th:text="${msg}" th:if="${not #strings.isEmpty(msg)}"></p>
```

## 六、properties

缓存和格式化的时间

```properties
spring.thymeleaf.cache=false
spring.mvc.date-format=yyyy-MM-dd
```