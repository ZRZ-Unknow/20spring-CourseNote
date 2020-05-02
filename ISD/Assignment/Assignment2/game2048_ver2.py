import copy
import math
import random
import sys
import time
import warnings
import math
import gym  
import numpy as np
from PyQt5.QtWidgets import (QMainWindow,QWidget,QPushButton,QDialog,
    QApplication,QDesktopWidget,QLabel,QMessageBox)
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt


class Game2048Env(gym.Env):
    # render: whether to display gui
    def __init__(self, render:bool=True):
        super(Game2048Env, self).__init__()
        self.action_space = gym.spaces.Discrete(4)
        self.observation_space = gym.spaces.Box(low=0, high=2048, shape=(4,4))
        self.render = render
        self.done = False
        self.state = [[0, 0, 0, 0] for i in range(4)]
        self.score_dict = {}
        for num in range(1, 12):
            self.score_dict[2 ** num] = 2 ** (num - 1)
        self.episode_length = 0
        self.info = {}
        self.port = None
        if self.render:
            self._run()
            msg = self.port.recv()
            assert msg == 'init_ok'
    def reset(self):
        self.state = [[0, 0, 0, 0] for i in range(4)]
        self._generateNew(2)
        self.done = False
        self.info = {}
        self.score = 0
        self.episode_length = 0
    
    # returns obs, rew, done, info
    def step(self, action: int):
        assert self.action_space.contains(action), 'Illegal Action!'
        prev_score = self.score

        def _moveLeft():
            self.prev_board=copy.deepcopy(self.state)
            self.episode_length += 1
            for i in range(4):
                tmp = []
                for j in range(4):
                    if self.state[i][j] != 0:
                        tmp.append(self.state[i][j])
                for k in range(len(tmp) - 1):
                    if tmp[k] != 0 and tmp[k] == tmp[k + 1]:
                        tmp[k] *= 2
                        self.score += self.score_dict[tmp[k]]
                        tmp = tmp[:k + 1] + tmp[k + 2:] + [0]
                tmp += [0] * (4 - len(tmp))
                self.state[i] = tmp
            self._checkBoard()
        def _moveRight():
            self.prev_board=copy.deepcopy(self.state)
            self.episode_length += 1
            for i in range(4):
                tmp = []
                for j in range(4):
                    if self.state[i][j] != 0:
                        tmp.append(self.state[i][j])
                for k in range(len(tmp) - 1, 0, -1):
                    if tmp[k] != 0 and tmp[k] == tmp[k - 1]:
                        tmp[k] *= 2
                        self.score += self.score_dict[tmp[k]]
                        tmp = [0] + tmp[:k - 1] + tmp[k:]
                tmp = [0] * (4 - len(tmp)) + tmp
                self.state[i] = tmp
            self._checkBoard()
        def _moveUp():
            self.prev_board = copy.deepcopy(self.state)
            self.episode_length += 1
            for j in range(4):
                tmp = []
                for i in range(4):
                    if self.state[i][j] != 0:
                        tmp.append(self.state[i][j])
                for k in range(len(tmp) - 1):
                    if tmp[k] != 0 and tmp[k] == tmp[k + 1]:
                        tmp[k] *= 2
                        self.score += self.score_dict[tmp[k]]
                        tmp = tmp[:k + 1] + tmp[k + 2:] + [0]
                tmp += [0] * (4 - len(tmp))
                for i in range(4):
                    self.state[i][j] = tmp[i]
        def _moveDown():
            self.prev_board = copy.deepcopy(self.state)
            self.episode_length += 1
            for j in range(4):
                tmp = []
                for i in range(4):
                    if self.state[i][j] != 0:
                        tmp.append(self.state[i][j])
                for k in range(len(tmp) - 1, 0, -1):
                    if tmp[k] != 0 and tmp[k] == tmp[k - 1]:
                        tmp[k] *= 2
                        self.score += self.score_dict[tmp[k]]
                        tmp = [0] + tmp[:k - 1] + tmp[k:]
                tmp = [0] * (4 - len(tmp)) + tmp
                for i in range(4):
                    self.state[i][j] = tmp[i]
        
        if action == 0:
            _moveUp()
        elif action == 1:
            _moveDown()
        elif action == 2:
            _moveLeft()
        elif action == 3:
            _moveRight()
        self._checkBoard()
        if self.render:
            self.port.send(("step",(self.score, self.state)))
            msg = self.port.recv()
            assert msg == 'step_ok'
        return self.state, self.score - prev_score, self.done, self.info
   
    def close(self):
        if self.port is not None:
            self.port.send(("close", None))
            self.port.close()
            self.gui_process.terminate()
            self.gui_process.join()

    def seed(self, seed):
        random.seed(seed)

    # you can modify the following two functions if you really need them, but they are neither tested nor recommended
    # UNTESTED
    def setRender(self, render:bool):
        warnings.warn("Not recommended API", UserWarning)
        if self.render and not render:
            self.close()
            self.port = None
            self.gui_process = None
        if not self.render and render:
            self._run()
            msg = self.port.recv()
            assert msg == 'init_ok'
        self.render = render
    
    
    # UNTESTED
    def set(self, state, score=0):
        warnings.warn("Not recommended API", UserWarning)
        self.state = copy.deepcopy(state)
        self.score = score
        if self.render:
            self.port.send(("set",(self.state,self.score)))
            msg = self.port.recv()
            assert msg == 'set_ok'
    
    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k != 'gui_process' and k != 'port':
                setattr(result, k, copy.deepcopy(v, memo))
        result.render = False
        return result

    def _run(self):
        from multiprocessing import Process, Pipe
        port, remote_port = Pipe(duplex=True)
        self.port = port
        self.gui_process = Process(target=self._initGUI, args=(remote_port, port, ))
        self.gui_process.start()
        remote_port.close()

    def _initGUI(self, port, remote_port):
        app=QApplication(sys.argv)
        qt_game=Game2048GUI(port, remote_port)
        sys.exit(app.exec_())
    
    def wrapper_action(self):
        act_list=self.avaliable_action(self.state)
        return act_list

    def avaliable_action(self,board):
        act_list=[]
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    act_list=[0,1,2,3]
                    return act_list
        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == board[i - 1][j] or board[i][j] == board[i + 1][j]:
                    act_list.append(0)
                    act_list.append(1)
                if board[i][j] == board[i][j - 1] or board[i][j] == board[i][j + 1]:
                    act_list.append(2)
                    act_list.append(3)
                if set(act_list)=={0,1,2,3}:
                    return list(set(act_list))
        if board[0][0] == board[0][1] or board[3][0] == board[3][1] or  board[0][3] == board[0][2] or board[3][3] == board[3][2] or \
                board[0][1] == board[0][2] or board[3][1] == board[3][2]:
            act_list.append(2)
            act_list.append(3)
        if set(act_list)=={0,1,2,3}:
            return list(set(act_list))
        if board[0][0] == board[1][0] or board[3][0] == board[2][0] or board[0][3] == board[1][3] or board[3][3] == board[2][3] or \
                board[1][0] == board[2][0] or board[1][3]==board[2][3]:
            act_list.append(0)
            act_list.append(1)
        return list(set(act_list))


    def _checkBoard(self):
        self.before_gen_state=copy.deepcopy(self.state)
        for i in range(4):
            for j in range(4):
                if self.state[i][j] == 2048:
                    self.done = True
                    self.info['episode_length'] = self.episode_length
                    self.info['success'] = True
                    self.info['total_score'] = self.score
        if self.prev_board != self.state and self._getAvailablePos(self.state):
            self._generateNew(1)
        elif not self._getAvailablePos(self.state):  
            def _canMove(board):
                for i in range(1, len(board) - 1):
                    for j in range(1, len(board[0]) - 1):
                        if board[i][j] == board[i - 1][j] or board[i][j] == board[i + 1][j] or board[i][j] == board[i][j - 1] or \
                                board[i][j] == board[i][j + 1]:
                            return True
                if board[0][0] == board[0][1] or board[0][0] == board[1][0]:
                    return True
                if board[3][0] == board[3][1] or board[3][0] == board[2][0]:
                    return True
                if board[0][3] == board[1][3] or board[0][3] == board[0][2]:
                    return True
                if board[3][3] == board[3][2] or board[3][3] == board[2][3]:
                    return True
                if board[1][0] == board[2][0] or board[0][1] == board[0][2] or board[3][1] == board[3][2] or board[1][3] == \
                        board[2][3]:
                    return True
                return False
            if not _canMove(self.state):
                self.done = True
                self.info['episode_length'] = self.episode_length
                self.info['total_score'] = self.score
                if self.info.get('success') is None:
                    self.info['success'] = False
                

    def _generateNew(self, num):
        sample = random.sample(self._getAvailablePos(self.state), num)
        for i in range(num):
            x, y = sample[i]
            self.state[x][y] = 2

    def _getAvailablePos(self, arr):
        res = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0:
                    res.append([i, j])
        return res
    
    def evaluate_state(self):
        count=0
        for i in range(4):
            for j in range(4):
                if self.state[i][j]==0:
                    count+=1
        return count

