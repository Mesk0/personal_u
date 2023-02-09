import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
# plot画折线图
plt.plot(input_values,squares,linewidth=5)
# 设置图名，字体大小
plt.title("Square Numbers", fontsize=24)
# 分别设置X轴，Y轴标题，字体大小
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 分别设置刻度
plt.tick_params(axis='both',labelsize=14)
plt.show()
