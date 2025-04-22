import matplotlib.pyplot as plt

# 绘制头部
plt.Circle((0, 0), 1, color='yellow')

# 绘制眼睛
plt.Circle((-0.3, 0.3), 0.1, color='black')
plt.Circle((0.3, 0.3), 0.1, color='black')

# 绘制嘴巴
plt.plot([-0.3, 0.3], [-0.3, -0.3], color='red')

# 绘制身体
plt.plot([0, 0], [-1, -3], color='blue')

# 绘制手臂
plt.plot([-1, 1], [-2, -2], color='blue')

# 绘制腿
plt.plot([-0.5, 0], [-3, -4], color='blue')
plt.plot([0.5, 0], [-3, -4], color='blue')

# 设置坐标轴范围
plt.xlim(-2, 2)
plt.ylim(-5, 1)

# 隐藏坐标轴
plt.axis('off')

# 显示图像
plt.show()