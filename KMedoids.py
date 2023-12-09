import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids

def plot_kmeans_iteration(data, centers, labels, iteration):
    #plt.figure(figsize=(8, 6))

    # 绘制散点图
    for cluster_label in np.unique(labels):
        cluster_points = data[labels == cluster_label]
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1], s=200, label=f'Cluster {cluster_label}', alpha=0.7)

    # 绘制簇中心
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, label='Cluster Centers')

    # # 绘制簇中心的虚线圆
    # for center, label in zip(centers, np.unique(labels)):
    #     circle = plt.Circle(center, radius=1.5, color='red', fill=False, linestyle='dashed', linewidth=2, alpha=0.5)
    #     plt.gca().add_patch(circle) 

    plt.title(f'K-Medoidss Iteration {iteration}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend(loc='best')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# 生成示例数据
data = np.array([[1, 2], [2, 3], [2, 6], [7, 2], [10, 8], [12, 5]])

# 创建 KMeans 模型，设置簇的数量（k）
init = np.array([[2,6],[12,5]])
kmeans = KMedoids(n_clusters=2, metric='manhattan', init=init, max_iter=2, random_state=42)  # 设置最大迭代次数为5
plot_kmeans_iteration(data, init, np.zeros(6), 0)

lab =[]
for d in data:
    a = abs(d[0] - init[0, 0]) + abs(d[1] - init[0, 1])
    b = abs(d[0] - init[1, 0]) + abs(d[1] - init[1, 1])
    if a < b:
        lab.append(1)
    else:
        lab.append(0)
plot_kmeans_iteration(data, init, lab, 0)

# 手动执行迭代过程
for i in range(kmeans.max_iter):
    # 执行一步迭代
    kmeans.fit(data)
    
    # 获取簇中心和簇标签
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    
    # 输出结果并绘图
    print(f"Iteration {i + 1}:")
    print("Cluster Centers:")
    print(centers)
    print("Cluster Labels:")
    print(labels)
    print("")
    
    plot_kmeans_iteration(data, centers, labels, i + 1)

# 最终结果
print("Final Result:")
print("Cluster Centers:")
print(centers)
print("Cluster Labels:")
print(labels)
