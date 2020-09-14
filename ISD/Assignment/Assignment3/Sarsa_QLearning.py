import numpy as np
import gym
import random
import matplotlib.pyplot as plt
import time

class Sarsa():
    def __init__(self,alpha,epsilon,gamma,env='CliffWalking-v0'):
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.env = gym.make(env)
        self.action_num = self.env.action_space.n
        self.state_num = self.env.observation_space.n
        self.Q = np.zeros((self.state_num,self.action_num)) 
    
    def policy(self,state):
        if np.random.uniform(0,1) < self.epsilon:
            return self.env.action_space.sample()  
        else:
            return np.argmax(self.Q[state])

    def train(self,iter_num):
        rewards_list = []
        for episode in range(iter_num):
            cur_state = self.env.reset()
            cur_action = self.policy(cur_state)
            done = False
            sum_of_rewards = 0
            while not done:
                obs,reward,done,info = self.env.step(cur_action)
                sum_of_rewards += reward
                next_action = self.policy(obs)
                self.Q[cur_state,cur_action] += self.alpha*(reward+self.gamma*self.Q[obs,next_action]-self.Q[cur_state,cur_action])
                cur_state, cur_action = obs, next_action
            rewards_list.append(sum_of_rewards)
        self.env.close()
        return rewards_list

class QLearning():
    def __init__(self,alpha,epsilon,gamma,env='CliffWalking-v0'):
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.env = gym.make(env)
        self.action_num = self.env.action_space.n
        self.state_num = self.env.observation_space.n
        self.Q = np.zeros((self.state_num,self.action_num)) 
    
    def policy(self,state):
        if np.random.uniform(0,1) < self.epsilon:
            return self.env.action_space.sample()  
        else:
            return np.argmax(self.Q[state])

    def train(self,iter_num):
        rewards_list = []
        for episode in range(iter_num):
            state = self.env.reset()
            done = False
            sum_of_rewards = 0
            while not done:
                action = self.policy(state)
                obs,reward,done,info = self.env.step(action)
                sum_of_rewards += reward
                self.Q[state,action] += self.alpha*(reward+self.gamma*np.max(self.Q[obs])-self.Q[state,action])
                state = obs
            rewards_list.append(sum_of_rewards)
        self.env.close()
        return rewards_list

class NStep_Sarsa():
    def __init__(self,alpha,epsilon,gamma,N,env='CliffWalking-v0'):
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.N = N
        self.env = gym.make(env)
        self.action_num = self.env.action_space.n
        self.state_num = self.env.observation_space.n
        self.Q = np.zeros((self.state_num,self.action_num))
    
    def policy(self,state):
        if np.random.uniform(0,1) < self.epsilon:
            return self.env.action_space.sample()  
        else:
            return np.argmax(self.Q[state])
    
    def train(self,iter_num):
        rewards_list = []
        for episode in range(iter_num):
            state_list, action_list, reward_list = [],[],[0]
            state = self.env.reset()
            action = self.policy(state)
            state_list.append(state)
            action_list.append(action)
            T = np.Infinity
            t = 0
            while True:
                if t < T:
                    obs,reward,done,info = self.env.step(action_list[-1])
                    state_list.append(obs)
                    reward_list.append(reward)
                    if done:
                        T = t+1
                    else:
                        action_list.append(self.policy(state_list[-1]))
                tau = t-self.N+1
                if tau >= 0:
                    G = 0
                    for i in range(tau+1,min(tau+self.N,T)+1):
                        G += self.gamma**(i-tau-1)*reward_list[i]
                    if tau+self.N < T:
                        s, a = state_list[tau+self.N], action_list[tau+self.N]
                        G += self.gamma**self.N*self.Q[s,a]
                    s, a = state_list[tau], action_list[tau]
                    self.Q[s,a] += self.alpha*(G-self.Q[s,a])
                if tau==T-1:
                    break
                t += 1
            rewards_list.append(sum(reward_list))
        self.env.close()
        return rewards_list

class Sarsa_Lambda():
    def __init__(self,alpha,epsilon,gamma,Lambda,env='CliffWalking-v0'):
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.Lambda = Lambda
        self.env = gym.make(env)
        self.action_num = self.env.action_space.n
        self.state_num = self.env.observation_space.n
        self.Q = np.zeros((self.state_num,self.action_num))
    
    def policy(self,state):
        if np.random.uniform(0,1) < self.epsilon:
            return self.env.action_space.sample()  
        else:
            return np.argmax(self.Q[state])
    
    def train(self,iter_num):
        rewards_list = []
        for episode in range(iter_num):
            Z = np.zeros((self.state_num,self.action_num))
            cur_state, cur_action = self.env.reset(), self.env.action_space.sample() 
            done = False
            sum_of_rewards = 0
            while not done:
                obs,reward,done,info = self.env.step(cur_action)
                sum_of_rewards += reward
                next_action = self.policy(obs)
                TD_error = reward + self.gamma*self.Q[obs,next_action] - self.Q[cur_state,cur_action]
                Z[cur_state,cur_action] += 1
                for s in range(self.state_num):
                    for a in range(self.action_num):
                        self.Q[s,a] += self.alpha*TD_error*Z[s,a]
                        Z[s,a] *= self.gamma*self.Lambda
                cur_state, cur_action = obs, next_action
            rewards_list.append(sum_of_rewards)
        self.env.close()
        return rewards_list

def res_process(rewards_list):
    N = len(rewards_list)
    res = []
    n = 10
    for i in range(0,N-n):
        res.append(sum(rewards_list[i:i+n])/n)
    return res

def test1():
    iter_num = 200
    sarsa = Sarsa(0.9,0.1,0.8)
    r1 = sarsa.train(iter_num)
    r1 = res_process(r1)
    qlearning = QLearning(0.9,0.1,0.8)
    r2 = qlearning.train(iter_num)
    r2 = res_process(r2)
    plt.plot(range(len(r1)),r1,label='Sarsa')
    plt.plot(range(len(r2)),r2,label='QLearning')
    plt.ylim(-300,0)
    plt.legend()
    plt.show()

def test2():
    iter_num = 200
    for n,Lambda in [(1,0),(3,0.5),(5,1)]:
        nstep_Sarsa = NStep_Sarsa(1,0.1,0.9,n)
        r1 = nstep_Sarsa.train(iter_num)
        r1 = res_process(r1)
        plt.plot(range(len(r1)),r1,label='NStep_Sarsa '+str(n))
        sarsa_lambda = Sarsa_Lambda(1,0.1,0.9,Lambda)
        r2 = sarsa_lambda.train(iter_num)
        r2 = res_process(r2)
        plt.plot(range(len(r2)),r2,label='Sarsa_Lambda '+str(Lambda))
        plt.legend()
        plt.show()

if __name__=="__main__":
    test1()
    test2()