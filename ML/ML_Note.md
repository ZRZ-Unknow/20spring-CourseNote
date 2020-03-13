# Chapter1:绪论

+ 参考书目:sweat_smile:

  > + 西瓜书
  > + Elements of statistic learning (ESL), 
  > + PRML 
  > + Machine Learning, 1997, Tom Mitchell米切尔
  > + 统计学习方法

+ 达特茅斯会议标志着人工智能学科的诞生(1956)

+ AI发展历程

  >+ 1966~1960s: Logic Reasoning，成就：自动定理证明系统
  >+ 1970s~1980s: Knowledge Engineering，成就：专家系统
  >+ 1990~？：Machine Learning

+ ML经典定义：利用经验改善系统自身的性能

+ ML理论基础：PAC(Probably Approximately Correct)概率近似正确

### 基本术语

+ 示例(instance)、样例(example)
+ 样本(sample)
+ 属性(attribute)，特征(feature)、属性值
+ 属性空间，样本空间，输入空间
+ 特征向量
+ 标记空间，输出空间

+ 假设(hypothesis)，真相(ground-truth)，学习器(learner)：本课特指算法经过输入数据和参数后得到的实例

+ 监督学习：分类与回归等

在机器学习中，常假设数据独立同分布（i.i.d.假设）

+ 泛化(generalization)：观测到样例后，推广到一般、未来(归纳)
+ 特化(specialization)：得到一个一般的规律，推广到特殊的（演绎）

+ 假设空间(hypothesis space)：
+ 版本空间(version space)：与训练集一致的假设集合，该如何选择哪个假设(模型)？
  + 归纳偏好（inductive bias）：机器学习算法在学习过程中对某种类型假设的偏好

  + 一般原则：奥卡姆剃刀(Ocam's razor)

  + 任何一个有效的机器学习算法必有其偏好

  + 没有免费的午餐(NFL定理)：一个算法a在某些问题上比b好，则一定存在一些问题上b比a好

    ![image-20200228121221378](pic\image-20200228121221378.png)

    其中对h的求和为1

  + 

# Chapter2:模型评估和选择

### 评估方法

+ 泛化误差与经验误差，过拟合与欠拟合(overfitting/underfitting)
+ 测试集与训练集的划分
  + 留出法:把数据集直接划分为训练集与测试集
    + 多次重复划分
    + 保持数据分布一致性(如分层采样)
    + 测试集比例(1/5~1/3),不能太大也不能太小
  + k-折交叉验证法：k-fold cross validation
    + 将数据集分成k份，做k次实验，每一次都换一个测试集，最后求个平均值
    + 通常将数据集划分也做k次
  + 自助法：
    + 基于自助采样(bootsrap sampling)（有放回采样）
    + 训练集与原样本集同规模，但是训练集的分布出现了改变
    + 包外估计(out-of-bag estimation)：约有36.8%的样本不出现
  + 留一法(LOO)：k折中k选取为数据样本的数量，测试集仅有一个样本，排除了k折时划分的随机性
+ 算法的参数：一般由人工设定，称为超参数
+ 模型的参数：一般由学习确定
+ 验证集(validation set)：从训练集上划出一部分得到

### 性能度量

+ 回归任务常用均方误差：$E(f;D)=\frac{1}{m}\sum_{i=1}^m(f(x_i)-y_i)^2$, 是一个二范式的loss函数

+ 分类任务：

  <img src="pic\image-20200306101442952.png" alt="image-20200306101442952" style="zoom:67%;" />

  分类结果混淆矩阵：TruePositive,FalseNegitive

  查准率：预测为正例的里面预测对了的有多少

  查全率：所有为正例的里面预测对了的有多少

  ![image-20200306101614864](pic\image-20200306101614864.png)

  + 基于BEP的性能度量：PR图中，y=x直线与学习器的曲线相交得到的平衡点(break-event point)中，BEP更大的学习器更优

  + F1度量：$F1=\frac{2PR}{P+R}$, 是P和R的调和平均数：$\frac{1}{F1}=\frac{1}{2}(\frac{1}{P}+\frac{1}{R})$.

    <img src="pic\image-20200306103242559.png" alt="image-20200306103242559" style="zoom:67%;" />

  + ![image-20200306103401121](pic\image-20200306103401121.png)

  + ROC与AUC：TPR为所有判为正例中真正例的比例；FPR为所有判断为反例中真反例的比例；

    <img src="pic\image-20200306104857206.png" alt="image-20200306104857206" style="zoom: 80%;" />

  + 代价敏感错误率(cost-sensitive):

    <img src="pic\image-20200306105128476.png" alt="image-20200306105128476" style="zoom:80%;" />



### 比较检验

统计假设检验(hypothesis test)

+ 二项检验(binomal test)
+ t检验
+ 交叉t检验
+ Friedman检验与Nemenyi后续检验

(see page 40-42)

### 偏差与方差

![image-20200306185123512](pic\image-20200306185123512.png)

+ 期望输出$\bar f(x)=E_D[f(x;D)]$,即为所有训练集的输出的期望

+ $var(x)$是使用样本数相同的不同训练集产生的预测输出的方差

+ $bias^2(x)=(\bar f(x)-y)^2$是 **期望输出与真实标记之间的差别**

+ 噪声相当于系统误差

+ 假设噪声期望为0

  <img src="pic\image-20200306190820843.png" alt="image-20200306190820843" style="zoom:80%;" />

  

# Chracter3:线性模型

### 线性回归

+ 离散属性的处理：可用one-hot编码
+ 基本形式:$f(x)=w^Tx+b$
+ 通过最小化均方误差来求解(最小二乘法)
  + $(w^*,b^*)=argmin_{(w,b)} \sum_{i=1}^m(f(x_i)-y_i)^2=||w^Tx+b-y||_2^2$.
  + 直接求导可的最优解
  + <img src="pic\image-20200306192250509.png" alt="image-20200306192250509" style="zoom:67%;" />

+ 对数线性回归：$lny=w^Tx+b$.
+ 广义线性模型：$y=g^{-1} (w^Tx+b)$.

### 对数几率回归

+ 考虑二分类问题，对数几率函数：$y=\frac{1}{1+e^{-z}}$.

+ ![image-20200313104651353](pic\image-20200313104651353.png)

  y表示x作为正例的概率，1-y则为反例，其比值表示了x作为正例的相对可能性，比值大于1的话,ln就大于0

  优点：

  + 无需事先假设数据分布
  + 可得到类别的近似概率
  + 容易优化，可用许多数值优化算法

+ 似然函数： $P(Y|X)=\prod_{i=1}^n{n}p(y_i|x_i)$ ,取对数

  ![image-20200313110719852](pic\image-20200313110719852.png)