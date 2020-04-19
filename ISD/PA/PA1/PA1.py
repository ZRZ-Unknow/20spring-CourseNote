'''
@Descripttion: 
@version: 
@Author: Zhou Renzhe
@Date: 2020-04-19 11:31:14
@LastEditTime: 2020-04-19 11:42:46
'''
import numpy as np

class DP_on_GridWorld():
    def __init__(self,gamma,max_iter):
        self.N=10
        self.gamma=gamma
        self.max_iter=max_iter
        self.U_old=np.zeros((self.N,self.N))
        self.U_new=np.zeros((self.N,self.N))
        self.T=np.array([[0.7],[0.1],[0.1],[0.1]])
        self.award_pos=[(7,8),(2,7),(4,3),(7,3)]
        self.award=[10,3,-5,-10]
        self.dire=['up','down','left','right']

    def is_against_wall(self,i,j):
        if(0<=i and i<self.N and 0<=j and j<self.N):
            return False
        return True

    def act(self,i,j,direction):   #在状态(i,j)处采取行动direction，得到该状态的新效用值
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
            U_s_prime[k]=self.U_old[pos[k,0],pos[k,1]]
        U_s=self.T.transpose().dot(R)+self.gamma*self.T.transpose().dot(U_s_prime)
        return U_s

    def value_iteration(self):
        iter=0
        while iter<self.max_iter:
            for i in range(self.N):
                for j in range(self.N):
                    U_s_list=[]
                    for k in range(4):
                        U_s_list.append(self.act(i,j,self.dire[k]))
                    self.U_new[i,j]=max(U_s_list)
            iter+=1
            delta=self.U_old-self.U_new
            delta=np.dot(delta,delta)
            if(np.trace(delta)<1e-10):
                print("iter:%d,值迭代收敛,"%iter,end='')
                break
            self.U_old=self.U_new.copy()   #深拷贝
        np.set_printoptions(precision=2,suppress=True)
        print("gamma=%f,值迭代结果:"%self.gamma)
        print(self.U_old)

def main():
    dp=DP_on_GridWorld(gamma=0.5,max_iter=100)
    dp.value_iteration()

if __name__=="__main__":
    main()