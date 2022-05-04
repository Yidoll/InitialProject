"""
神经网络
"""
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
import numpy as np

np.random.seed(0)
iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target

indices = np.random.permutation(len(iris_x))

iris_x_train = iris_x[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_x_test = iris_x[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]

# slover是权重优化策略; activation 表示选择的激活函数, 这里没有设置, 默认是relu; alpha是惩罚参数; hidden_layer_sizes 是隐藏层大小, 长度就是隐藏层的数量,
# 每一个大小就是设置每层隐藏层的神经元数量; random_state 是初始化所使用的随机项
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
# 增加一层 hidden_layer_sizes=(10, 10, 10)
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10, 10, 10), random_state=1)
clf.fit(iris_x_train, iris_y_train)
iris_y_predict = clf.predict(iris_x_test)
score = clf.score(iris_x_test, iris_y_test, sample_weight=None)

print('iris_y_predict=')
print(iris_y_predict)

print('iris_y_test=')
print(iris_y_test)

print('Accuracy:', score)
print('layers nums: ', clf.n_layers_)