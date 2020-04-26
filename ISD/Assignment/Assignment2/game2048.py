import copy
import math
import random
import sys
import time

import gym  
import numpy as np
from PyQt5.QtWidgets import (QMainWindow,QWidget,QPushButton,QDialog,
    QApplication,QDesktopWidget,QLabel,QMessageBox)
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt


class Game2048Env(gym.Env):
    # render: whether to display gui
    # keyboard_control: whether to activate hotkeys
    # play: if you want to play 2048 yourself :)
    def __init__(self, render:bool = True, keyboard_control:bool=False, play : bool=False):
        self.action_space = gym.spaces.Discrete(4)
        self.render = render
        self.keyboard_control = keyboard_control
        if play:
            app=QApplication(sys.argv)
            qt_game=Game2048GUI(None, self.render, self.keyboard_control)
            app.exec_() 
        else:
            self.run()

    def run(self):
        from multiprocessing import Process, Pipe
        port, remote_port = Pipe(duplex=True)
        self.port = port
        self.p = Process(target=self.initQt, args=(remote_port, ))
        self.p.start()
        remote_port.close()

    def initQt(self, port):
        app=QApplication(sys.argv)
        qt_game=Game2048GUI(port, self.render, self.keyboard_control)
        app.exec_()

    def reset(self):
        self.port.send(4)
        return self.port.recv()

    # returns obs, rew, done, info
    def step(self, action: int):
        assert self.action_space.contains(action)
        self.port.send(action)
        return self.port.recv()
    
    def close(self):
        self.port.send(10)
        self.port.close()
        self.p.join()

    def seed(self, seed):
        random.seed(seed)


