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
  + **最大化方差推导**：假定样本已经中心化，即$\sum_ix_i=0$，投影矩阵为$W$，$x_i$的投影为$W^Tx_i$。
  
    ![image-20200406210416557](pic\image-20200406210416557.png)
  
    **协方差相关详见https://blog.csdn.net/xueluowutong/article/details/85334256?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-2**
  
    
  
    得到样本点的协方差矩阵为$\sum_iW^Tx_ix_i^TW$，最大化方差，则优化目标可以写为
    $$
    \begin{align}
    \max_W&\quad tr(WXX^TW)\\
    s.t.&\quad W^TW=I
    \end{align}
    $$
    
  + **最近重构性推导**：样本已经中心化，假定投影变换后的新坐标系为$\{w_1,...,w_d\}$，$w_i$为标准正交基向量（$\|w_i\|_2=1,w_i^Tw_j=0(i\neq j)$，若丢弃新坐标系中的部分坐标，将维度降到$d'$，样本$x_i$的投影为$z_i=(z_{i1},...,z_{id'}),z_{ij}=w_j^Tx_i$，若基于$z_i$来重构$x_i$，得到$\hat{x_i}=\sum_{j=1}^{d'}z_{ij}w_j$。
  
    ![image-20200406213333223](pic\image-20200406213333223.png)
  
    用拉格朗日乘子法，求导后得到$XX^TW=\lambda W$. 算法：
  
    ![image-20200406213654360](pic\image-20200406213654360.png)
  
  + 推导详见**南瓜书https://datawhalechina.github.io/pumpkin-book/#/chapter10/chapter10**



# Chapter4:决策树

+ 基于树结构进行决策
  + 每个内部结点对应于某个属性上的“测试”
  + 每个分支对应于该测试的一种可能结果(即该属性的某个取值)
  + 每个叶结点对应于一个预测结果

+ **从根到叶递归：（ID3算法；J.Ross.Quinlan）**

  + 三种停止条件：
    + 当前结点包含的样本全属于同一类别，则无需再划分(已经全是好瓜，就不用再划分)
    + 当前属性集为空，或所有样本在所有属性上取值相同，无法划分（所有属性都用完了，没有feture再往下划分了，则将此节点标记为当前结点样本中样本数最多的类别(投票)；）
    + 当前结点包含的样本集合为空，不能划分（如颜色有红，白，黑，但训练数据中没有黑色样本，则看他父节点：父节点中好瓜多于坏瓜，则认为这个节点是好瓜）

+ **信息增益：information gain**

  + 信息熵(entropy)：度量样本集合“纯度”的一种指标，假定当前样本集合D中第K类样本所占的比例为$p_k$，则D的信息熵定义为
    $$
    Ent(D)=-\sum_{k=1}^{|y|}p_k\log_2p_k
    $$
    其值越小，D的纯度越高；当信息划分干净时，熵就小，如D中属于1类的有1个，属于0类的有0个，其熵为0；属于1类的有1个，属于0类的有1个，其熵大于0

  + 在决策树选择属性时，选择某个属性a划分得到V个结点，计算这V个结点的信息熵，加权(每个结点的样本数量占总的权重)累加；信息增益为：
    $$
    Gain(D,a)=Ent(D)-\sum_{v=1}^Vw^vEnt(D^v)，w^v=\frac{|D^v|}{|D|}
    $$
    选择使信息增益最大的属性作为划分属性

    好的条件就是信息增益越大越好，即变化完后熵越小越好（熵代表混乱程度，最大程度地减小了混乱）。因此我们在树分叉的时候，应优先使用信息增益最大的属性，这样降低了复杂度，也简化了后边的逻辑。

+ 可用于回归任务的决策树算法：CART(Classification and Regression Tree)
+ 基于决策树的最强大算法之一：RF(Random Forest)，集成学习
+ 信息增益对可取值数目比较多的属性有所偏好，有明显弱点，故考虑**增益率**：
  + $Gain\_ratio(D,a)=\frac{Gain(D,a)}{IV(a)}$， $IV(a)=-\sum_{v=1}^Vw^v\log_2w^v$.  分类数越多，IV越大，对应的增益率会变小，故增益率对可取值数目较小的属性偏好
  + 选择属性划分时考虑启发式(C4.5)：先从候选划分属性中找出信息增益高于平均水平的属性，再从中选择增益率最高的。
+ **基尼指数(gini index)**
  
  + ![image-20200327113739477](pic\image-20200327113739477.png)
  + 在候选属性集合中，选取那个使划分后基尼指数最小的属性，此时数据的纯度更高
+ 划分选择对**泛化性能的影响很有限**，**剪枝方法和程度对决策树泛化性能影响更显著**。
  + 剪枝是决策树对“过拟合”的主要手段
  + 预剪枝(pre-pruning)：提前终止某些分支的生长
    + 测试时间开销降低，训练时间开销降低，过拟合风险降低，欠拟合风险增加
  + 后剪枝(post-pruning)：生成一颗完全树，再回头剪枝
    + 测试时间开销降低，训练时间开销增加，过拟合风险降低，欠拟合风险基本不变
  + 泛化性能后剪枝通常优于预剪枝
  
+ **处理连续值的属性**：
  + 基本思路：**连续属性离散化**
    + 二分法：n个属性值可以形成n-1个候选划分，然后将它们当作n-1个离散属性值处理
      + 如在样本集D上有一个连续属性a，假定a在D上出现了n个不同的取值，则将这些值从小到大排序，定一个划分点t将这些取值划分开来
      + 当t处于a的两个相邻取值$[a_i,a_{i+1})$中的任意值时，划分结果相同，故可以分别令t取a的n个取值区间的中点，对这n个划分计算信息增益取最大化信息增益的那个划分

+ **处理缺失值属性**

  + 如何在属性值缺失的情况下进行划分属性选择？

    + 给定训练集D和属性a，令$\hat{D}$表示D中在属性a上没有缺失值的样本子集，可以仅根据$\hat{D}$来判断a的优劣

    + $a=(a^1,...a^V)$，$\hat{D}^v$表示$\hat{D}$取值为$a^v$的样本子集，$\hat{D}_k$表示$\hat{D}$中属于第k类的样本子集

    + 有$\hat{D}=\bigcup_{k=1}^{|Y|}\hat{D}_k$，$\hat{D}=\bigcup_{v=1}^{|V|}\hat{D}^v$。为每个样本赋予一个权重，定义：

      <img src="pic\image-20200403095555196.png" alt="image-20200403095555196" style="zoom: 80%;" />

      对于属性a，$\rho$表示无缺失值样本所占比例，$\hat{\rho}_k$表示无缺失值样本中第k类所占比例，$\hat{r_v}$表示无缺失值样本中在属性a上取值为$a^v$的样本所占比例。将信息增益推广为：

      <img src="pic\image-20200403100002350.png" alt="image-20200403100002350" style="zoom:80%;" />

  + 给定划分属性，若样本在该属性上的值缺失，如何对样本进行划分？

    + 若样本x在属性a上取值已知，则将x划入对应取值的子节点，且样本权值为$w_x$。
    + 否则，将x同时划入所有子节点，且样本权值在与属性值$a^v$对应的子节点中调整为$\hat{r_v}\times w_x$。即让同一个样本以不同的概率划入到不同的子节点中去。

+ 一棵决策树对应于一个规则集，可以将规则进行合并等操作，提升泛化性能【C4.5Rule】

+ **多变量决策树**

  + 每个非叶结点是一个形如$\sum_{i=1}^dw_ia_i=t$的线性分类器，$w_i$表示属性$a_i$的权重，如这个结点：*-0.8x密度-0.044x含糖率 < -0.313?* 
  + 混合决策树可以在结点中嵌入神经网络等



# Chapter5:神经网络

### 神经元模型

+ “神经网络是由具有适应性的简单单元组成的广泛并行互联的网络，它的组织能够模拟生物神经系统对真实世界物体所作出的反应”----Kohonen

+ M-P神经元模型

  <img src="pic\image-20200417111341720.png" alt="image-20200417111341720" style="zoom:80%;" />

+ 神经网络的万有逼近性：（任何通用机器学习模型都要具有万有逼近性）“仅需一个包含足够多神经元的隐层，多层前馈神经网络就能以任意精度逼近任意复杂度的连续函数”----Hornik

+ 感知机（Perceptron）：由两层神经元组成，输入层接收外界输入信号后传递给输出层（M-P神经元），也称阈值逻辑单元。

  <img src="pic\image-20200417111557014.png" alt="image-20200417111557014" style="zoom:67%;" />

  

### 反向传播算法

+ BackPropagation：

  给定训练集$D=\{(x^1,y^1),...(x^m,y^m\}$，$x$为$d$维向量，$y$为$l$维向量，在如图的网络中：

  ![image-20200417170638369](pic\image-20200417170638369.png)

  假设隐层和输出层神经元都使用Sigmoid函数$f(x)=\frac{1}{1+e^{-x}}$，有
  $$
  f'(x)=-\frac{1}{(1+e^{-x})^2}\times -e^{-x}=\frac{1}{1+e^{-x}}\times \frac{e^{-x}}{1+e^{-x}}=f(x)(1-f(x))\\
  f(-x)=1-f(x)\\
  f'(-x)=-1\times f(-x)\times(1-f(-x))=-(1-f(x))f(x)=-f'(x)
  $$
  对于$(x^k,y^k)$，假设神经网络输出为$\hat{y_k}=(\hat{y_1}^k,...\hat{y_l}^k)$，即$f(\beta_j-\theta_j)=\hat{y_j}^k$. 用均方误差作为loss：
  $$
  E_k=\frac{1}{2}\sum_{j=1}^l(\hat{y_j}^k-y_j^k)^2
  $$
  则第j个输出神经元的权重更新为：
  $$
  \Delta w_{hj}=-\eta\frac{\partial E_k}{\partial w_{hj}}
  $$
  由链式法则$w_{hj}\rightarrow\beta_j\rightarrow\hat{y_j}^k$,得到
  $$
  \begin{align}
  \frac{\partial E_k}{\partial w_{hj}}&=\frac{\partial E_k}{\partial\hat{y_j}^k}\times
  \frac{\partial\hat{y_j}^k}{\partial\beta_j}\times\frac{\partial\beta_j}{\partial w_{hj}}\\
  &=(\hat{y_j}^k-y_j^k)\times \hat{y_j}^k(1-\hat{y_j}^k)\times b_h
  \end{align}
  $$
  从而
  $$
  \Delta w_{hj}=\eta g_jb_h
  $$
  其中
  $$
  \begin{align}
  g_j&=\hat{y_j}^k(1-\hat{y_j}^k)(y_j^k-\hat{y_j}^k)\\
  &=-\frac{\partial E_k}{\partial \hat{y_j}^k}\frac{\partial\hat{y_j}^k}{\partial\beta_j}\\
  &=-\frac{\partial E_k}{\partial \beta_j}
  \end{align}
  $$
  由Sigmoid函数性质，$\hat{y_j}^k=f(\beta_j-\theta_j)$容易得到
  $$
  \frac{\partial E_k}{\partial \theta_j}=\frac{\partial E_k}{\partial \hat{y_j}^k}\frac{\partial \hat{y_j}^k}{\partial \theta_j}=
  -\frac{\partial E_k}{\partial \beta_j}=g_j
  $$
  第j个输出神经元的阈值更新为：
  $$
  \begin{align}
  \Delta \theta_j&=-\eta\frac{\partial E_k}{\partial \theta_{j}}\\
  &=-\eta\frac{\partial E_k}{\partial\hat{y_j}^k}\times
  \frac{\partial\hat{y_j}^k}{\partial\theta_j} \\
  &=-\eta(\hat{y_j}^k-y_j^k)\times [-1\times(1-\hat{y_j}^k)\hat{y_j}^k]\\
  &=-\eta g_j
  \end{align}
  $$
  第h个隐层神经元的权重更新为：
  $$
  \begin{align}
  \Delta v_{ih}&=-\eta \frac{\partial E_{k}}{\partial v_{ih}}
  \end{align}
  $$
  由链式法则$v_{ih}\rightarrow \alpha_{h}\rightarrow b_h\rightarrow\beta\rightarrow\hat{y}^k$,得到
  $$
  \begin{align}
  \frac{\partial E_{k}}{\partial v_{ih}}&=\frac{\partial E_k}{\partial b_h}\times
  \frac{\partial b_h}{\partial \alpha_h}\times\frac{\partial \alpha_h}{\partial v_{ih}}
  \end{align}
  $$
  其中后两项由$b_h=f(\alpha_h-\gamma_h)$得到为$b_h(1-b_h)\times x_i^k$，其中$x_i^k$代表$x^k$的第$i$个分量
  $$
  \begin{align}
  \frac{\partial E_k}{\partial b_h}&=\sum_{j=1}^l\frac{\partial E_k}{\partial \hat{y_j}^k}\times\frac{\partial \hat{y_j}^k}{\partial \beta_j}\times\frac{\partial \beta_j}{\partial b_h}\\
  &=\sum_{j=1}^l(-g_j)\times w_{hj}
  \end{align}
  $$
  综合得到
  $$
  \Delta v_{ih}=\eta(\sum_{j=1}^l g_jw_{hj})b_h(1-b_h)x_i^k=\eta e_hx_i^k
  $$
  其中
  $$
  \begin{align}
  e_h&=b_h(1-b_h)\sum_{j=1}^l g_jw_{hj}\\
  &=-\frac{\partial E_k}{\partial b_h}\frac{\partial b_h}{\partial\alpha_h}\\
  &=-\frac{\partial E_k}{\partial \alpha_h}
  \end{align}
  $$
  由Sigmoid函数性质，$b_h=f(\alpha_{h}-\gamma_h)$可得
  $$
  \frac{\partial E_k}{\partial \gamma_h}=\frac{\partial E_k}{\partial b_h}\frac{\partial b_h}{\partial\gamma_h}=-\frac{\partial E_k}{\partial \alpha_h}=e_h
  $$
  第h个隐层神经元的阈值更新为：
  $$
  \begin{align}
  \Delta\gamma_h&=-\eta\frac{\partial E_{k}}{\partial \gamma_h}\\
  &=-\eta\frac{\partial E_k}{\partial b_h}\frac{\partial b_h}{\partial \gamma_h}\\
  &=-\eta e_h
  \end{align}
  $$



+ **标准BP算法描述**：

  <img src="pic\image-20200417183238278.png" alt="image-20200417183238278" style="zoom: 50%;" />

+ <img src="pic\image-20200417183343253.png" alt="image-20200417183343253" style="zoom:50%;" />

  在很多任务中，累积误差下降到一定程度后进一步下降会十分缓慢这时标准BP算法往往会获得较好的解。

+ 缓解过拟合，两种策略：

  <img src="pic\image-20200417183518470.png" alt="image-20200417183518470" style="zoom:50%;" />

### 全局最小与局部极小

+ 局部极小local minimum与全局最小global minimum
  + 对$w^*,\theta^*$，若存在$\epsilon>0$使得任意$(w;\theta)\in\{(w;\theta)|\|(w;\theta)-(w^*,\theta^*)\|\leq\epsilon\}$都有$E(w;\theta)\geq E(w;\theta^*)$，则称其为局部极小解。（E为训练误差）
  + 对参数空间中的任意$(w;\theta)$都有$E(w;\theta)\geq E(w;\theta^*)$，则称其为全局最小解。
+ 有可能跳出局部最小的方法：
  + 以多组不同参数值初始化多个神经网络，按标准方法训练后，取其中误差最小的解作为最终参数。
  + 模拟退火算法，每一步有一定概率接受比当前解更差的结果。
  + 随机梯度下降，即便陷入局部极小点，它计算出的梯度仍可能不为0。
  + 遗传算法。

### 其他神经网络、深度学习

+ RBF网络（径向基函数网络）
+ ART网络（自适应谐振理论网络），可进行增量学习（接收到训练样例时仅需根据新样例对模型更新，而不必重新训练模型）或在线学习（每获得一个新样本就进行一次模型更新）

+ SOM网络（自组织映射网络）
+ 级联相关网络：结构自适应网络，可以学习网络结构
+ Elman网络：一种递归神经网络
+ Boltzmann机
+ 深度学习：多隐层网络训练
  + 无监督逐层训练：每次训练一层隐节点，训练时将上一层隐节点的输出作为输入，而本层隐节点的输出作为下一层隐节点的输入，称为“预训练”；完成预训练后，再对整个网络进行“微调”（比如用BP算法对整个网络训练）
  + 权共享：让一组神经元使用相同的连接权，如卷积神经网络
  + 理解：对输入信号进行逐层加工，从而把初始的、与输出目标之间联系不太密切的输入表示，转化为与输出目标更密切的表示。即通过多层处理，逐渐将初始的低层特征表示转化为高层特征表示，用简单模型完成复杂的分类等学习任务。



# Chapter6:支持向量机

### SVM基本型

+ 给定训练样本集$D=\{(x_i,y_i)\},y_i\in\{-1,1\},i=1,...m$，假设训练集线性可分，容易知道应该找到位于两类样本“正中间”的划分超平面

  + 划分超平面：$w^Tx+b=0$。设样本空间中任意点到超平面的距离为 $r$

    ![](pic\20180823151007260.png)

    易得 $x=x_0+r\frac{w}{\|w\|}$。将$w^Tx_0+b=0$代入，得到 $r=\frac{w^Tx+b}{\|w\|}$ 。

  +  假设超平面能正确分类，则存在$\delta>0$使
    $$
    \begin{align}
    &w^Tx_i+b\geq\delta,\quad y_i=+1\\
    &w^Tx_i+b\leq-\delta,\quad y_i=-1
    \end{align}
    $$
    两边同时除以$\delta$，则可以得到有
    $$
    \begin{align}
    &w^Tx_i+b\geq 1,\quad y_i=+1\\
    &w^Tx_i+b\leq-1,\quad y_i=-1\\
    \text{从而有 }&y_i(w^Tx_i+b)\geq1
    \end{align}
    $$
    距离超平面最近的点使得等式成立，它们称为**支持向量**。

    ![](pic\5bc72f6a838c4.png)

    定义**间隔**为两个异类支持向量到超平面的距离之和
    $$
    \gamma=\frac{2}{\|w\|}
    $$
    则目标变为找到具有最大间隔(maximum margin)的划分超平面：
    $$
    \begin{align}
    &\max_{w,b}\quad\frac{2}{\|w\|}\\
    &s.t.\quad y_i(w^Tx_i+b)\geq1,\quad i=1,...,m
    \end{align}
    $$
    等价于
    $$
    \begin{align}
    &\min_{w,b}\quad\frac{1}{2}\|w\|^2\\
    &s.t.\quad y_i(w^Tx_i+b)\geq1,\quad i=1,...,m
    \end{align}
    $$
    这是一个凸的二次规划问题，解这个问题的$w$不是稀疏的，所有样本都会对$w$产生影响；但是解它的对偶问题得到的解$w$是稀疏的。

### 对偶问题

+ **拉格朗日方法**：
  $$
  \begin{align}
  \min_x\quad&f_0(x)\\
  s.t.\quad&f_i(x)\leq0,\quad i=1,...,m\\&h_i(x)=0,\quad i=1,...,p
  \end{align}
  $$
  对等式约束和不等式约束引入拉格朗日乘子  $v_i,\lambda_i$  得到**拉格朗日函数**：
  $$
  L(x,\lambda,v)=f_0(x)+\sum_{i=0}^m\lambda_if_i(x)+\sum_{i=1}^pv_ih_i(x)
  $$
  进一步得到**拉格朗日对偶函数**：$g(\lambda,v)=\inf_xL(x,\lambda,v)$.

  **拉格朗日对偶问题**为：
  $$
  \begin{align}
  \max\quad &g(\lambda,v)\\
  s.t.\quad&\lambda\succcurlyeq0
  \end{align}
  $$
  对偶问题构成了原问题最优值的下界，当**Slater条件**成立时，强对偶性成立，即**两个问题的最优解相等**。

  强对偶性成立时，有最优性条件：**KKT条件**：
  $$
  \begin{align}
  f_i(x^*)\leq0&,\quad i=1,...,m\\
  h_i(x^*)=0&,\quad i=1,...,p\\
  \lambda_i^*\geq0&,\quad i=1,...,m\\
  \lambda_i^*f_i(x^*)=0&,\quad i=1,...,m\quad\text{(由互补松驰性得到)}\\
  \nabla L(x^*,\lambda^*,v^*)=0
  \end{align}
  $$
  
+ 应用拉格朗日乘子法，得到上面问题的对偶函数/拉格朗日函数：
  $$
  L(w,b,\alpha)=\frac{1}{2}\|w\|^2+\sum_{i=1}^m\alpha_i(1-y_i(w^Tx_i+b)),\quad\alpha=(\alpha_1,...,\alpha_m)
  $$
  由KKT条件对w和b求偏导为0得到 $\quad w=\sum_{i=1}^m\alpha_iy_ix_i,\quad 0=\sum_{i=1}^m\alpha_iy_i$。代入上式得到**拉格朗日对偶函数**：

  <img src="pic\image-20200406193638955.png" alt="image-20200406193638955" style="zoom:80%;" />

  所以其对偶问题为$\max_\alpha\min_{w,b}L(w,b,\alpha)$，即
  $$
  \begin{align}
  \max_\alpha&\quad \sum_{i=1}^m\alpha_i-\frac{1}{2}\sum_{i=1}^m\sum_{j=1}^m\alpha_i\alpha_jy_iy_jx_i^Tx_j\\
  s.t.&\quad\sum_{i=1}^m\alpha_iy_i=0,\\
  &\quad\alpha_i\geq0,\quad i=1,...,m
  \end{align}
  $$
  解出$\alpha$后，即可得到w，对于$\alpha_i$不为0的样本，$y_i(w^Tx_i+b)=1$，代入w即可得到b，但实际上常使用所有支持向量求得的b相加再求平均，更鲁棒。

  令$f(x_i)=w^Tx_i+b$，得到模型$f(x)=w^Tx+b=(\sum_{i=1}^m\alpha_iy_ix_i^Tx)+b$。由KKT条件得:
  $$
  \begin{align}
  &\alpha_i\geq0\\
  &1-y_if(x_i)\leq0\\
  &\alpha_i(1-y_if(x_i))=0
  \end{align}
  $$
  故对一个样本来说，要么$\alpha_i=0$要么$y_if(x_i)=1$，**若为前者，则该样本将不会在模型$f(x)$的求和项中出现，若为后者，则表明该样本为支持向量**。

+ **SMO算法**求解该对偶问题。

  + 执行以下步骤直到收敛：

    + 选取一对需更新的变量$\alpha_i,\alpha_j$
    + 固定$\alpha_i,\alpha_j$以外的参数，求解对偶式得到更新后的$\alpha_i,\alpha_j$

  + <img src="pic\image-20200410103941772.png" alt="image-20200410103941772" style="zoom:67%;" />

    $c=-\sum_{k\neq i,j}\alpha_ky_k$为常数。



### 核函数

+ 训练样本线性不可分时，可将样本从原始空间映射到一个更高维的特征空间，使得样本在这个特征空间中线性可分。如果原始空间是有限维的，则一定存在一个高维特征空间使得训练集线性可分。

+ $x$被映射为$\phi(x)$。将上面的所有x都换掉即得到变换后的问题。用**核函数**来求解样本在特征空间的内积：
  $$
  \kappa(x_i,x_j)=\phi(x_i)^T\phi(x_j)
  $$
  

  ![](pic\5bc730cc49adc.png)

  + 因此，核函数可以直接计算隐式映射到高维特征空间后的向量内积，而不需要显式地写出映射后的结果，它虽然完成了将特征从低维到高维的转换，但最终却是在低维空间中完成向量内积计算，与高维特征空间中的计算等效**（低维计算，高维表现）**，从而避免了直接在高维空间无法计算的问题。引入核函数后，原来的对偶问题与分类函数则变为：

    + 对偶问题：

      <img src="pic\5bc730cc173b2.png" style="zoom: 67%;" />

    + 分类函数：

      <img src="pic\5bc730cc05959.png" style="zoom:67%;" />

  + <img src="pic\image-20200406202508516.png" alt="image-20200406202508516" style="zoom:67%;" />

  + 在线性不可分问题中，核函数的选择成了支持向量机的最大变数，若选择了不合适的核函数，则意味着将样本映射到了一个不合适的特征空间，则极可能导致性能不佳。常用核函数为：

    ![image-20200406202705518](pic\image-20200406202705518.png)

    若$\kappa_1,\kappa_2$为核函数，有

    + 对任意正数$\gamma_1,\gamma_2$，其线性组合$\gamma_1\kappa_1+\gamma_2\kappa_2$也是核函数。
    + 核函数的直积也是核函数 $\kappa_1\bigotimes\kappa_2(x,z)=\kappa_1(x,z)\kappa_2(x,z)$。
    + 对任意函数$g(x)$，$\kappa(x,z)=g(x)\kappa_1(x,z)g(z)$也是核函数。
    
    基本经验：**文本数据常用线性核，情况不明时可尝试高斯核**。
    
  + <img src="pic\image-20200410110519500.png" alt="image-20200410110519500" style="zoom:67%;" />



### 软间隔与正则化

+ 允许某些点不满足约束$y_i(w^Tx_i+b)\geq1$，“出现在间隔里面”；我们期望在最大化间隔同时，不满足约束的样本尽可能少，于是优化目标变为：
  $$
  \min_{w,b}\frac{1}{2}\|w\|^2+C\sum_{i=1}^ml_{0/1}(y_i(w^Tx_i+b)-1)\\
  l_{0/1}=
  \begin{cases}
  1,\quad z<0\\
  0,\quad otherwise
  \end{cases}
  $$
  C为大于0的常数，当C为无穷大时，为了最小化目标，迫使所有样本都满足约束使得后面的求和项为0.

  $l_{0/1}$非凸，不连续，常用**替代损失函数**：

  ![image-20200408222125444](pic\image-20200408222125444.png)

  采用hinge损失：当满足约束时，求和项为0；不满足时，大于0
  $$
  \min_{w,b}\frac{1}{2}\|w\|^2+C\sum_{i=1}^m\max(0,1-y_i(w^Tx_i+b))
  $$
  引入松弛变量$\xi_i\geq\max(0,1-y_i(w^Tx_i+b))$：即所有样本满足松弛后的约束$y_i(w^T_ix_i+b)\geq1-\xi_i$，后面是个“惩罚项”，为了使其不过于太松弛
  $$
  \begin{align}
  \min_{w,b}&\quad\frac{1}{2}\|w\|^2+C\sum_{i=1}^m\xi_i\\
  s.t.&\quad y_i(w^Tx_i+b)\geq1-\xi_i\\
  &\quad\xi_i\geq0,\quad i=1,...,m
  \end{align}
  $$
  类似地，得到拉格朗日函数：

  ![image-20200408223335272](pic\image-20200408223335272.png)

  对$w,b,\xi_i$求$\inf$得：
  $$
  w=\sum_{i=1}^m\alpha_iy_ix_i,\quad0=\sum_{i=1}^m\alpha_iy_i,\quad C=\alpha_i+\mu_i
  $$
  得到对偶问题：

  ![image-20200408223801256](pic\image-20200408223801256.png)

  **与硬间隔的对偶问题差别在与对$\alpha$的约束不同**。其KKT条件为：

  ![image-20200408224132717](pic\image-20200408224132717.png)

  对任意训练样本，总有$\alpha_i=0$或$y_if(x_i)=1-\xi_i$.

  + 若$\alpha_i=0$ , 则该样本不会对模型产生影响
  + 若$\alpha_i>0$，则必有$y_if(x_i)=1-\xi_i$，即该样本为支持向量，由$C=\alpha_i+\mu_i$知
    + 若$\alpha_i<C$，则有$\mu_i>0$，因此$\xi_i=0$，该样本正好在最大间隔边界上
    + 若$\alpha_i=C$，则有$u_i=0$，
      + 若$\xi_i\leq 1$，则该样本落在最大间隔内部
      + 若$\xi_i>1$，则该样本被错误分类

  因而软间隔支持向量机的最终模型仅和支持向量有关，采用hinge损失函数保持了稀疏性。

  <img src="pic\image-20200408225027009.png" alt="image-20200408225027009" style="zoom:67%;" />



### 支持向量回归

+ 希望学得$f(x)=w^Tx+b$，使得$f(x),y$尽可能接近

+ Support Vector Regression假设能容忍$f(x)$与$y$之间最多有$\epsilon$的误差，即当它们两个的差的绝对值大于$\epsilon$时才计算损失

+ 形式化SVR：
  $$
  \min_{w,b}\frac{1}{2}\|w\|^2+C\sum_{i=1}^ml_\epsilon(f(x_i)-y_i)\\
  l_{0/1}=
  \begin{cases}
  0,\quad &|z|\leq\epsilon\\
  |z|-\epsilon,\quad &otherwise
  \end{cases}
  $$
  对每个点需要两个松弛变量：因为$f(x_i)-\epsilon\leq y_i\leq f(x_i)+\epsilon$，所以$f(x_i)-\epsilon-\xi_i\leq y_i\leq f(x_i)+\epsilon+\hat{\xi_i}$
  $$
  \begin{align}
  \min_{w,b}&\quad\frac{1}{2}\|w\|^2+C\sum_{i=1}^m(\xi_i+\hat{\xi_i})\\
  s.t.&\quad f(x_i)-y_i\leq\epsilon+\xi_i\\
  &\quad y_i-f(x_i)\leq\epsilon+\hat{\xi_i}\\
  &\quad\xi_i\geq0,\hat{\xi_i}\geq0,\quad i=1,...,m
  \end{align}
  $$
  得到拉格朗日函数：

  <img src="pic\image-20200408231525962.png" alt="image-20200408231525962" style="zoom:80%;" />

  对$w,b,\xi_i$求$\inf$得：
  $$
  w=\sum_{i=1}^m(\hat{\alpha_i}-\alpha_i)x_i,\quad0=\sum_{i=1}^m(\hat{\alpha_i}-\alpha_i),\quad C=\alpha_i+\mu_i,\quad C=\hat{\alpha_i}+\hat{\mu_i}
  $$
  得到对偶问题：

  <img src="pic\image-20200408231814498.png" alt="image-20200408231814498" style="zoom: 80%;" />

  KKT条件为：

  <img src="pic\image-20200408231856437.png" alt="image-20200408231856437" style="zoom:80%;" />

  得到解$f(x)=\sum_{i=1}^m(\hat{\alpha_i}-\alpha_i)x_i^Tx+b$，使$\hat{\alpha_i}-\alpha_i\neq0$的样本为支持向量，它们必然落在$\epsilon$间隔带之外

  因为：

  + 当且仅当$f(x_i)-y_i-\epsilon-\xi_i=0$时$\alpha_i$才能取非零值；当且仅当$f(x_i)-y_i-\epsilon-\hat{\xi_i}=0$时$\hat{\alpha_i}$才能取非零值。即样本不落入$\epsilon$间隔带中它们才能取0值。且这两个为0不能同时成立，所以$\alpha_i,\hat{\alpha_i}$中至少有一个为0

  <img src="pic\image-20200408232438799.png" alt="image-20200408232438799" style="zoom:80%;" />



### 核方法

+ ![image-20200408232957481](pic\image-20200408232957481.png)

+ 核方法(kernel methods)常通过引入核函数来将线性学习器拓展为非线性学习器

+ 对LDA进行“核化”得到**“核线性判别分析”KLDA**：

  西瓜书P138

  