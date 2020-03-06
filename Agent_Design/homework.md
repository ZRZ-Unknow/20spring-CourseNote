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

+ 令随机变量$O=E\or F$，即$O$表示睡眠充足或有红眼

  可得$P(O_t^1|S_t)=\sum_{E=1\text{ or }F=1}P(E_t|S_t)P(F_t|S_t),P(O_t^0|S_t)=P(E_t^0|S_t)P(F_t^0|S_t)$, 从而得出表：

  <img src="pic\2-4-2.jpg" style="zoom: 50%;" />

  此为隐含状态$S$、观察状态$O$的隐马尔可夫模型。



### 2.5

+ $o_0=0,o_1=o_2=1$,令$S$表示$EnoughSleep$,由前向算法，可得（向量的第一项表示s=1,第二项表示s=0,以下运算均保留两位小数）：
  $$
  \begin{align}
  &b_0(s)=P(o_0|s)P(s)=(0.7\times0.72,0.3\times0.21)=(0.504,0.063)\rightarrow(0.89,0.11)\\
  &b_1(s)=(0.2086,0.20145)\rightarrow(0.51,0.49)\\
  &b_2(s)=(0.1554,0.35155)\rightarrow(0.31,0.69)
  \end{align}
  $$
  故
  $$
  \begin{align}
  &P(s_0|o_0)=(0.89,0.11)\\
  &P(s_1|o_{0:1})=(0.51,0.49)\\
  &P(s_2|o_{0:2})=(0.31,0.69)
  \end{align}
  $$
  
+ 由前向-后向算法：
  $$
  \begin{align}
  &P(s_o|o_{0:2})=P(s_0|o_0)P(o_{1:2}|s_0)=P(s_0|o_0)\sum_{s_1}P(o_1|s_1)P(s_1|s_0)\sum_{s_2}P(o_2|s_2)P(s_2|s_1)=(0.79,0.21)\\
  &P(s_1|o_{0:2})=P(s_1|o_{0:1})P(o_2|s_1)=(0.38,0.62)\\
&P(s_2|o_{0:2})=(0.31,0.69)
  \end{align}
  $$
  
+ $t=0$时的滤波概率为$(0.89,0.11)$，平滑概率为$(0.79,0.21)$,滤波下s=1的概率比平滑下的大，即$o_1,o_2$信息的加入降低了s=1的概率，而由于其都为1故这是容易理解的。

  $t=1$时的滤波概率为$(0.51,0.49)$，平滑概率为$(0.38,0.62)$,滤波下s=0的概率比平滑下的小，即$o_2$信息的加入增加了s=0的概率，而由于其为1故这也是容易理解的。