class Game2048GUI(QDialog):
    def __init__(self, port, render=True, keyboard_control=True,):
        super().__init__()
        self.render = render
        self.port = port
        self.keyboard_control = keyboard_control
        self.show_animation = True
        self.score = 0
        self.episode_length = 0
        self.done = False
        self.info = {}
        self.board = [[0, 0, 0, 0] for i in range(4)]
        self._generateNew(2)
        if self.render:
            self._initUI()
        if self.port is not None:
            self._mainLoop()

    def _initUI(self):
        self.color_dict={}
        self.score_dict={}
        # you can change to whatever you like :)
        self.color_dict[0]='white'
        col = ['lightgrey','grey', 'pink', 'yellow', 'brown', 'red', 'violet', 'crimson', 'fuchsia'] * 100
        for num in range(1, 100):
            self.color_dict[2 ** num] = col[num - 1]
            self.score_dict[2 ** num] = 2 ** (num - 1)

        self.board_font = QFont('Consolas', 20)
        self.scoreboard_font = QFont('Consolas', 16)
        self.button_font = QFont('Consolas', 12)

        self.setGeometry(300, 300, 500, 550)
        self.setWindowTitle("2048")
        self.center()

        self.scoreboard=QLabel(self)
        self.scoreboard.resize(150, 80)
        self.scoreboard.move(30, 0)
        self.scoreboard.setFont(self.scoreboard_font)
        self.scoreboard.setText('Score : {}'.format(self.score))


        restart_button = QPushButton('Restart', self)
        restart_button.setFont(self.button_font)
        restart_button.resize(80, 30)
        restart_button.move(380, 25)
        restart_button.clicked.connect(self._restart)
        restart_button.setFocusPolicy(Qt.NoFocus)

        self._initBoardUI()
        self._updateBoardUI()
        self.show()

    def _mainLoop(self):
        while True:
            QApplication.processEvents()
            cmd = self.port.recv()
            if cmd == 0:
                prev_score = self.score
                self._moveUp()
                self.port.send((self.board, self.score - prev_score, self.done, self.info))
            if cmd == 1:
                prev_score = self.score
                self._moveDown()
                self.port.send((self.board, self.score - prev_score, self.done, self.info))
            if cmd == 2:
                prev_score = self.score
                self._moveLeft()
                self.port.send((self.board, self.score - prev_score, self.done, self.info))
            if cmd == 3:
                prev_score = self.score
                self._moveRight()
                self.port.send((self.board, self.score - prev_score, self.done, self.info))
            if cmd == 4:
                self._restart()
                self.port.send((self.board))
            if cmd == 10:
                self.port.close()
                exit(0)

    def _setBoard(self, board, score):
        self.board=copy.deepcopy(board)
        self.score=score

    def _restart(self):
        self.board = [[0, 0, 0, 0] for i in range(4)]
        self.score = 0
        self.done = False
        self.info = {}
        self.episode_length = 0
        self._generateNew(2)
        if self.render:
            self._updateBoardUI()

    def _initBoardUI(self):
        self.scoreboard.setText('Score : {}'.format(0))
        self.board_labels = [[0, 0, 0, 0] for i in range(4)]
        for i in range(4):
            for j in range(4):
                self.board_labels[i][j] = QLabel(self)
                self.board_labels[i][j].setFont(self.board_font)
                self.board_labels[i][j].setAlignment(Qt.AlignCenter)
                self.board_labels[i][j].resize(100, 100)
                self.board_labels[i][j].move(110 * j + 30, 110 *i+70)

    def _updateBoardUI(self):
        for i in range(4):
            for j in range(4):
                col=self.color_dict[self.board[i][j]]
                if self.board[i][j] == 0:
                    txt=''
                else:
                    txt=str(self.board[i][j])
                self.board_labels[i][j].setText(txt)
                self.board_labels[i][j].setStyleSheet('background-color:%s'%col)
        self.scoreboard.setText('Score : {}'.format(self.score))


    def keyPressEvent(self,e):
        if self.render and self.keyboard_control:
            if e.key()==Qt.Key_W or e.key()==Qt.Key_Up:
                self._moveUp()
            elif e.key() == Qt.Key_S or e.key()==Qt.Key_Down:
                self._moveDown()
            elif e.key()==Qt.Key_A or e.key()==Qt.Key_Left:
                self._moveLeft()
            elif e.key()==Qt.Key_D or e.key()==Qt.Key_Right:
                self._moveRight()

    def _moveLeft(self):
        self.prev_board=copy.deepcopy(self.board)
        self.episode_length += 1
        for i in range(4):
            tmp = []
            for j in range(4):
                if self.board[i][j] != 0:
                    tmp.append(self.board[i][j])
            for k in range(len(tmp) - 1):
                if tmp[k] != 0 and tmp[k] == tmp[k + 1]:
                    tmp[k] *= 2
                    self.score += self.score_dict[tmp[k]]
                    tmp = tmp[:k + 1] + tmp[k + 2:] + [0]
            tmp += [0] * (4 - len(tmp))
            self.board[i] = tmp
        self._checkBoard()
        if self.render:
            self._updateBoardUI()

    def _moveRight(self):
        self.prev_board=copy.deepcopy(self.board)
        self.episode_length += 1
        for i in range(4):
            tmp = []
            for j in range(4):
                if self.board[i][j] != 0:
                    tmp.append(self.board[i][j])
            for k in range(len(tmp) - 1, 0, -1):
                if tmp[k] != 0 and tmp[k] == tmp[k - 1]:
                    tmp[k] *= 2
                    self.score += self.score_dict[tmp[k]]
                    tmp = [0] + tmp[:k - 1] + tmp[k:]
            tmp = [0] * (4 - len(tmp)) + tmp
            self.board[i] = tmp
        self._checkBoard()
        if self.render:
            self._updateBoardUI()

    def _moveUp(self):
        self.prev_board = copy.deepcopy(self.board)
        self.episode_length += 1
        for j in range(4):
            tmp = []
            for i in range(4):
                if self.board[i][j] != 0:
                    tmp.append(self.board[i][j])
            for k in range(len(tmp) - 1):
                if tmp[k] != 0 and tmp[k] == tmp[k + 1]:
                    tmp[k] *= 2
                    self.score += self.score_dict[tmp[k]]
                    tmp = tmp[:k + 1] + tmp[k + 2:] + [0]
            tmp += [0] * (4 - len(tmp))
            for i in range(4):
                self.board[i][j] = tmp[i]
        self._checkBoard()
        if self.render:
            self._updateBoardUI()

    def _moveDown(self):
        self.prev_board = copy.deepcopy(self.board)
        self.episode_length += 1
        for j in range(4):
            tmp = []
            for i in range(4):
                if self.board[i][j] != 0:
                    tmp.append(self.board[i][j])
            for k in range(len(tmp) - 1, 0, -1):
                if tmp[k] != 0 and tmp[k] == tmp[k - 1]:
                    tmp[k] *= 2
                    self.score += self.score_dict[tmp[k]]
                    tmp = [0] + tmp[:k - 1] + tmp[k:]
            tmp = [0] * (4 - len(tmp)) + tmp
            for i in range(4):
                self.board[i][j] = tmp[i]
        self._checkBoard()
        if self.render:
            self._updateBoardUI()

    def _checkBoard(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 2048:
                    self.done = True
                    self.info['episode_length'] = self.episode_length
                    self.info['success'] = True
                    self.info['total_score'] = self.score
        if self.prev_board != self.board:
            self._generateNew(1)
        elif not self._getAvailablePos(self.board):  
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
                if board[1][0] == board[2][0] or board[0][1] == board[0][2] or board[3][1] == board[3][2] or board[3][1] == \
                        board[3][2]:
                    return True
                return False
            if not _canMove(self.board):
                self.done = True
                self.info['episode_length'] = self.episode_length
                self.info['total_score'] = self.score
                if self.info.get('success') is None:
                    self.info['success'] = False
                

    def _generateNew(self, num):
        sample = random.sample(self._getAvailablePos(self.board), num)
        for i in range(num):
            x, y = sample[i]
            self.board[x][y] = 2

    def _getAvailablePos(self, arr):
        res = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == 0:
                    res.append([i, j])
        return res

    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self,event):
        reply=QMessageBox.question(self,'Warning','Are you sure you want to quit?',
            QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    env = Game2048Env(True, False, True)    
    obs = env.reset()
    done = False
    while not done:
        # A random agent as example
        # 0-3 means: up, down, left, right respectively
        action = random.randint(0, 3)
        time.sleep(0.2)
        obs, rew, done, info = env.step(action)
        print(rew, done, info)
    # remember to close the env, but you can always let resources leak on your own computer :|
    env.close()
    exit(0)
