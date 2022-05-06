"""
DBScan 算法
"""
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import dbscan
import numpy as np

# 生成500个点 噪声为0.1
X,_ = datasets.make_moons(500, noise=0.1, random_state=1)
#
# df = pd.DataFrame(X, columns=['x', 'y'])
# df.plot.scatter('x', 'y', s=200, alpha=0.5,c="green", title='dataset by DBSCAN')
# plt.show()

# eps为邻域半径, min_samples为最少样本量
core_smaples, cluster_ids = dbscan(X, eps=0.2, min_samples=20)
# cluster_ids中-1表示对应的点为噪声
df = pd.DataFrame(np.c_[X, cluster_ids], columns=['x', 'y', 'cluster_id'])
df['cluster_id'] = df['cluster_id'].astype('i2')
# 绘制结果图像
df.plot.scatter('x', 'y', s=200, c=list(df['cluster_id']), cmap='Reds', colorbar=False, alpha=0.6, title='DBSCAN cluster result')
plt.show()