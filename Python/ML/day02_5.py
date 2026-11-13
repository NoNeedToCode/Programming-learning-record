import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split    
from sklearn.neighbors import KNeighborsClassifier      
import joblib
from collections import Counter 
from sklearn.metrics import accuracy_score

# 忽略警告
import warnings
warnings.filterwarnings('ignore', module='sklearn')

# 1.定义函数，接收用户传入的索引，展示 该索引对应的图片

def show_digit(idx):
    df = pd.read_csv('F:/Users/LEGION/10086/ML/train.csv')
    # print(df)  # （42000列 * 785列）

    # 2. 判断传入的索引是否越界

    if idx < 0 or idx > len(df) - 1:
        print('索引越界！')
        return

    # 3.走这里，说明没有越界，就正常获取数据
    x = df.iloc[:, 1:]
    y = df.iloc[:, 0]

    # 4.查看用户传入的索引对应的图片是多少
    print(f'该图片对应的数字是：{y.iloc[idx]}')
    print(f'查看所有的标签的分布情况：{Counter(y)}')

    # 5.查看下 用户传入的索引对应的图片 的形状
    print(x.iloc[idx].shape)       # (784,) 我们要想办法把（784，）转换成（28, 28）
    # print(x.iloc[idx].values)    # 具体的784个像素点数据

    x_data = x.iloc[idx].values.reshape(28, 28)  

    # 6. 把（784，）转化成（28， 28）
    x = x.iloc[idx].values.reshape(28, 28)
    # print(x)  # 28 * 28像素点
    plt.imsave('F:/Users/LEGION/10086/ML/Fig_01.png', x_data, cmap='gray')
    print("图片已保存为 28×28！")


    # 7.具体的绘制灰度图的动作
    plt.imshow(x, cmap='gray')       # 灰度图
    plt.axis('off')
    plt.show()


# 2.定义函数，训练模型，并保存训练好的模型
def train_model():
    # 1.加载数据集 
    df = pd.read_csv('F:/Users/LEGION/10086/ML/train.csv')
    # 2.数据的预处理
    # 2.1 拆分出特征列
    x = df.iloc[:, 1:]        # 特征列
    # 2.2 拆分出标签列
    y = df.iloc[:, 0]         # 标签列
    # 2.3 打印特征和标签的形状
    print(f'x的形状：{x.shape}')       # (42000, 784)
    print(f'y的形状：{y.shape}')       # (42000,)
    print(f'查看所有的标签的分布情况：{Counter(y)}')
    # 2.4 对特征列（拆分前）进行 归一化
    x = x / 255
    # 2.5 拆分训练集和测试集
    # 参1：特征列  参2：标签列   参3：测试集的比例  参4：随机种子   参5：参考y值进行抽取，保持标签的比例（数据均衡）
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=23,stratify=y)

    # 3.模型训练
    # 3.1 创建模型对象
    estimator = KNeighborsClassifier(n_neighbors=3)
    # 3.2 模型训练
    estimator.fit(x_train, y_train)

    # 4.模型评估
    print(f'{estimator.score(x_test, y_test)}')
    print(f'{accuracy_score(y_test,estimator.predict(x_test))}')

    # 5.保存模型
    # 参1：模型对象   参2：模型保存的路径
    joblib.dump(estimator,filename='F:/Users/LEGION/10086/ML/my_model/train.pkl')
    print('模型保存成功！')


# 3. 定义函数，测试模型
def use_model():
    # 1. 加载图片
    x = plt.imread('F:/Users/LEGION/10086/ML/Fig_01.png') # 28 * 28 像素
    x = x[:, :, 0]
    # 2. 绘制图片
    # plt.imshow(x, cmap='gray')     # 灰度图
    # plt.axis('off')
    # plt.show()
 
    # 3. 加载模型
    estimator = joblib.load('F:/Users/LEGION/10086/ML/my_model/train.pkl')

    # 4. 模型预测
    # 4.1 查看 数据集转换
    print(x.shape)                   # （28，28）
    print(x.reshape(1, 784).shape)   # （1，784）
    print(x.reshape(1, -1).shape)    # 效果等同于（1,784），语法糖，效果同上

    # 4.2 具体的转换动作，记得归一化（因为训练模型的时候 使用了 归一化动作）
    x = x.reshape(1, -1) 
    # pirnt(x) 看数据情况 发现读图已经归一化
    # 4.3 模型预测
    y_pre = estimator.predict(x)

    # 5.打印预测结果
    print(f'预测值为：{y_pre}')


# 4. 
if __name__ == '__main__':
    # 绘制数字
    # show_digit(5)

    # 训练模型，并保存模型
    # train_model()
    use_model()


