import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    # 调用了csv的reader类
    reader = csv.reader(f)
    # 调用了reader类的next函数，返回文件的下一行，第一次调用返回第一行
    header_row = next(reader)
    # enumerate获取每个元素的索引（csv中即值存放在那一列）及其值
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # 提取数据部分
    # 创造多个列表的语法
    dates, highs, lows = [], [], []
    # row遍历reader中的各行
    for row in reader:
        # 避免数据异常出现错误
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 设置图幅
fig = plt.figure(dpi=128, figsize=(10, 6))
# c参数设置折线的颜色，plot函数如果没有满足三个实参，默认实参传递给Y轴，X轴形参默认为[0:lens(Y)]
plt.plot(dates, highs, c='red', alpha=0.5)
# alpha设置透明度
plt.plot(dates, lows, c='blue', alpha=0.5)
# facecolor设置填充区域的颜色，传递了一个x值系列、两个y值系列
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high and low temperatures, 2014\nDeath vally,CA", fontsize=24)
plt.xlabel('', fontsize=16)
# 绘制斜日期标签
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()