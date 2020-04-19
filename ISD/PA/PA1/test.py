'''
@Descripttion: 
@version: 
@Author: Zhou Renzhe
@Date: 2020-04-19 01:09:33
@LastEditTime: 2020-04-19 21:30:44
'''
import numpy as np

a=np.ones((2,2,4))
a[0,0,2]=2
print(np.argmax(a[0,0]))