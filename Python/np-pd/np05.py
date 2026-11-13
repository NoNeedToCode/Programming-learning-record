import numpy as np

a=np.arange(3,15)
print(a)
print(a[3])
b=a.reshape(3,4)
print(b[2])
print(b[2][1])
print(b[1,:])
print(b[:,:])

for row in b:
    print(row)

for column in b.T:
    print(column)

print(b.flatten())

for item in b.flat:
    print(item)
