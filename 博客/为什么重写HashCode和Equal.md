# HashCode和Equals

在最开始提出一个问题：

==为什么hashcode()和equals()方法要一起重写？==

## 为什么我们要重写HashCode和Equals？

在我们业务系统中判断对象有时需要的不是严格意思上的相等，而是业务上的相等。在这种情况下，原生的equals方法就不能满足我们的需求了。

## equals 源码

```java
public boolean equals(Object obj) {
        return (this == obj);
    }
```

用以判断变量参数和当前实例是否相等，jdk默认实现是基于对象内存地址是否相等，如果两个对象内存地址相同， 则表示两个对象相等。

## hashcode 源码

```java
public native int hashCode();
```

默认情况下，该方法返回一个整数，对于每一个对象来说该数字是唯一的，但是该数字并非恒定的。

## 下面进行说明

```java
/**
 * @ClassName Student
 * @Version 1.0
 * @Author jet5devil
 * @Date 2020/8/29 4:25
 * @Description hashcode and equals
 */
public class Student {
    int id;
    String name;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public static void main(String[] args) {
        Student s1 = new Student(1, "jet5devil");
        Student s2 = new Student(1, "jet5devil");
       System.out.println("s1.hashcode:"+s1.hashCode());
        System.out.println("s2.hashcode:"+s2.hashCode());
        System.out.println("s1.equals(s2):"+s1.equals(s2));
    }
}

```

运行结果：在没有重写任何一个方法的时候，s1 和 s2  是两个不同的对象，自然hashcode不同，且equals的结果为false

> s1.hashcode:1735600054
> 		s2.hashcode:21685669
> 		s1.equals(s2):false

## 重写equals() 不重写hashcode()

```java
   @Override
    public boolean equals(Object o) {
        if (o == null) {
            return false;
        }
        if (!(o instanceof Student)) {
            return false;
        }
        if (o == this) {
            return true;
        }
        return this.getId() == ((Student) o).getId();
    }
```

> s1.hashcode:1735600054
> s2.hashcode:21685669
> s1.equals(s2):true

### ArrayList 中的equals()?

```java
public static void main(String[] args) {
        Student s1 = new Student(1, "jet5devil");
        Student s2 = new Student(1, "jet5devil");
        System.out.println("s1.hashcode:"+s1.hashCode());
        System.out.println("s2.hashcode:"+s2.hashCode());
        System.out.println("s1.equals(s2):"+s1.equals(s2));
        List<Student> stuList = new ArrayList<>();
        stuList.add(s1);
        System.out.println("stuList.size():"+stuList.size());
        System.out.println("Contains ?:"+stuList.contains(s2));
    }
```

>s1.hashcode:1735600054
>s2.hashcode:21685669
>s1.equals(s2):true
>stuList.size():1
>Contains ?true

可以看出虽然hashcode 不同，但是得到了我们期望的结果

```java
// 测试HashSet中的equals()
        Set<Student> stuSet = new HashSet<>();
        stuSet.add(s1);
        stuSet.add(s2);
        System.out.println("stuSet.size():"+stuSet.size());
        System.out.println("Contains?:"+stuSet.contains(new Student(1, "jet5devil")));
```

>stuSet.size():2
>Contains?:false

从结果可以看出这个时候,JVM认为不是同一个对象，虽然我们重写了equals方法

涉及HashSet的内部结构，

重写hashcode的重要性

```java
    @Override
    public int hashCode() {
        return Objects.hash(id, name);
    }
```

## 结论

- 如果两个对象相同，则他们的hashcode一定相同
- 如果两个对象的hashcode值相同，并不意味着他们是相同的
- 对于使用Hash散列方式存储对象的数据结构：HashSet、HashMap、HashTable等，仅仅重载equals方法会导致实际业务逻辑失败
- 在比较两个对象时，仅重载hashcode方法并不能强制java忽略内存地址。

[2018开年第一篇：equals()与hashCode()](https://blog.csdn.net/kangkanglou/article/details/78954894)



[java为什么要重写hashCode和equals方法](https://blog.csdn.net/zknxx/article/details/53862572)