class Game2048GUI(QMainWindow):
    def __init__(self, port, remote_port):
        super(Game2048GUI, self).__init__()
        self.port = port
        remote_port.close()
        self._initUI()
        if self.port is not None:
            self._mainLoop()

    def _initUI(self):
        self.color_dict={}
        self.score = 0
        self.state = [[0, 0, 0, 0] for i in range(4)]

        # you can change to whatever you like :)
        self.color_dict[0]='white'
        col = ['lightgrey','grey', 'pink', 'yellow', 'brown', 'red', 'violet', 'crimson', 'fuchsia','orange','green']
        for num in range(1, 12):
            self.color_dict[2 ** num] = col[num - 1]

        self.state_font = QFont('Consolas', 20)
        self.scoreboard_font = QFont('Consolas', 16)
        self.button_font = QFont('Consolas', 12)

        self.setGeometry(300, 300, 500, 550)
        self.setWindowTitle("2048 : played by ZRZ using MCTS")
        self.center()

        self.scoreboard=QLabel(self)
        self.scoreboard.resize(150, 80)
        self.scoreboard.move(30, 0)
        self.scoreboard.setFont(self.scoreboard_font)
        self.scoreboard.setText('Score:{}'.format(self.score))
        # restart_button = QPushButton('Restart', self)
        # restart_button.setFont(self.button_font)
        # restart_button.resize(80, 30)
        # restart_button.move(380, 25)
        # restart_button.clicked.connect(self._restart)
        # restart_button.setFocusPolicy(Qt.NoFocus)

        self._initBoardUI()
        self._updateBoardUI()
        self.show()

    def _mainLoop(self):
        self.port.send('init_ok')
        while True:
            QApplication.processEvents()
            cmd, data = self.port.recv()
            if cmd == "step":
                self.score, self.state = data
                self._updateBoardUI()
                self.port.send("step_ok")
            if cmd == "set":
                self.score, self.state = data
                self._updateBoardUI()
                self.port.send("set_ok")
            if cmd == "close":
                self.port.close()
                self.exit(0)

    def _initBoardUI(self):
        self.scoreboard.setText('Score:{}'.format(self.score))
        self.state_labels = [[0, 0, 0, 0] for i in range(4)]
        for i in range(4):
            for j in range(4):
                self.state_labels[i][j] = QLabel(self)
                self.state_labels[i][j].setFont(self.state_font)
                self.state_labels[i][j].setAlignment(Qt.AlignCenter)
                self.state_labels[i][j].resize(100, 100)
                self.state_labels[i][j].move(110 * j + 30, 110 *i+70)

    def _updateBoardUI(self):
        win=False
        for i in range(4):
            for j in range(4):
                col=self.color_dict[self.state[i][j]]
                if self.state[i][j] == 0:
                    txt=''
                else:
                    txt=str(self.state[i][j])
                self.state_labels[i][j].setText(txt)
                self.state_labels[i][j].setStyleSheet('background-color:%s'%col)
                if self.state[i][i]==2048:
                    win=True
        if win==False:
            self.scoreboard.setText('Score:{}'.format(self.score))
        else:
            self.scoreboard.setText('You Win!')
    
    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self,event):
        QMessageBox.information(self, "Hint", "Please close the window from the console")
        event.ignore()


