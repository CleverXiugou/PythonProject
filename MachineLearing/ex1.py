# as后面表示将这个库重命名为...
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read.csv是pandas库内的函数，表示读取制定路径的文件
path='ex1data1.txt'
# header=None表明没有列明，names 为读取的数据指定列名
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
# 表示展示数据的前几行，默认为5
print(data.head())

# data.describe()方法用于生成DataFrame对象data的描述性统计信息
# 包括计数，均值，标准差，最小值，25%分位数，50%分位数（中位数），75%分位数和最大值
print(data.describe())

# plot为DataFram对象的方法，用于绘图，kind指定绘图类型，x，y分别为横纵坐标名，figsize为图大小
data.plot(kind='scatter', x='Population', y='Profit', figsize=(12,8))

# 展示绘制好的图表
plt.show()