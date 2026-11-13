import numpy as np

a=np.arange(3)
b=a
c=a
print(a,b,c)
a[2]=10
print(a,b,c)
c=b.copy()
a[1]=100
print(a,b,c)
