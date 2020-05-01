'''
@Descripttion: 
@version: 
@Author: Zhou Renzhe
@Date: 2020-04-27 20:53:45
@LastEditTime: 2020-05-01 09:59:04
'''
import numpy as np
import math

class MCTS(object):
    def __init__(self,root,max_depth,c,gamma):
        self.root=root
        self.c=c
        self.gamma=gamma
        self.max_depth=max_depth
    
    def forward_search(self):
        node=self.root
        while(len(node.children)!=0):
            node=node.select_child(self.c)
        return node   #需要被扩展的node 
    
    def expand(self,node):
        for action in node.avaliable_actions:
            env=copy.deepcopy(node.env)
            board=env.step(action)
            child=Node(env,board,node,0,0,action)
            node.children.append(child)
    
    def rollout(self,node):
        env=copy.deepcopy(node)
        done=False
        info=None
        while not done:
            action=random.randint(0,3)
            ,,done,info=env.step(action)
        ep_lenth=info.get("episode_lenth")
        score=info.get("total_score")
        succ=info.get("success")
        return score

    def backup(self,node,r):
        if node.parent==None:
            return
        node.N+=1
        node.Q+=(r-node.Q)/node.N
        return backup(node.parent,r)