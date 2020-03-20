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

+ 解得$p(y=1|x)=\frac{e^{w^Tx+b}}{1+e^{w^Tx+b}},p(y=0|x)=\frac{1}{1+e^{w^Tx+b}}$.

+ y的分布列为$P(Y|X)=p_1^y\times (1-p_1)^{1-y}$.(伯努利分布)

+ 令$w^Tx+b=\beta^Tx$，似然函数： $L(\beta)=L(\beta;X_1,\cdots,X_n)=\prod_{i=1}^np(y_i|x_i)$ ,取对数，得到
$$
  \begin{align}
  L(\beta)&=\sum_{i=1}^ny_iln(p_1)+(1-y_i)ln(1-p_1)\\
  &=\sum_{i=1}^n(y_i\beta^Tx-ln(1+e^{\beta^Tx}))
  \end{align}
$$
  最大化对数似然，等价于最小化：
$$
  \mathcal{l}(\beta)=\sum_{i=1}^n(-y_i\beta^Tx+ln(1+e^{\beta^Tx}))
$$
  ![image-20200313110719852](pic\image-20200313110719852.png)

+ 最优化方法：梯度下降与牛顿法

  + 将$f(x)$泰勒展开：
    $$
    f(x)=f(x_k)+\nabla f(x_k)^T(x-x_k)+\frac{1}{2}(x-x_k)^T\nabla^2f(x_k)(x-x_k)
    $$
    由一阶条件知其一阶导数为0:
    $$
    \nabla f(x_k)^T+\nabla^2f(x_k)(x-x_k)=0\\
    x=x_k-\nabla^2f(x_k)^{-1}\nabla f(x_k)
    $$
    得到迭代公式

    ![image-20200313181937803](pic\image-20200313181937803.png)

### **Add:**MLE与MAP

+ 核心：贝叶斯公式
  $$
  P(\theta|X)=\frac{P(X|\theta)P(\theta)}{P(X)}\rightarrow posterior=\frac{likehood*prior}{evidence}
  $$
  posterior：通过样本X得到的参数$\theta$的概率，即**后验概率**

  likehood：通过参数$\theta$得到样本X的概率，**似然函数**

  prior：参数$\theta$的先验概率，一般是根据人的先验知识得来的

  evidence：样本X发生的概率，$P(X)=\int p(X|\theta)p(\theta)d\theta$，是各种$\theta$条件下样本X发生的概率的积分或求和

+ MLE: Maximum Likelihood Estimation，最大似然估计，是频率学派的估计方法

  + 关于参数$\theta$的似然函数为 $L(\theta|data)$，

  + 理解：概率是给定参数$\theta=(p_1,...p_n)$后，预测即将发生的事件的可能性

    + 如已知硬币正面概率$p_H$和反面概率$p_T$为0.5，这个p就是参数$\theta$。预测抛两次硬币，全部正面朝上的概率。
    + 即$data=(x_1,x_2)=(H,H)$, $P(HH|\theta)=P(HH|p_H=0.5;p_T=0.5)=p_H\times p_H=0.25$.
    + $P(HHT|\theta)=p_H^2(1-p_H)$ ，当$p_H=0.66$时似然函数是最大的，即**从现有的数据中看，参数$p_H=0.66$是看起来最“似然”的**。
    + **似然**就是反过来，已知事件data，求参数$\theta$，使得**在参数$\theta$下，事件data发生的概率是最大的**，即**对某一个参数$\theta$的猜想的概率**
    + 核心思想：认为当前发生的事件是概率最大的事件

  + 推导：分号只是用来隔离参数,$data=(X_1,...X_n)$。而data是已发生事件，P(data)为1
    $$
    L(\theta|data)=P(\theta|data)=\frac{P(data;\theta)}{P(data)}=P(data;\theta)=P_\theta(data)\text{ 表示给定参数下data发生的概率}\\L(\theta|data)=\prod_{i=1}^nP(X_i;\theta),\text{取对数得到对数似然}\\
    \theta_{MLE}=argmax\text{ }P(\theta|data)=argmax \sum_{i=1}^n\log P(X_i;\theta)
    $$
    .

