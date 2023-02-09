import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
# s设置点的大小,scatter画散点图
plt.scatter(x_values, y_values, s=100)
# 设置图名、X,Y轴解释，字体大小
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
# 设置刻度大小
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()
