'''
@Descripttion: 
@version: 
@Author: Zhou Renzhe
@Date: 2020-05-21 23:23:24
@LastEditTime: 2020-05-22 09:28:55
'''
import numpy as np
import gym

class QLearning():
    def __init__(self):
        pass

def main():
    np.set_printoptions(precision=2,suppress=True)
    env=gym.make("CliffWalking-v0")
    env.reset()
    for i in range(100):
        env.render()
        action=np.random.randint(env.action_space.n)
        obs,reward,done,info=env.step(action)
        print(obs,reward,done,info)

    env.close()

if __name__=="__main__":
    main()