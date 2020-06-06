import numpy as np
import gym
import random
import matplotlib.pyplot as plt


class Sarsa():
    def __init__(self,alpha,epsilon,gamma,env='CliffWalking-v0'):
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.env = gym.make(env)
        self.action_num = self.env.action_space.n
        self.state_num = self.env.observation_space.n
        self.Q = np.zeros((self.state_num,self.action_num))

    def train(self,iter_num):
        rewards_list = []
        for episode in range(iter_num):
            cur_state = self.env.reset()
            cur_action = -1
            if np.random.uniform(0,1) < self.epsilon:
                cur_action = self.env.action_space.sample()  #random.randint(0,self.action_num-1)
            else:
                cur_action = np.argmax(self.Q[cur_state])
            done = False
            sum_of_rewards = 0
            while not done:
                obs,reward,done,info = self.env.step(cur_action)
                sum_of_rewards += reward
                next_action = -1
                if np.random.uniform(0,1) < self.epsilon:
                    next_action = self.env.action_space.sample()  #random.randint(0,self.action_num-1)
                else:
                    next_action = np.argmax(self.Q[obs])
                self.Q[cur_state,cur_action] += self.alpha*(reward+self.gamma*self.Q[obs,next_action]-self.Q[cur_state,cur_action])
                cur_state = obs
                cur_action = next_action
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

    def train(self,iter_num):
        rewards_list = []
        for episode in range(iter_num):
            cur_state = self.env.reset()
            done = False
            sum_of_rewards = 0
            while not done:
                action = -1
                if np.random.uniform(0,1) < self.epsilon:
                    action = self.env.action_space.sample()   #random.randint(0,self.action_num-1)
                else:
                    action = np.argmax(self.Q[cur_state])
                obs,reward,done,info = self.env.step(action)
                sum_of_rewards += reward
                self.Q[cur_state,action] += self.alpha*(reward+self.gamma*np.max(self.Q[obs])-self.Q[cur_state,action])
                cur_state = obs
            rewards_list.append(sum_of_rewards)
        self.env.close()
        return rewards_list

class NStep-Sarsa():
    def __init__(self,alpha,epsilon,gamma,env='CliffWalking-v0'):
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.env = gym.make(env)
        self.action_num = self.env.action_space.n
        self.state_num = self.env.observation_space.n
        self.Q = np.zeros((self.state_num,self.action_num))

    def train(self,iter_num):
        rewards_list = []


def main():
    iter_num = 100
    sarsa = Sarsa(1,0.1,0.8)
    r1 = sarsa.train(iter_num)
    qlearning = QLearning(1,0.1,0.8)
    r2 = qlearning.train(iter_num)
    plt.ylim(-200,0)
    plt.plot(range(iter_num),r1,label='Sarsa')
    plt.plot(range(iter_num),r2,label='QLearning')
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()