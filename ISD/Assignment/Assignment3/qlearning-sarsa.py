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
        self.Q = np.random.rand(self.state_num,self.action_num)
        self.Q[-1] = [0]*self.action_num

    def train(self,iter_num):
        rewards_list = []
        for episode in range(iter_num):
            cur_state = self.env.reset()
            cur_action = -1
            if np.random.uniform(0,1) < self.epsilon:
                cur_action = self.env.action_space.sample()  
            else:
                cur_action = np.argmax(self.Q[cur_state])
            done = False
            sum_of_rewards = 0
            while not done:
                obs,reward,done,info = self.env.step(cur_action)
                sum_of_rewards += reward
                next_action = -1
                if np.random.uniform(0,1) < self.epsilon:
                    next_action = self.env.action_space.sample()  
                else:
                    next_action = np.argmax(self.Q[obs])
                self.Q[cur_state,cur_action] += self.alpha*(reward+self.gamma*self.Q[obs,next_action]-self.Q[cur_state,cur_action])
                cur_state = obs
                cur_action = next_action
                if episode>iter_num-3:
                    self.env.render()
                    time.sleep(1)
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
        self.Q = np.random.rand(self.state_num,self.action_num)
        self.Q[-1] = [0]*self.action_num

    def train(self,iter_num):
        rewards_list = []
        for episode in range(iter_num):
            cur_state = self.env.reset()
            done = False
            sum_of_rewards = 0
            while not done:
                action = -1
                if np.random.uniform(0,1) < self.epsilon:
                    action = self.env.action_space.sample()   
                else:
                    action = np.argmax(self.Q[cur_state])
                obs,reward,done,info = self.env.step(action)
                sum_of_rewards += reward
                self.Q[cur_state,action] += self.alpha*(reward+self.gamma*np.max(self.Q[obs])-self.Q[cur_state,action])
                cur_state = obs
                if episode>iter_num-3:
                    self.env.render()
                    time.sleep(1)
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

    def train(self,iter_num):
        rewards_list = []
        for episode in range(iter_num):
            state_list, action_list, reward_list = [],[],[]
            state = self.env.reset()
            action = -1
            if np.random.uniform(0,1) < self.epsilon:
                action = self.env.action_space.sample()  
            else:
                action = np.argmax(self.Q[state])
            state_list.append(state)
            action_list.append(action)
            reward_list.append(0)
            T = np.Infinity
            t = 0
            while True:
                if t<T:
                    obs,reward,done,info = self.env.step(action_list[-1])
                    state_list.append(obs)
                    reward_list.append(reward)
                    if done:
                        T = t+1
                    else:
                        if np.random.uniform(0,1) < self.epsilon:
                            action_list.append(self.env.action_space.sample())  
                        else:
                            action_list.append(np.argmax(self.Q[state_list[-1]]))
                tau = t-self.N+1
                if tau>=0:
                    G = 0
                    for i in range(tau+1,min(tau+self.N,T)+1):
                        G += self.gamma**(i-tau-1)*reward_list[i]
                    if tau+self.N<T:
                        G += self.gamma**self.N*self.Q[state_list[tau+self.N],action_list[tau+self.N]]
                    self.Q[state_list[tau],action_list[tau]] += self.alpha*(G-self.Q[state_list[tau],action_list[tau]])
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
    
    def train(self,iter_num):
        rewards_list = []
        for episode in range(iter_num):
            Z = np.zeros((self.state_num,self.action_num))
            cur_state = self.env.reset()
            cur_action = self.env.action_space.sample() 
            done = False
            sum_of_rewards = 0
            while not done:
                obs,reward,done,info = self.env.step(cur_action)
                sum_of_rewards += reward
                next_action = -1
                if np.random.uniform(0,1) < self.epsilon:
                    next_action = self.env.action_space.sample()
                else:
                    next_action = np.argmax(self.Q[obs])
                TD_error = reward + self.gamma*self.Q[obs,next_action] - self.Q[cur_state,cur_action]
                Z[cur_state,cur_action] += 1
                for state in range(self.state_num):
                    for action in range(self.action_num):
                        self.Q[state,action] += self.alpha*TD_error*Z[state,action]
                        Z[state,action] *= self.gamma*self.Lambda
                cur_state = obs
                cur_action = next_action
                if episode>iter_num-3:
                    self.env.render()
                    time.sleep(1)
            rewards_list.append(sum_of_rewards)
        self.env.close()
        return rewards_list
def main():
    iter_num = 200
    '''sarsa = Sarsa(1,0.1,0.8)
    r1 = sarsa.train(iter_num)
    qlearning = QLearning(1,0.1,0.8)
    r2 = qlearning.train(iter_num)
    #plt.ylim(-200,0)
    plt.plot(range(iter_num),r1,label='Sarsa')
    plt.plot(range(iter_num),r2,label='QLearning')
    plt.legend()
    plt.show()
    nstep_Sarsa = NStep_Sarsa(1,0.1,0.9,1)
    r3 = nstep_Sarsa.train(iter_num)
    plt.plot(range(iter_num),r3,label='NStep_Sarsa')'''

    sarsa_lambda = Sarsa_Lambda(1,0.1,0.9,1)
    r4 = sarsa_lambda.train(iter_num)
    plt.plot(range(iter_num),r4,label='Sarsa_Lambda')
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()