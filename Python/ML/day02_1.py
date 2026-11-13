# 欧式距离 = 对应维度差值的平方和开根
# 曼哈顿距离，城市街区距离 = 对应维度的差值的绝对值求和
# 切比雪夫距离 = 对应维度差值的绝对值的最大值
# 闵可夫斯基距离，闵氏距离 = 上三者结合


from sklearn.preprocessing import MinMaxScaler
# 1.准备数据集
x_train = [[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]]


# 2.创建归一化对象
# 参数默认是0 1， 如果就是这个可以不写
# transfer = MinMaxScaler()
transfer = MinMaxScaler(feature_range=(0,1))

# 3.对元数据进行归一化
x_train_new = transfer.fit_transform(x_train)

# 4.打印处理后数据
print("\n")
print(x_train_new)