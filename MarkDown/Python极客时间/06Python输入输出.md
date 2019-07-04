# 06 | Python "黑箱": 输入与输出
https://time.geekbang.org/column/article/96570
## 基本的输入输出
1：input("Notes To Say Something!")  
2：数据类型转换是使用try，catch语句。  

## 简单NLP（自然语言处理）任务。
- 基本步骤
    - 1:读取文件
    - 2:去除所有标点和换行符，并把所有大写转换成小写
    - 3:合并相同的词，统计每个词出现的频率，并按照词频从大到小排序
    - 4:将结果输出到文件out.txt
```python
import re


def parse(text):
    # 使用re去除标点和换行符
    text = re.sub(r'[^\w]', ' ', text) # sub 函数用于替换字符串中匹配，使用空格来代替标点和换行符
    # 转换成小写
    text = text.lower()
    # 生成所有词的列表
    word_list = text.split(' ')
    # 去除空白单词
    # filter(func, seq),用于提取seq中能使func为true的元素序列。是一个布尔函数
    word_list = filter(None, word_list) # 判断word_list中的字符是否为空
    # 生成单词和词频但系,就是遍历这个word_list来统计
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    # 按照词频排序
    # key 表示用于么一个列表项，reverse表示反向排序
    sorded_word_cnt = sorted(word_cnt.items(), key=lambda kv:kv[1], reverse=True)
    return sorded_word_cnt


with open('in.txt', 'r') as fin:
    text = fin.read()
word_and_freq = parse(text)
with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))

```
**注意：所有的I/O操作都应该进行错误处理**

## json 序列化与实战
1:json(JavaScript Object Notation)是一种轻量级的数据交换格式，把所有事情都用设计的字符串来表示。
2:函数
- json.dumps()  python基本数据类型----->序列化string
- json.loads()  字符串反序列化python的基本数据类型
## 总结
- I/O 操作需谨慎，一定要进行充分的错误处理，并细心编码，防出现漏洞
- 编码时，对内存占用的磁盘占用要有充分的估计，
- json序列化是很方便的工具

## 思考题
第一问：你能否把NLP的例子中的word count实现一遍？不过这次，in.txt可能非常非常大（意味你不能一次性读入到内存），而out.txt不是很大（意味着单词的重复很多）
第二问：百度网盘，假设空间限制（5GB），如果有一天，你计划把家里的100G的数据传送到公司，可惜你没有带U盘，于是你想到了.....
