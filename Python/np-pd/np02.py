import numpy as np

a=np.array([2,23,4],dtype=np.float64)# 最后是指明
print(a.dtype)
b=np.ones((3,4))
print(b)
c=np.empty((4,4))
print(c)
print(np.arange(10,20,2).reshape((5,1)))
print(np.linspace(1,10,5).reshape((5,1)))
