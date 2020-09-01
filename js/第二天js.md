## 4、函数

### 定义一个函数

```javascript
function abs(x){
    if(x >= 0){
        return x;
    }
    else{
        return -x;
    }
}
```

如果没有传入参数，返回undefine

```javascript
var abs = funcion(x){
    // .....
}
```

调用函数

abs(10);

```javascript
var abs = function(x){
	if(typeof x!=='number'){
        throw 'not a number';
    }
}
```

### arguments

代表传递进来的所有参数，是一个数组

获取包括参数的所有参数

### rest

获取除参数之外的所有参数

```javascript
function abs(a,b,...rest){
    console.log(a);
    console.log(b);
    console.log(res);
}
```

rest 只能写在最后，使用...

### 变量的作用域

![image-20200827202716562](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200827202716.png)

全局对象window

默认所有的全局变量都 自动绑定到window下的，alert()有也是绑定在window上

```javascript
var new = windown.alert;
windown.alert();
windown.alert = function(){};
// alert 失效
```

#### 规范

var PI = 3.14;

```javascript
// 唯一的全局变量
var kuangapp = {};
//  定义全局变量
kuangapp.name =  'kuangshen';
kuangapp.add = function(a, b){
	retur a+b;
}
```

#### 局部作用域问题

let关键字 解决 局部作用域问题

```javascript
function aa(){
    for(let i = 0; i<10;i++){
        // ...
    }
}
```

#### 常量Const

es6中引入常量关键字

```javascript
const PI = 2.22;
console.log(PI);
PI = '123'; // 会报错
```



### 方法

```javascript
var kuangshen = {
    name: 'kuangshen',
    birth: 2020,
    age: function(){
        // 今年- 出生年月
        var now = new  Date().getFullYear();
        return now - this.birth;
    }
};
function getAge(){
    var now = new Date().getFullYear();
    return now-this.birth;
}
var kuangshen2 = {
    age: getAge
}
// 属性
kuangshen.age
// 方法
kuangshen.age();
```

## 5、内部对象

#### apply

```javascript
getAge().apply(kuangshen, []);
// this指向kuagnsheng，参数为空参
```

所有的方法都有apply。

### 特殊对象

#### Date

标准对象

typeof

```javascript
var now = new Date();
now.getFullYear();// year
now.getMonth();// month
now.getDate();// day
now.getDay();// week
now.getHours();// hours
now.getMinutes();// minutes
now.getSecond();// second

now.getTime();// time stamp
console.log(new Date(157...));//  time stamp to time
```

```javascript
var now = new Date();
now.toLocaleString();  // local time
now.toGMTString();
```

### Json

```javascript
var user  = {
    name: 'jet5devil',
    age: 20,
    sex: 'boy'
}
var jsonuser = JSON.stringify(user);

var json = JSON.parse('{"name": "jet5devil"}');
```

## 6、面向对象编程

类：模板

对象：具体的实例

JS需要换一下思维

```javascript
//  __proto__ 父类
xiaoming.__proto__ = student;
```

### Class 继承

class 关键字是es6引入

```javascript
function Student(name){
    this.name = name;
}
// ES6
class Student{
    constructor(name){
        this.name = name;
    }
    hello(){
        alert('hello');
    }
}
var xiaoming = new Student('xiaomign');
class xiaoStudent extends Student{
    constructor(name, grade){
        super(name);
        this.grade = grade;
    }
    myGrade(){
        alert('wo shi yi ge xiaostudent');
    }
}
```

####  原型链

![image-20200827221522113](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200827221522.png)

## 操作BOM

```javascript
window.innerWidth
window.innerHeight
```

```javascript
nabigator.userAgent
```

大多数时候，不使用navigator对象，会被人修改

```javascript
screen.width
screen.height
```

```javascript
location(重要)
location.assign('https:// ... ');
```

```javascript
document 代表当前页面，HTML DOM 文件树
doucment.title
document.title = ""
document.getElementById('app');
document.cookie
```

获取具体的文档树节点

获取cookie

截获cookie原理

```javascript
history.back()
history.forword()
```

## 操作DOM对象（重点）

### 核心

浏览器网页就是一个DOM属性结构

更新 遍历DOM节点 删除 添加 （DOM 相当与标签）

获取DOM节点

#### 1 获取Dom标签

```javascript
// 对应的css选择器
document.getElementByTagName('ha')
document.getElementById('p1');
document.getElemenetByClassName('p2');

var children = father.childre;// 所有的子节点
father.firstChildren
father.lastChildren
```

这是原生的，尽量是用jquery

#### 2 更新节点

```javascript
id1.innerText = 'wqe';
id1.innerHtml = '<strong> </strong>'
id1.style.color = 'red';
id1.style.fontSize = '20px';
id1.style.padding = '2em';
```

#### 3 删除节点

1、先获取父节点，在删除自己

```javascript
father.removeChild('p1');
```

#### 4 插入节点

我们获得了dom节点，但是 是空的，我们通过innerHtml就可以增加一个节点。但是有数据的时候不能这样使用。

追加

```javascript
// 已有的节点
var js = document.getElementById('js');
 var list = document.getElementById('list');
 list.appendChild(js);
// 没有节点 创建一个节点
var newP = document.createElement('p');
newP.id = 'newP';
newP.innerText = 'hello jet5devil';
list.appendChild(newP);
newP.setAttribute('type', 'text/javascript');
```

#### insertBefore

![image-20200827234305683](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200827234305.png)

 

## 9 操作表单

表单是什么？ form dom

文本框 text

下拉框  select

单选框radio

多选框  checkbox

...

### 获取有要提交的信息

```javascript
// 得到输入框的值
var input_name = document.getElementById('username')
input_name.value

// 所选框
boy_radio.checked
// 修改选取的值
girl_radio.checked = 'true'
```

### 提交表单（重点）

```javascript
<button> 绑定时间
onClick()
function aa(){
    var psword = document.getE...('password');
    psword.value = md5(psword.value);
    return true;
}

onsubmit = 'aaa()'
```

![image-20200827235428823](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200827235428.png)

##  10 Jquery

jquery  里面有大量的js的函数

CDN jquery 

```javascript
<script src="lib/jquery.js"></script>
```

```javascript
// 公式 ： $(selector).action()
```

![image-20200828000527617](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200828000527.png)

#### 选择器

![image-20200828000722445](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200828000722.png)

[jquery](https://jquery.cuishifeng.cn/)

#### 事件

鼠标 键盘

![image-20200828001751945](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200828001752.png)

$() 表示页面加载完毕，是$(document.ready())的简写

#### 操作DoM

![image-20200828002421635](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200828002421.png)

![image-20200828003550894](https://gitee.com/jet5devil/typora-picture/raw/master/img/20200828003550.png)

https://www.ihewro.com/