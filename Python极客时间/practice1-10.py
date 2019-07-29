'''
1 实验目的
（1）       熟悉matplotlib库作图函数；
（2）       熟悉数据分析与可视化。
2实验内容
从网络教学平台下载天气数据pollution.csv，完成如下数据分析和可视化要求，
(1)     统计每年的日平均PM2.5指数，日平均气温，并分别用柱状图显示，要求图有中文标题和坐标轴说明；
(2)     采用2X2子图，以折线展示5年内PM2.5,气温，气压，累计降雨量趋势图；
(3)     统计每年PM2.5指数平均值最高的5个月，获取每天的PM2.5指数，并在同一图表上汇出其折线图（不同年份用不同的颜色表示）
'''
# import pandas as pd
# import matplotlib.pyplot as plt
#
# unrate = pd.read_csv('pollution.csv')
# data1=pd.DataFrame(unrate,columns=[u"No",u"year",u"month",u"day",u"hour",u"pm2.5"],)
# print(data1)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
Date = pd.read_csv('./pollution.csv')
print(Date.head(1))
# 去Nan 数据
pre_Date = Date.dropna()
# 获取年份
years = list(pre_Date.groupby('year').size().index)
years_mean_pm = []
years_mean_temperature = []
years_mean_pres=[]
years_mean_ir=[]
for year in years:
    # 获取当年数据
    current_Date = pre_Date.loc[pre_Date['year']==year]
    # 计算pm2.5年平均
    mean_pm = current_Date['pm2.5'].mean()
    # 记录当前年的pm 平均值
    years_mean_pm.append(mean_pm)
    # 每年平均温度
    mean_temperature = current_Date['TEMP'].mean()
    # 记录当前年的温度 平均值
    years_mean_temperature.append(mean_temperature)
    mean_pres=current_Date['PRES'].mean()
    years_mean_pres.append(mean_pres)
    mean_ir=current_Date['Ir'].mean()
    years_mean_ir.append(mean_ir)
x = np.arange(len(years))
width = 0.2
fig,ax = plt.subplots()
ax.bar(x,years_mean_pm,width,alpha = 0.8)
ax.bar(x+width,years_mean_temperature,width,alpha = 0.8,color= 'black')
plt.title("daliy_mean PM2.5 And Temp EveryYear")
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(0.8, 1))
ax.set_xticks(x +width/2)#将坐标设置在指定位置
ax.set_xticklabels(years)#将横坐标替换成
plt.xlabel('时间')
plt.ylabel('Blue is pm 2.5             Black is temp')
plt.show()

plt.title("PM2.5, temperature, pressure, cumulative rainfall trend chart within 5 years")
plt.xlabel('year')
plt.subplot(221)
plt.plot(years, years_mean_pm, color="green", label="pm2.5")
plt.legend(loc='upper right')
plt.subplot(222)
plt.plot(years, years_mean_temperature, color="red", label="TEMP")
plt.legend(loc='upper right')
plt.subplot(223)
plt.plot(years, years_mean_pres, color="skyblue", label="PRES")
plt.legend(loc='upper right')
plt.subplot(224)
plt.plot(years, years_mean_ir, color="blue", label="Ir")
plt.legend(loc='upper right')
plt.show()

color=['black','red','blue','yellow','green']
for year in years:
    # 取出当年数据，只取month,day,pm2.5这几列的数据
    data_year = pre_Date.loc[pre_Date['year'] == year,['month','day','pm2.5']]
    #求出pm2.5的月平均值
    month_mean_pm = data_year.groupby('month')['pm2.5'].mean()
    # 对pm2.5的月平均值排序，ascending=False表示降序,ture是升序
    month_mean_pm_1 = month_mean_pm.sort_values(ascending=False)
    # 取出pm2.5月平均值最高的前五个月的月份的月份值
    months = list(month_mean_pm_1.index[:5])
    # 求出每月有pm2.5的天数
    month_day_sum = data_year.groupby(['month','day']).mean().groupby(['month']).size()
    # 天数总数
    totol_days=0
    # pm2.5每日的值
    day_value=[]
    for i in months:
        totol_days = totol_days+month_day_sum[i]
        # 取出当月数据
        data_month = data_year.loc[data_year['month']==i]
        # 取出当月每日pm2.5的平均值，存进day_value
        month_values = list(data_month.groupby('day')['pm2.5'].mean().values)
        day_value+=month_values
    plt.plot(range(totol_days),day_value,color[year-2010],label=str(year))
plt.legend()
plt.xlabel('day')
plt.ylabel('pm2.5')
plt.show()