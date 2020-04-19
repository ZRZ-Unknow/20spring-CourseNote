'''
@Descripttion: 
@version: 
@Author: Zhou Renzhe
@Date: 2020-04-19 11:31:14
@LastEditTime: 2020-04-19 21:54:20
'''
import numpy as np

class DP_on_GridWorld():
    def __init__(self,gamma,max_iter):
        self.N=10
        self.gamma=gamma
        self.max_iter=max_iter
        self.U_old=np.zeros((self.N,self.N))
        self.U_new=np.zeros((self.N,self.N))
        self.best_policy=np.array([['anydire' for i in range(self.N)] for j in range(self.N)])
        #self.policy=np.ones((10,10,4))/4    #10x10矩阵的每个元素是一个1x4小矩阵，对应于策略pi采取上下左右行动的概率
        self.inplace_U=np.zeros((self.N,self.N))
        self.T=np.array([[0.7],[0.1],[0.1],[0.1]])
        self.award_pos=[(7,8),(2,7),(4,3),(7,3)]
        self.award=[10,3,-5,-10]
        self.dire=['up','down','left','right']

    def is_against_wall(self,i,j):
        if(0<=i and i<self.N and 0<=j and j<self.N):
            return False
        return True

    def act(self,i,j,direction,U):   #在状态(i,j)处采取行动direction，得到该状态的新效用值，U为当前需要使用的效用矩阵
        U_s=0
        pos=np.array((4,2))  #pos的四个新位置分别代表朝向当前方向下的前、后、左、右，转移概率为0.7,0.1,0.1,0.1
        R=np.zeros((4,1))
        U_s_prime=np.zeros((4,1))
        if (i,j) in [(7,8),(2,7)]:      #在该位置执行任何动作都到达终止状态
            _index=self.award_pos.index((i,j))
            return self.award[_index]
        if direction=='up':
            pos=np.array([[i-1,j],[i+1,j],[i,j-1],[i,j+1]])   
        elif direction=='down':
            pos=np.array([[i+1,j],[i-1,j],[i,j+1],[i,j-1]])   
        elif direction=='left':
            pos=np.array([[i,j-1],[i,j+1],[i+1,j],[i-1,j]]) 
        elif direction=='right':
            pos=np.array([[i,j+1],[i,j-1],[i-1,j],[i+1,j]]) 
        for k in range(4):
            if self.is_against_wall(pos[k,0],pos[k,1]):
                pos[k]=[i,j]
                R[k]=[-1]
            if (i,j) in self.award_pos:
                _index=self.award_pos.index((i,j))
                R[k]=[self.award[_index]]
            U_s_prime[k]=U[pos[k,0],pos[k,1]]
        U_s=self.T.transpose().dot(R)+self.gamma*self.T.transpose().dot(U_s_prime)
        return U_s
    
    def compute_best_policy(self,U):
        for i in range(self.N):
            for j in range(self.N):
                if (i,j) in [(7,8),(2,7)]:
                    continue
                U_s_list=[]
                for k in range(4):
                    U_s_list.append(self.act(i,j,self.dire[k],U))
                self.best_policy[i,j]=self.dire[np.argmax(U_s_list)]
    
    def value_iteration(self):
        iter=0
        while iter<self.max_iter:
            for i in range(self.N):
                for j in range(self.N):
                    U_s_list=[]
                    for k in range(4):
                        U_s_list.append(self.act(i,j,self.dire[k],self.U_old))
                    self.U_new[i,j]=max(U_s_list)
            iter+=1
            delta=self.U_new-self.U_old
            if(np.linalg.norm(delta,ord=np.inf)<1e-10):
                print("iter:%d,值迭代收敛,"%iter,end='')
                break
            self.U_old=self.U_new.copy()   #深拷贝
        np.set_printoptions(precision=2,suppress=True)
        print("gamma=%f,值迭代结果:"%self.gamma)
        print(self.U_old)
        self.compute_best_policy(self.U_new)
        print("最优策略：")
        print(self.best_policy)
    
    def gauss_seidel_value_iteration(self):
        iter=0
        while iter<self.max_iter:
            U_copy=self.inplace_U.copy()  #U_copy仅仅用来保存上一轮迭代的值从而进行是否收敛的比较，在self.inplace_U上进行inplace更新
            #可以手动写出一个容易更快收敛的更新顺序，比如从非0奖赏状态开始向外扩散的更新顺序，
            # 但是我为了方便从状态矩阵的左下角到右上更新状态，因为有非0奖赏的状态集中在左下部分，这一更新顺序也要比值迭代更快一些收敛。
            for i in range(self.N-1,-1,-1):      
                for j in range(self.N-1,-1,-1):
                    U_s_list=[]
                    for k in range(4):
                        U_s_list.append(self.act(i,j,self.dire[k],self.inplace_U))
                    self.inplace_U[i,j]=max(U_s_list)
            iter+=1
            delta=self.inplace_U-U_copy
            if(np.linalg.norm(delta,ord=np.inf)<1e-10):
                print("iter:%d,高斯赛德尔值迭代收敛,"%iter,end='')
                break
        np.set_printoptions(precision=2,suppress=True)
        print("gamma=%f,高斯赛德尔值迭代结果:"%self.gamma)
        print(self.inplace_U)
        self.compute_best_policy(self.inplace_U)
        print("最优策略：")
        print(self.best_policy)
    
    def policy_evaluation(self,policy,n):
        U_prev=np.zeros((self.N,self.N))
        U_now=np.zeros((self.N,self.N))
        iter=0
        while iter<n:
            for i in range(self.N):
                for j in range(self.N):
                    U_s=np.zeros((4,1))
                    for k in range(4):
                        if(policy[i,j,k]==0):
                            U_s[k,0]=0
                        else:
                            U_s[k,0]=self.act(i,j,self.dire[k],U_prev)
                    U_now[i,j]=policy[i,j].dot(U_s)
            iter+=1
            delta=U_now-U_prev
            if(np.linalg.norm(delta,ord=np.inf)<1e-10):
                break
            U_prev=U_now.copy()
        return U_now

    def policy_iteration(self):
        iter=0
        policy_old=np.ones((self.N,self.N,4))/4
        policy_new=np.ones((self.N,self.N,4))/4
        U_pi=np.zeros((self.N,self.N))
        while(iter<self.max_iter):
            U_pi=self.policy_evaluation(policy_old,100)
            for i in range(self.N):
                for j in range(self.N):
                    U_s_list=[]
                    for k in range(4):
                        U_s_list.append(self.act(i,j,self.dire[k],U_pi))
                    max_action_index=[]
                    for k in range(4):
                        if(U_s_list[k]==max(U_s_list)):
                            max_action_index.append(k)
                    prob=1/len(max_action_index)
                    for k in range(4):
                        if k in max_action_index:
                            policy_new[i,j,k]=prob
                        else:
                            policy_new[i,j,k]=0
            iter+=1
            if(np.all(policy_new==policy_old)):
                print("iter:%d,策略迭代收敛,"%iter,end='')
                break
            policy_old=policy_new.copy()   #深拷贝
        np.set_printoptions(precision=2,suppress=True)
        print("gamma=%f,策略迭代结果:"%self.gamma)
        print(U_pi)
        best_pi=np.array([['anydire' for i in range(self.N)] for j in range(self.N)])
        for i in range(self.N):
            for j in range(self.N):
                if (i,j) in self.award_pos:
                    continue
                k=np.argmax(policy_new[i,j])
                best_pi[i,j]=self.dire[k]
        print("最优策略：")
        print(best_pi)


def main():
    dp=DP_on_GridWorld(gamma=0.5,max_iter=100)
    #dp.gauss_seidel_value_iteration()
    #dp.value_iteration()
    dp.policy_iteration()
    
if __name__=="__main__":
    main()