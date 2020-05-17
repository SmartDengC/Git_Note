# HashMap 底层存储原理详解

## 数组

```java
public class Array{
    public static void main(String[] arg){
        Integer[] integers = new Integer[10];
        integers[0] = 0;
        integers[1] = 0;
        integers[2] = 0;
        integers[3] = 0;
        System.out.println(integers[1]);
    }
}
```



## 链表

```java
public class Node{
    public Node next;
    public Object data;
    
    public Node(Object data){
        this.data = data;
    }
	public static void main(String[] args){
		Node node = new Node("王哥");
        node.next = new Node("B哥");
	}
}
```

