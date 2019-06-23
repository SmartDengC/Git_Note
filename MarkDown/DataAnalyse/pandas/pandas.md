# pandas 的数据结构
- Series
- DataFrame

# 简单操作

# 第一部分：pandas基础知识
### Series （`import pandas as pd`)  
1: data_obj = pd.range(20)  
2：pd.Series 返回的数据结构是pandas.core.series.Series  
3：data_obj.value 类型为 numpy.ndarray  
4：data_obj.index 类型为 pandas.core.indexes.range.RangeIndex   
5：data_obj.head()
6：数字索引：data_obj[1]
7：data_obj.name  
8：data_obj.index.name
9：删除列  del data_obj['A']


- list ----> Series  
`pd.range(10, 20)`
- dict ----> Series  
```python
dict = {
    2001:17.8,
    2002:20.1,
    2003:16.5
}
ser_obj = pd.Series(dict)
```
## DataFrame
pd.DataFrame(np.random.randn(),index,colums)
- dict ----> DataFrame
```python
dict = {
    'A':1.,
    'B':pd.Timestamp('20190827'),
    'C':pd.Series(1, index=list(range(4)), dtype='float32'),
    'D':np.array([3]*4,dtype='int32')
}
pd.DataFrame(dict)
```
# 第二部分：pandas 数据操作
### Series
`ser_obj = pd.Series(range(5), index=['a','b','c','d','e'])`
1：行索引：ser_obj['a']  
2：切片索引： ser_obj[1:3]  
3：不连续索引：ser_obj[[0,2,4]], ser_obj[['a'.'e']]  
4：布尔索引：ser_obj[ser_obj>2], ser_obj>2,先将其中的数值转换成bool值，在使用bool值对，ser_obj中的进行筛选
### DataFrame
`df_obj = pd.DataFrame(np.random.randn(5,4), colums=['a','b','c','d','e'])`  
1：列索引：df_obj['a'] ，返回Series类型 ,df_obj[[0]],返回DataFrame类型  
2：不连续索引：df_obj[['a','c']]


### 三种索引方式 loc  
### 整型位置索引
### 混合索引

### 对齐运算
1:进行相应的操作，如何两个对象不一样，多出来的地方操作为空，无论是Series还是DataFrame  
### 函数使用
abs 取绝对值
apply 
isnull()
dropna()
fillna() # 如果为空，用其补缺
### 索引排序
sort_index(ascending=Flase)

# 第三部分：pandas统计计算和描述
- 常用的统计计算  
sum()   
max()  
min()  
- 统计描述  
describe()  

# 第四部分：层级索引
- 交换分层顺序  
swaplevel()  
- 交换并排序分层  
swaplevel().sortlevel()

# 第五部分：分类和聚合
- Groupby 对象
```python
# 前提
dict_obj = {'key1' : ['a', 'b', 'a', 'b', 
                      'a', 'b', 'a', 'a'],
            'key2' : ['one', 'one', 'two', 'three',
                      'two', 'two', 'one', 'three'],
            'data1': np.random.randn(8),
            'data2': np.random.randn(8)}
df_obj = DataFrame(dict_obj)
```
1：groupby 返回的是一个DataFrameGroupBy 的对象，使用mean() 查看数据
- 分组运算
