"""
决策树算法
"""
from sklearn import datasets
from sklearn.tree import  DecisionTreeClassifier # 引入决策树算法包
import numpy as np
# 引入画图相关的包
from IPython.display import Image
# dot是一个程序化生成流程图的简单语言
import pydotplus
from sklearn import tree

np.random.seed(0)
iris = datasets.load_iris()

iris_x = iris.data # 数据部分
iris_y = iris.target # 类别部分
# 从150条数据中选140条作为训练集，10条作为测试集。permutation接收一个数作为参数（这里为数据集长度150），产生一个0-1449乱序一维数组
indices = np.random.permutation(len(iris_x))
iris_x_train = iris_x[indices[:-10]] # 训练集数据
iris_y_train = iris_y[indices[:-10]] # 训练集标签
iris_x_test = iris_x[indices[-10:]] # 测试集数据
iris_y_test = iris_y[indices[-10:]] # 测试集标签

# 设置树的最大深度为4
clf = DecisionTreeClassifier(max_depth=4)
clf.fit(iris_x_train, iris_y_train)

dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names,
                                filled=True, rounded=True,
                                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())

iris_y_predict = clf.predict(iris_x_test)

score = clf.score(iris_x_test, iris_y_test, sample_weight=None)

print('iris_y_predict=')
print(iris_y_predict)
print('iris_y_test=')
print(iris_y_test)
print('Accuracy:', score)