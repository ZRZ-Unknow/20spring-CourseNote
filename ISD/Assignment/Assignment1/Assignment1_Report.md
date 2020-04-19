# 编程作业1

**实现值迭代算法、高斯-赛德尔值迭代算法、策略迭代算法，复现其在10x10栅格世界问题的结果**

+ **代码架构**：

  我创建了一个class:DP_on_GridWorld，初始化了转移概率T、最大迭代次数max_iter、行动方向dire、四个奖赏reward和四个奖赏位置reward_pos等。主要函数有：

  + `act(i,j,direction,U)`：表示在状态(i,j)处采取行动direction，根据公式
    $$
    R(s,a)+\gamma\sum_{s'}T(s'|s,a)U_k(s')
    $$
    返回在效用矩阵U上计算该状态的新效用值

  + `value_iteration`：值迭代算法

  + `gauss_seidel_value_iteration`：高斯-赛德尔值迭代算法

  + `policy_evaluation(policy,n)`：计算策略policy的n步期望回报

  + `policy_iteration`：策略迭代算法

  + `compute_best_policy(U,policy_matrix=None)`：根据效用矩阵U和策略矩阵policy_matrix计算最优策略

+ **算法实现**：(具体实现详见`value&policy_iteration.py`文件)

  + **值迭代**：

    ```python
    U_old=np.zeros((self.N,self.N))  #效用矩阵U_k
    U_new=np.zeros((self.N,self.N))  #效用矩阵U_{k+1}
    while iter<self.max_iter:
        for i in range(self.N):
            for j in range(self.N):
                U_s_list=[]   #表示四个动作计算得出的新效用
                for k in range(4):
                    U_s_list.append(self.act(i,j,self.dire[k],U_old))
                U_new[i,j]=max(U_s_list)  #对应伪代码中的求max操作
                iter+=1
                delta=U_new-U_old
                if(np.linalg.norm(delta,ord=np.inf)<self.epsilon):
                    print(COLOR+"iter:%d,值迭代收敛,"%iter,BACK,end='')
                    break
                U_old=U_new.copy()   
    ```

  + **高斯-赛德尔值迭代**：

    ```python
    U_inplace=np.zeros((self.N,self.N))
    while iter<self.max_iter:
        U_last_iter=U_inplace.copy() #保存上一轮迭代的结果，从而进行收敛性的判别
        #按状态矩阵的左下到右上顺序更新状态，因为有非0奖赏的状态集中在左下部分，这一更新顺序要比值迭代更快一些收敛。
        for i in range(self.N-1,-1,-1):      
            for j in range(self.N-1,-1,-1):
                U_s_list=[]
                for k in range(4):
                    #inplace更新状态
                    U_s_list.append(self.act(i,j,self.dire[k],U_inplace))
                U_inplace[i,j]=max(U_s_list)
        iter+=1
        delta=U_inplace-U_last_iter
        if(np.linalg.norm(delta,ord=np.inf)<self.epsilon):
            print(COLOR+"iter:%d,高斯赛德尔值迭代收敛,"%iter,BACK,end='')
            break
    ```

  + **策略评价**：

    与值迭代几乎相同，所不同的是没有打印信息且最后返回U_new

  + **策略迭代**：

    ```python
    #10x10矩阵的每个元素是一个1x4小矩阵，对应于策略pi采取上下左右行动的概率,初始化为1/4
    policy_old=np.ones((self.N,self.N,4))/4  #pi_k
    policy_new=np.ones((self.N,self.N,4))/4  #pi_{k+1}
    U_pi=np.zeros((self.N,self.N))
    while(iter<self.max_iter):
        U_pi=self.policy_evaluation(policy_old,self.max_iter)
        for i in range(self.N):
            for j in range(self.N):
                U_s_list=[]
                for k in range(4):
                    U_s_list.append(self.act(i,j,self.dire[k],U_pi))
                #表示新效用值中最大值的下标，对应伪代码的求argmax操作
                max_action_index=[]  
                for k in range(4):
                    if(U_s_list[k]==max(U_s_list)):
                        max_action_index.append(k)
                prob=1/len(max_action_index)
                #在pi_{k+1}中拥有最大效用值的动作平分概率，而其他动作概率为0
                for k in range(4):
                    if k in max_action_index:
                        policy_new[i,j,k]=prob
                    else:
                        policy_new[i,j,k]=0
        iter+=1
        if(np.all(policy_new==policy_old)):
            print(COLOR+"iter:%d,策略迭代收敛,"%iter,BACK,end='')
            break 
        policy_old=policy_new.copy()   
    ```

+ **实验结果**：

  + **直接运行`value&policy_iteration.py`文件即可得到运行结果**

  + $\gamma=0.5$：

    + 收敛的效用矩阵为：

      ![image-20200419232531235](pic\image-20200419232531235.png)

    + 最优策略为：

      ![image-20200419232622631](pic\image-20200419232622631.png)

  + $\gamma=0.9$：

    + 收敛的效用矩阵为：

      ![image-20200419232907227](pic\image-20200419232907227.png)

    + 最优策略为：

      ![image-20200419232954896](pic\image-20200419232954896.png)

  