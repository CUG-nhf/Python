import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义三个转化函数 f1, f2, f3
def f1(x, y):
    return 6 - 2 * x - y

def f2(x, y):
    return 6 - 2 * y - x

def f3(x, y):
    return 6 - x - y

# 生成输入数据 x, y
x = np.linspace(0, 6, 10, endpoint=True)
y = np.linspace(0, 6, 10, endpoint=True)

# 创建网格点坐标
X, Y = np.meshgrid(x, y)

# 计算 z1, z2, z3
z1 = f1(X, Y)
z2 = f2(X, Y)
z3 = f3(X, Y)

z1[z1 < -1] = np.nan
z2[z2 < 0] = np.nan
z3[z3 < 0] = np.nan

# 绘制三个平面
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# 绘制 z1
ax.plot_surface(X, Y, z1, alpha=0.5, rstride=100, cstride=100, color='r', label='2x+y+z=6')

# 绘制 z2
ax.plot_surface(X, Y, z2, alpha=0.5, facecolors='g', rstride=100, cstride=100, label='x+2y+z=6')

# 绘制 z3
ax.plot_surface(X, Y, z3, alpha=0.5, facecolors='b', rstride=100, cstride=100, label='x+y+z=6')

ax.scatter([3, 1.475], [0, 1.159], [0, 1.889], color='red')

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 添加图例
ax.legend()

# 显示图形
plt.show()
