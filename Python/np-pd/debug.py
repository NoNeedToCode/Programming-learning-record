import numpy as np
import timeit
print(timeit.timeit("sum(range(100000000))",number=100)/100 )
print(timeit.timeit("np.sum(np.arange(100000000))",globals=globals(),number=100)/100 )
np.__config__.show