class Node(object):
    def __init__(self,state,parent,last_action,avaliable_actions,Q=0,N=0):
        
        self.state=state
        self.parent=parent
        self.Q=Q
        self.N=N
        self.last_action=last_action
        self.avaliable_actions=avaliable_actions    #[i for i in range(4)]   #avaliable_actions
        self.children=[]

    def select_child(self,c):  
        return self.children[random.randint(0,len(self.children)-1)]
    
    def score(self):
        if self.N==0:
            return 0
        else:
            return self.Q/self.N
    def hasUnexamedAction(self):
        tmp=copy.deepcopy(self.avaliable_actions)
        for i in range(len(self.children)):
            node=self.children[i]
            tmp.remove(node.last_action)
        if len(tmp)>0:
            return True
        else:
            return False

    def getUnexamedAction(self):
        tmp=copy.deepcopy(self.avaliable_actions)
        for i in range(len(self.children)):
            node=self.children[i]
            tmp.remove(node.last_action)
        return random.choice(tmp)

    def select_best_action(self):
        scores=[]
        for node in self.children:
            scores.append(node.score())
        index=np.argmax(np.array(scores))
        return self.children[index].last_action

class MCTS(object):
    def __init__(self,root,env,max_depth,c,gamma,max_iter):
        self.env=copy.deepcopy(env)
        self.simulate_env=None
        self.root=root
        self.c=c
        self.gamma=gamma
        self.max_depth=max_depth
        self.max_iter=max_iter
    
    def forward_search(self):
        self.simulate_env=copy.deepcopy(self.env)
        node=self.root
        while(len(node.children)!=0 and not node.hasUnexamedAction()):
            node=node.select_child(self.c)
            self.simulate_env.step(node.last_action)
        return node
    
    def expand(self,node):
        if node.hasUnexamedAction():
            action=node.getUnexamedAction()
            self.simulate_env.step(action)
            newNode=Node(None,node,action,[i for i in range(4)])
            node.children.append(newNode)
            node=node.children[-1]
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
        if node.parent==None:
            return
        node.N+=1
        node.Q+=R
        self.backup(node.parent,R)

    def train(self):
        t1=time.time()
        for i in range(self.max_iter):
            node=self.forward_search()
            node=self.expand(node)
            R=self.rollout()
            self.backup(node,R)
            t2=time.time()
            if self.env.score>7300:
                continue
            if (t2-t1)>0.5:
                break
        best_action=self.root.select_best_action()
        return best_action

