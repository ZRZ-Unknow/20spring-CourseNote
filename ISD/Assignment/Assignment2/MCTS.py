'''
@Descripttion: 
@version: 
@Author: Zhou Renzhe
@Date: 2020-04-27 20:53:45
@LastEditTime: 2020-05-19 13:35:11
'''
import numpy as np
import math
import random
import copy
import time
import sys

class Node(object):
    def __init__(self,parent,last_action,avaliable_actions=[0,1,2,3],Q=0,N=0):
        self.parent=parent
        self.Q=Q
        self.N=N
        self.last_action=last_action
        self.avaliable_actions=avaliable_actions    
        self.children=[]
    
    def set_avaliable_actions(self,env):
        act_list=[]
        for action in range(4):
            tmp=copy.deepcopy(env)
            state_before=copy.deepcopy(tmp.state)
            tmp.step(action)
            if state_before==tmp.state:
                continue
            act_list.append(action)
        self.avaliable_actions=act_list
    
    def is_fully_expanded(self):
        return len(self.avaliable_actions)==len(self.children)
    
    def select_child(self,c):
        ucts=[]
        for node in self.children:
            ucts.append(node.calc_uct(c))
        index=np.argmax(np.array(ucts))
        return self.children[index]
    
    def calc_uct(self,c):
        return self.Q/self.N + c * math.sqrt(2*math.log(self.parent.N)/(self.N))

    def get_unused_action(self):
        tmp=copy.deepcopy(self.avaliable_actions)
        for node in self.children:
            tmp.remove(node.last_action)
        return random.choice(tmp)

    def select_best_action(self):
        scores=[]
        for node in self.children:
            scores.append(node.calc_uct(0))
        index=np.argmax(np.array(scores))
        return self.children[index].last_action

class MCTS(object):
    def __init__(self,root,env,max_iter):
        self.env=copy.deepcopy(env)
        self.simulate_env=None
        self.root=root
        self.max_iter=max_iter
    
    def forward_search(self):
        self.simulate_env=copy.deepcopy(self.env)
        node=self.root
        while(node.is_fully_expanded()):
            node=node.select_child(node.Q/node.N)
            self.simulate_env.step(node.last_action)
        return node
    
    def expand(self,node):
        action=node.get_unused_action()
        newNode=Node(node,action)
        node.children.append(newNode)
        node=newNode
        self.simulate_env.step(action)
        return node

    def rollout(self):
        score_before=self.env.score
        done=False
        while not done:
            action=random.randint(0,3)
            obs,res,done,info=self.simulate_env.step(action)
        score_after=self.simulate_env.score
        return score_after-score_before
    
    def backup(self,node,R):
        while node != None:
            node.N+=1
            node.Q+=R
            node=node.parent

    def train(self,time_limit):
        t1=time.time()
        t2=time.time()
        for i in range(self.max_iter):
            node=self.forward_search()
            node=self.expand(node)
            R=self.rollout()
            self.backup(node,R)
            t2=time.time()
            if (t2-t1)>=time_limit:
                break
        if (t2-t1)<time_limit:
            time.sleep(time_limit-t2+t1)
        best_action=self.root.select_best_action()
        return best_action

class Logger(object):
    def __init__(self, filename, stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a+')
 
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)