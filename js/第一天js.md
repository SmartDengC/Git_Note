<script src="js/qj.js"></script>

type 不用写也是默认

<script> // ..</script>

alert('hello word');

##2.2 基本语法入门

// 1、var  num  = 1;

// 2、 var name  = "jingjiang";

'hello word';

console.log( score);

![image-20200827183932060](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200827183932.png)

==数据类型==

number  NaN Infinity 无限大

==字符串  ==

==布尔值==

==逻辑运算== && || ！

比较运算符 = == 类型不一样，数字一样返回true === 类型一样 数值一样为true

==浮点数问题==

console.log((1/3) === (1-2/3)) false

==Math.abs()

==null 和 undefine==

==数组==

var arr=[1,2,3,'hello', null,true];

数组越界 ，js报undefine

==对象==

对象大括号，数组中括号

var person =  {

​	name:"qianjiang",

​    age: 3,

​    tags :[]

}



## 严格检查模式

es6使用let定一个常量 

'use sttict' 严格检查模式，预防随意性的问题

## 数据类型

### 字符串

'use strict'

单引号和双引号 都可以

var msg = `hello 

world

nihao`

var mag = 'hello ${name}'

5、字符串长度

str.length

6、字符串的可变性，不可变

str.toUpperCase()

str.toLowerCase()

### 数组

var arr = [1,1,2,3]

arr.length

数组大小会发生变化  

arr.length = 10

arr.indexOf(2); 通过元素获得下标索引

slice() 截取arr的一部分，返回一个新的数组

arr.push('a'); 压入到尾部

unshift(), 在头部亚茹数据

shift();从头部取出数据

arr.pop();

sort()

reverse();

concat();只是返回一个新的数组，以前的数组没有改变

join() 

### 对象

![image-20200827192007628](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200827192008.png)

person.age

person.age = 22

delete person.age 动态的删除对象属性

person.haha = 'haha'

'age' in person javascript 对象的key是字符串

### 流程控制

'use strict'

if

while(age < 3){console.log(age);}



for(let i = 0;  i<10;i++){

console.log(i)}



age.forEach(function(value){

console.log(value)})

for(var num in age){

​    console.log(age[num])

}

### Map和Set

new Map();

new Set();

var map = new Map([['tom', 2], ['jack', 22]]);

map.get('tom');

map.set('admin', 33);

map.delete('tom');

set

var set = new Set([1,1,2,3,4]);

set.add(2);

set.delete(3);

set.has(3);



for in

for of



