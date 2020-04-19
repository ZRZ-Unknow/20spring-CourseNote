'''
@Descripttion: 
@version: 
@Author: Zhou Renzhe
@Date: 2020-04-18 17:06:34
@LastEditTime: 2020-04-19 11:29:27
'''

import numpy as np
N=10
gamma=0.5
U_old=np.zeros((N,N))
U_new=np.zeros((N,N))
T=np.array([[0.7],[0.1],[0.1],[0.1]])
award_pos=[(7,8),(2,7),(4,3),(7,3)]
award=[10,3,-5,-10]
dire=['up','down','left','right']
max_iter=100


def is_against_wall(i,j):
    if(0<=i and i<N and 0<=j and j<N):
        return False
    return True

def act(i,j,direction):   #在状态(i,j)处采取行动direction，得到该状态的新效用值
    U_s=0
    pos=np.array((4,2))  #pos的四个新位置分别代表朝向当前方向下的前、后、左、右，转移概率为0.7,0.1,0.1,0.1
    R=np.zeros((4,1))
    U_s_prime=np.zeros((4,1))
    if (i,j) in [(7,8),(2,7)]:      #在该位置执行任何动作都到达终止状态
        _index=award_pos.index((i,j))
        return award[_index]
    if direction=='up':
        pos=np.array([[i-1,j],[i+1,j],[i,j-1],[i,j+1]])   
    elif direction=='down':
        pos=np.array([[i+1,j],[i-1,j],[i,j+1],[i,j-1]])   
    elif direction=='left':
        pos=np.array([[i,j-1],[i,j+1],[i+1,j],[i-1,j]]) 
    elif direction=='right':
        pos=np.array([[i,j+1],[i,j-1],[i-1,j],[i+1,j]]) 
    for k in range(4):
        if is_against_wall(pos[k,0],pos[k,1]):
            pos[k]=[i,j]
            R[k]=[-1]
        if (i,j) in award_pos:
            _index=award_pos.index((i,j))
            R[k]=[award[_index]]
        U_s_prime[k]=U_old[pos[k,0],pos[k,1]]
    U_s=T.transpose().dot(R)+gamma*T.transpose().dot(U_s_prime)
    return U_s

def value_iteration():
    iter=0
    while iter<max_iter:
        for i in range(N):
            for j in range(N):
                U_s_list=[]
                for k in range(4):
                    U_s_list.append(act(i,j,dire[k]))
                U_new[i,j]=max(U_s_list)
        iter+=1
        delta=U_old-U_new
        delta=np.dot(delta,delta)
        if(np.trace(delta)<1e-10):
            print("iter:%d,值迭代收敛"%iter)
            break
        U_old=U_new.copy()   #深拷贝
    np.set_printoptions(precision=2,suppress=True)
    print("gamma=%f,值迭代结果:"%gamma)
    print(U_old)