+ MAP: Maximum A Posteriori, 最大后验估计，引入了先验概率分布，贝叶斯学派

  + 在MLE中，将$\theta$看做是未知的参数，但它是一个定值，只是这个值未知。即最大似然估计是的函数，其求解过程就是找到使得最大似然函数最大的那个参数。

  + 最大后验估计，将参数$\theta$看成一个随机变量，并在已知样本集data的条件下，估计参数。$\theta$是有概率意义的

  + 推导：
    $$
    \theta_{MAP}=argmax\text{ }P(\theta|data)=argmax\text{ }P(data|\theta)P(\theta)
    $$
    这里的$P(data|\theta)$和MLE的$P(data;\theta)$只是记法不一样。
    $$
    \begin{align}
    \log P(data|\theta)P(\theta)&=\log P(data|\theta)+\log P(\theta)\\
    &=\log \prod_{i=1}^nP(X_i|\theta)+\log P(\theta) \\
    &=\sum_{i=1}^n\log P(X_i|\theta) +\log P(\theta)
    \end{align}
    $$
    可以看到MAP的优化函数只比MLE多了一个$\log P(\theta)$，而$P(\theta)$是由先验分布给出的，通常是$\beta$分布或高斯分布

  + 例如：对于投硬币的例子来看，我们认为（”先验地知道“）$\theta$ 取0.5的概率很大，取其他值的概率小一些。我们用一个高斯分布来具体描述我们掌握的这个先验知识，例如假设 $P(\theta)$ 为均值0.5，方差0.1的高斯函数

### 线性判别分析(Linear Discriminant Analysis)

+ 给定训练样例集，设法将样例投影到一条直线上，使得同类样例的投影点尽可能接近，异类的尽可能远离

+ <img src="pic\image-20200313192618233.png" alt="image-20200313192618233" style="zoom:80%;" />

  <img src="pic\image-20200313192742456.png" alt="image-20200313192742456" style="zoom:80%;" />

  <img src="pic\image-20200313192808679.png" alt="image-20200313192808679" style="zoom:80%;" />

  拉格朗日乘子：
  $$
  \min l(w,\lambda)=-w^TS_bw+\lambda(w^TS_ww-1)\\
  \text{微分:}-S_bw+\lambda S_ww=0\\
  w^TS_ww-1=0\\
  S_bw=(u_0-u_1)((u_0-u_1)^Tw),\text{后者是个标量，所以其方向为}u_0-u_1
  $$
  
+ LDA的多分类任务：

  + 假定存在N个类别，第i类示例数为$m_i$,**全局散度矩阵**定义为：
    $$
    S_t=S_b+S_w=\sum_{i=1}^m(x_i-u)(x_i-u)^T
    $$
    $u$为所有示例的均值向量，**类内散度矩阵**重定义为每个类别的散度矩阵之和：
    $$
    S_w=\sum_{i=1}^NS_{w_i},S_{w_i}=\sum_{x\in X_i}(x-u_i)(x-u_i)^T
    $$
    

  


### 多分类学习

+ 拆解法：分为若干个二分类任务
  + 一对一(OVO)：训练$C_N^{2}=\frac{N(N-1)}{2}$个分类器
  + 一对其余(OVR):每次将一个类作为正类，其余作为父类，训练N个分类器：存在类别不平衡问题
  + 多对多(MVM)：每次将若干个类作为正类，若干个其他类作为负类
+ MVM：纠错输出码(Error Correcting Output Codes, ECOC)
  + 编码：对N个类别做M次划分，每次将一部分类别划分为正类，一部分划为反类，从而产生M个分类器
  + 解码：M个分类器分别对测试样本进行预测，产生一个编码，将预测编码与各个类别的编码比较，返回距离最小的类别
  + ![image-20200320110754825](pic\ML_Note.md)
  + 海明距离是：各个位上不相等的总个数；注意与曼哈顿距离区分开
  + 停用类在计算距离时通常有个系数，如0.5

### 类别不平衡问题

+ 假设正例样本小于负例样本
+ 几率$\frac{y}{1-y}$反映了正例可能性与负例可能性的比值
  + 若$\frac{y}{1-y}>1$，预测为正例，这里假设的是正例与负例样本平衡
  + 若$\frac{y}{1-y}>\frac{m^+}{m^-}$，则预测为正例，$m^+,m^-$表示正例样本与负例样本的个数：假设训练集是真实样本总体的无偏采样，故观测几率就代表了真实几率
  + 做一些变换，使得分类器用原来的（即判定>1是正例的分类器）：令$$\frac{y'}{1-y'}=\frac{y}{1-y}\times\frac{m^-}{m^+}$$。叫做**再缩放rescaling**
+ **训练集是真实样本的无偏采样**常常不成立，可采用：
  + 欠采样undersapling：去除一些反例使得正反例样本平衡
    + EasyEnsemble算法
  + 过采样oversampling：增加一些正例使得正反例样本平衡
    + SMOTE算法
  + 阈值移动threshold-moving：用原始数据训练，决策时使用$$\frac{y'}{1-y'}=\frac{y}{1-y}\times\frac{m^-}{m^+}$$。

### 主成分分析

+ Principal Component Analysis:降维，无监督学习
  + 最大化方差推导：
  + 



## TODO: 拉格朗日对偶，奇异值分解与特征值分解，PCA推导，矩阵求导

