# 学习总结

这里参考的是字母哥在b站的spring boot的教程视频和教学的文档

[b站教学视频地址](https://www.bilibili.com/video/av62047875?p=56)

[教学文档在看云中，登录，直接手spring boot，书名叫做手摸手教你学spring boot 2.x](https://www.kancloud.cn/hanxt/springboot2)

[代码地址15章](https://github.com/hanxt/boot-launch.git)


[代码地址16张](https://github.com/hanxt/bootlaunch-flux.git)


# 自我总结，

解首先说一下为什么要学习spring boot，就是因为他火，常用，各种优势，反正就是学了，好，没有毛病，我就直接使用文字来说了，多用文字，少用图，全是写给自己看的。

# 第一章 从项目开始
## 创建项目

创建一个项目，使用sspring initaliar（spring 初始化项目），点击下一步，这里填写group，（java中com下面的一下包名称），然后就是artifact，language，packaging，java version，等等，这些看英文就知道是什么了。  
然后就是选中web，将spring web添加进去。点击finish就可以了。

就可以直接运行了，是不是特别简单。

## 写一个测试controller试试

然后就是像spring mvc的项目或者其他的项目一样，写一个controller测试，表示测试成功。

## 插件（lombam和热部署什么的）

两个maven库，一个是lombok，一个是devtools，就是一些配置，在设置里面compiler，ctrl+alt+shift+/,勾选，就行了。