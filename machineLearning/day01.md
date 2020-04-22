卷积，赤化，抹零
fully connected layer
future balues bote on x or o
全连接，乘以一个权重，
www.image-net.org/index
backpropagation ? 损失函数，反向传播
处理图片的数据  
in a nutshell?  

## 1.1 人工智能的关系  
人工智能>机器学习>深度学习  
机器学习是人工智能的一个实现途径
深度学习是机器学习的一个方法发展而来
1956年成为人工智能元年  

传统预测 图像领域 自然语言处理领域

## 1.2 什么是机器学习
是从数据中自动分析获得模型，并利用模型对未知的数据进行预测。
数据， 模型， 预测
从历史数据中获得规律？这些历史数据是怎样的格式？
面积，位置，楼层，朝向----房价（特征值和目标值构成的）

对于每一行数据称之为一个样本
有些数据集可以没有目标值

## 1.3 机器学习分类
含有猫狗的图片，是猫还是狗？
监督学习
    目标值：类别  分类问题 k-近邻， 贝叶斯分类，决策树， 随机森铃，逻辑回归
    目标值：连续型的数据  回归问题 线性回归

无监督学习
    目标值：无  无监督学习  k-means

## 1.4 机器学习的开发流程
获取数据--数据处理--特征工程--机器学习算法模型训练--模型评估--应用  

## 1.5 学习框架和资料
算法是核心，数据和计算是基础  
找准定位  


## 2.1 数据集
可用的数据集 （公司内部， 百度， 数据接口）
学习阶段可用的数据集 sklearn， kaggle:https://www.kaggle.com/datasets, UCI数据集
### scikit-learn 工具介绍
### 安装  pip install sklearn
### 使用数据集 sklearn.datasets load_*(小规模数据), ftech_*(大规模)
sklearn.datasets.load_iris()
sklearn.datasets.fetch_20newsgroups(data_home=None, subset="all") train or test for subset

返回Bunch字典格式，继承字典 键值对 data target DESCR, feature_names, target_names
bunch.key = values

数据集的划分， 20-30%
sklearn.model_selection.train_test_split(arrays, "options)
发挥的一个步骤  

sklearn  特征工程
pandas 数据清洗

### 特征抽取
机器学习算法 统计方法， 数学公式， 不能处理字符串-转换成数值？
类型--》数值？
将任意的数据转换成机器学习的数字特征
字段特征提取
文本的耳针提取

sklearn.feature_extraction
#### 字典 特征提取
sklearn.feature_extraction.DictVectorizer(sparse=True, ...)
矩阵matrix二维数组， 向量 vector
.fit_tranform()

#### 文本 特征抽取
单词， 短语， 字母， 
data = sklearn.feature_extraction.text.CountVectorize(stop_words=[])
fit_transform(data.toarray())
.get_feature_names()
stop_word 停用词

pip install jieba
```python
data = [""]
import jieba
def cut_word(text):
    a = " ".join(List(jieba.cut(text)))  # 生成器
    print(a)
```

```python
data =[""]
data_new = []

for sent in data:
    data_new.append(cut_word(sent))
transfer = CountVectorize()
data_final = transfer.fit_transform(data_new)
print("data_new", data_final.toarray())
print(" 特征名称", tranfer.get_feature_names())
```
关键词：
方法2：Tf-idf
sklearn.feature_extraction .text.TfidfVectorizer
### 特征预处理
sklearn.preprocessing
#### 归一化
归一化 ， 数据映射到一个区间，如果有异常值？最大值或者最小值， 鲁棒性较差
sklearn.preprocessingo.MinMaxScaler()
fit_features()
```python
# 获取数据
data = pd.read_csv("")
data = data.iloc[:, :3]
# 实例化一个转换器类
from sklearn.preprocessing import MinMaxScaler
transfer = MinMaxScaler(feature_range=[2,3])
# 调用fit_feature()
data_new = transger.fit_feature(data)
```
#### 标准化
通过对原始数据进行变换把数据变换到均值为0， 保准差为1的范围内
(x - mean) / std
标准差：集中程度
sklearn.preprocessing.StandardScaler()
fit_feature()

### 特征降维
#### 降维
ndarray 嵌套的层数，
此处的降维就是降低特征的个数，要求特征与特征之间不相关  

##### 特征选择
数据中包含冗余 或相关变量只在从原有特征中找出主要特征。  
Filter， 
方差选择法  
    sklearn.feature_selection.VarianceThreshold()
相关系数 
    from scipy.stats import pearsour
Embedded（嵌入式） 决策树，正则化，深度学习

##### 主成分分析
降维，减少信息损失
sklearn.decomposition.PCA(n_components=Nune)
小数：保留百分之多少的系信息
整数：减少到多少特征

交叉表和透视表
pd.merge(aisles, products, on=["", ""])
pd.crosstab(tab3[""], tab3[""])