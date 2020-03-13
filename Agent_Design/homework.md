# 课后练习

### 1.1

+ Agent: 用传感器来感受环境并用执行器来与环境交互作用的事物
+ Agent函数：一种数学描述，将Agent的感知序列映射为动作
+ Agent程序：Agent函数在代码上的具体实现
+ 理性：每一步动作都选择让目标期望收益最大化的
+ 自主：有学习能力，能够通过学习改正或完善自身知识
+ 反射Agent:仅仅根据当前的感知来选择行动
+ 基于模型的Agent: 内部有模型会根据感知历史来维持内部状态，模型是关于世界如何运作的世界模型
+ 基于目标的Agent:能用目标信息来描述想要达到的状态

+ 基于效用的Agent：能使用更为细致通用的性能度量来对状态进行赋值，即效用函数
+ 学习Agent：由学习元件、评判元件、性能元件和问题产生器组成的Agent

### 1.2

```python
#-------基于目标的Agent--------

def goal_based_agent():
    state=UPDATE_STATE(state,action,percept,model)
    actions=GET_AVALIABLE_ACTION(state)    #获得当前状态下所有合法的行动
    next_states=UPDATE_STATE_IN_MODEL(state,actions,action_history)  #在model中采取行动得到下一个状态列表
    action=CHOOSE_ACTION_BASED_GOAL(actions,next_states,goal) #根据目标选择最优动作
    return action

#-------基于效用的Agent--------

def utility_based_agent():
    state=UPDATE_STATE(state,action,percept,model)
    actions=GET_AVALIABLE_ACTION(state)    #获得当前状态下所有合法的行动集合
    next_states=UPDATE_STATE_IN_MODEL(state,actions,action_history)  #在model中采取行动得到下一个状态集合
    action=CHOOSE_ACTIONS_BASED_GOAL(actions,next_states,goal) #根据目标选择最优动作集合
    best_action=CHOOSE_ACTION_BASED_UTILITY(action,state) #根据效用函数选择最优动作
    return best_action

```

### 2.1

令$X,Y$表示随机变量生命和水，由题意知：

|  X   |  Y   | P(X,Y) |
| :--: | :--: | :----: |
|  0   |  0   |  0.25  |
|  0   |  1   |   0    |
|  1   |  0   |  0.25  |
|  1   |  1   |  0.5   |

则有：$$P(X=1|Y=1)=\frac{P(X=1,Y=1)}{P(Y=1)}=\frac{0.5}{0.5}=1$$

故在给定有水的前提下，火星上有生命的概率为１

### 2.2

+ 我们有：

  $$
  \begin{align} P(S_t|O_{0:t}) &= P(S_t|O_{0:t-1},O_t) \\ &=\frac{P(O_t|S_t,O_{0:t-1})P(S_t|O_{0:t-1})}{P(O_t|O_{0:t})}\end{align}
  $$
  而:
  $$
  \begin{align} P(O_t|O_{0:t-1}) &= \frac{P(O_{0:t})}{P(O_{0:t-1})} \\ &= \frac{\sum_i^N{\alpha_t(i)}}{\sum_i^N{\alpha_{t-1}(i)}}\end{align}
  $$
  由前向概率算法，此式可算出，从而得到
  $$
  P(S_t|O_{0:t})\varpropto P(O_t|S_t,O_{0:t-1})P(S_t|O_{0:t-1})
  $$



+ 由观测独立性假设：$P(O_t|S_t,O_{0:t-1})=P(O_t|S_t)$,
  再由全概率公式：
  $$
  \begin{align} P(S_t|O_{0:t-1}) &= \sum_{s_{t-1}} {P(S_t|S_{t-1},O_{0:t-1})P(S_{t-1}|O_{0:t-1})} \\ &= \sum_{s_{t-1}} {P(S_t|S_{t-1})P(S_{t-1}|O_{0:t-1})} \end{align}
  $$
  故$P(O_t|S_t,O_{0:t-1})P(S_t|O_{0:t-1})=P(O_t|S_t)\sum_{s_{t-1}} {P(S_t|S_{t-1})P(S_{t-1}|O_{0:t-1})}$.
  
  

### 2.3

+ 分类任务是从给定的一组观察或特征中推理所属类别。
+ 朴素贝叶斯模型的假设是给定所属类别，证据变量之间条件独立，即对于所有$i\ne j$,有$(o_i\perp o_j|C)$.
+ <img src="pic\2-4-3.jpg" style="zoom:50%;" />

### 2.4

+ 令随机变量$S,F,E$分别表示睡眠充足，上课睡觉和红眼，其值域都为{0,1}，从而可以得出四个表：

  <img src="pic\2-4-4.jpg" style="zoom: 50%;" />

  对应的贝叶斯网络结构为：

  <img src="pic\2-4-1.jpg" style="zoom:50%;" />

  表已给出了先验概率分布$P(S)$，状态转移分布$P(S_t|S_{t-1})$,观察分布$P(E_t|S_t),P(F_t|S_t)$,从而可以进行滤波和预测。

+ 令$O$为观察变量，取值为${O_1,O_2,O_3,O_4}$，分别表示*上课睡觉且有红眼*、*上课睡觉且无红眼*、*上课不睡觉且有红眼*、*上课不睡觉且无红眼*。由条件独立性可由$E,F$得出观察分布，从而可得出以下几个表：

  <img src="pic\2-4-2.jpg" style="zoom: 50%;" />

  此为隐含状态$S$、观察状态$O$的隐马尔可夫模型。



