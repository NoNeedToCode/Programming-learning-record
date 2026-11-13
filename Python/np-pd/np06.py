import numpy as np

a=np.array([1,1,1])
b=np.array([2,2,2])

c=np.vstack((a,b))
d=np.hstack((a,b,a))
print(a.shape,b.shape,c,d)

a=a[:,np.newaxis]
b=b[:,np.newaxis]

c=np.concatenate((a,b,b,a),axis=1)
print(a,b,c)
