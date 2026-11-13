#1. 导包
from sklearn.neighbors import KNeighborsClassifier

#2. 准备数据集
x_train = [[0], [1], [2], [3]]
y_train = [0, 0, 1, 1]
x_test = [[5]]

#3. 创建模型对象
# estimator：估算器，模型对象，也可以用变量名model做接收
estimator = KNeighborsClassifier(n_neighbors=3)

#4. 模型训练
#传入：训练集的特征数据，训练集的标签数据
estimator.fit(x_train, y_train)

#5. 模型预测
# 传入：测试集的特征数据，获取到：预测结果（测试集的标签，y_test)
y_pre = estimator.predict(x_test)

#6. 打印预测结果（投票一样的时候会选择最小的）
print(f"预测值为：{y_pre}")