### 2.5

+ $o_0=O_4,o_1=O_3,o_2=O_1$,令$S$表示$EnoughSleep$,由前向算法，可得（向量的第一项表示s=1,第二项表示s=0,以下运算均保留两位小数）：
  $$
  \begin{align}
  &b_0(s)=P(o_0|s)P(s)=(0.7\times0.72,0.3\times0.21)=(0.504,0.063)\rightarrow(0.89,0.11)\\
  &b_1(s)=(0.1341,0.12495)\rightarrow(0.52,0.48)\\
  &b_2(s)=(0.0112,0.0924)\rightarrow(0.11,0.89)
  \end{align}
  $$
  故
  $$
  \begin{align}
  &P(s_0|o_0)=(0.89,0.11)\\
  &P(s_1|o_{0:1})=(0.52,0.48)\\
  &P(s_2|o_{0:2})=(0.11,0.89)
  \end{align}
  $$
  
+ 由前向-后向算法：
  $$
  \begin{align}
  &P(s_o|o_{0:2})=P(s_0|o_0)P(o_{1:2}|s_0)=P(s_0|o_0)\sum_{s_1}P(o_1|s_1)P(s_1|s_0)\sum_{s_2}P(o_2|s_2)P(s_2|s_1)=(0.76,0.24)\\
  &P(s_1|o_{0:2})=P(s_1|o_{0:1})P(o_2|s_1)=(0.29,0.71)\\
&P(s_2|o_{0:2})=(0.11,0.89)
  \end{align}
  $$
  
+ $t=0$时的滤波概率为$(0.89,0.11)$，平滑概率为$(0.76,0.24)$,滤波下s=1的概率比平滑下的大，即$o_1,o_2$信息的加入降低了s=1的概率，而由于其都表现了有红眼故这是容易理解的：未来的观察对当前状态有影响。

  $t=1$时的滤波概率为$(0.52,0.48)$，平滑概率为$(0.29,0.71)$,滤波下s=0的概率比平滑下的小，即$o_2$信息的加入增加了s=0的概率，而由于其有红眼故这也是容易理解的。



### 2.6

+ 图的拓扑排序是一个结点的有序列表，使得如果图中有边$A\rightarrow B$，则A出现在B之前。
+ 拓扑排序使得贝叶斯网络中的采样可以从条件概率分布中采样，因为由于链式法则，在采样一个随机变量之前需要先采样其父节点。
+ 拓扑排序总是存在，但不唯一。
+ 拓扑排序：A,B,D,C,F,E。



### 2.7

+ 吉布斯采样法的缺点是，样本之间存在相关性，不容易进入到维泰分布。为了减少样本之间的相关性，可以每隔固定次数采样一次。为了采样进入到一个稳态分布的样本序列，舍弃从初始样本出发不久采样到的样本。
+ 极大似然估计的一个重大缺陷是当数据集足够小时，使得某些事件不能被观测到，则会认为其发生的概率为0。
+ 贝叶斯学习的优点有：用所有假说做预测，而不是使用单个“最好”的假说，可归约为概率推理，缺点是需要大规模求和或积分。



### 2.8

对数似然为：
$$
\begin{align}
\mathcal{l}(m,b,\sigma^2)&=ln\mathcal{N}(x_{1:n}|m,b,\sigma^2)\\
&=\sum_{j=1}^n ln(\frac{1}{\sqrt{2\pi}\sigma}exp(-\frac{(x_j-my_j-b)^2}{2\sigma^2}))\\
&=n(-ln\sqrt{2\pi}-ln\sigma)-\sum_{j=1}^{n}\frac{(x_j-my_j-b)^2}{2\sigma^2}
\end{align}
$$

对$m,b,\sigma$分别求偏导令其为0：
$$
\begin{align}
&\frac{\partial l}{\partial m}=-\sum_{j=1}^n\frac{1}{\sigma^2}(my_j+b-x_j)y_j=0\\
&\frac{\partial l}{\partial b}=-\sum_{j=1}^n\frac{1}{\sigma^2}(my_j+b-x_j)=0\\
&\frac{\partial l}{\partial \sigma}=-\frac{n}{\sigma}+\sum_{j=1}^n\frac{1}{\sigma^3}(my_j+b-x_j)^2=0
\end{align}
$$
解得：
$$
\begin{align}
&m^*=\frac{n\sum_{j=1}^nx_jy_j-\sum_{j=1}^nx_j\sum_{j=1}^ny_j }{n\sum_{j=1}^ny_j^2-(\sum_{j=1}^ny_j)^2}\\
&b^*=\frac{\sum_{j=1}^nx_j}{n}-\frac{\sum_{j=1}^ny_j(n\sum_{j=1}^nx_jy_j-\sum_{j=1}^nx_j\sum_{j=1}^ny_j)}{n(n\sum_{j=1}^ny_j^2-(\sum_{j=1}^ny_j)^2)}\\
&\sigma^*{^2}=\frac{1}{n}\sum_{j=1}^n(x_j-m^*y_j-b^*)^2
\end{align}
$$
