import matplotlib.pyplot as plt
from RandomWalk import Randomwalk
# 多次循环可以多次随机漫步
while True:
    rw = Randomwalk(50000)
    rw.fill_walk()
    # figure输出图表的宽度、高度、分辨率、背景色
    plt.figure(figsize=(10, 6))
    # 隐藏坐标轴，此操作必须位于scatter之前，且plt.axes()必须赋给一个变量，然后调用才行
    current_axes = plt.axes()
    current_axes.get_xaxis().set_visible(False)
    current_axes.get_yaxis().set_visible(False)
    # 创建数字列表，便于颜色映射
    point_numbers = list(range(rw.num_points))
    # 此颜色映射原理的值得思考
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)
    # 标起点和终点
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
