# 标准化

from sklearn.preprocessing import MinMaxScaler,StandardScaler 
# 1.准备数据集
x_train = [[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]]

# 2.创建标准化对象
transfer = StandardScaler()

# 3.对元数据进行标准化
x_train_new = transfer.fit_transform(x_train)

# 4.打印处理后数据
print("标准化后数据集为：\n")
print(x_train_new)

# 5.打印数据的均值和方差
print(f"数据集的均值为：{transfer.mean_}")
print(f"数据集的方差为：{transfer.var_}")
print(f"数据集的标准差为：{transfer.scale_}")