import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
# edgecolor='none' 去除点的轮廓.c=()为传递点的颜色的实参
# 颜色映射
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
# 设置刻度范围
plt.axis([0,1100,0,1100000])
# 第一实参表示保存文件名，第二个实参为裁剪图表周围多余的空白
# 文件保存须在图表展示语句之前，否则会出现保存图片空白的情况
plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()