def train_():
    depth=[5,10,20,30]
    c=[0.5,1,10,100]
    max_iter=[50,100,200,300,400]
    for i in range(len(depth)):
        for j in range(len(c)):
            for k in range(len(max_iter)):
                env = Game2048Env(True) 
                env.seed(0)
                env.reset()
                done = False
                obs=None
                rew=0
                info=None
                state=copy.deepcopy(env.state)
                print("=====================training===========================")
                while not done:
                    node=Node(copy.deepcopy(env),state,None,0,0,None,None)
                    agent=MCTS(node,depth[i],0.3,c[j],max_iter[k])         
                    action=agent.train()
                    obs, rew, done, info = env.step(action)
                    state=copy.deepcopy(obs)
                print(depth[i],c[j],max_iter[k])
                print(obs,rew, done, info)
                print("==================end training==========================")
                env.close()

if __name__ == '__main__':
    env = Game2048Env(True) 
    # you can fix the seed for debugging, but your agent SHOULD NOT overfit to the env of a certain seed
    env.seed(0)
    # render is automatically set to False for copied envs
    # remember to call reset() before calling step()
    env.reset()
    done = False
    state=copy.deepcopy(env.state)
    while not done:
        # A random agent as example
        # 0, 1, 2, 3 mean up, down, left, right respectively
        #action = random.randint(0, 3)
        node=Node(state,None,None,[i for i in range(4)])
        agent=MCTS(node,env,50,0.3,1,400)         
        action=agent.train()
        obs, rew, done, info = env.step(action)
        state=copy.deepcopy(obs)
        print(obs,rew, done, info)
    # remember to close the env, but you can always let resources leak on your own computer :|
    time.sleep(20)
    env.close()
    #train_()
