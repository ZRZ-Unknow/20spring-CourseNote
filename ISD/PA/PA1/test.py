'''
@Descripttion: 
@version: 
@Author: Zhou Renzhe
@Date: 2020-04-19 01:09:33
@LastEditTime: 2020-04-19 10:22:59
'''
import numpy as np

a=np.array([[1,2],[3,4],[5,6]])

b=[(1,2),(3,4),(5,6)]

if (1,2) in b:
    print(b.index((3,4)))
U=[1,5,3]
print(max(U))