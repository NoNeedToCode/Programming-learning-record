import numpy as np
import pandas as pd
s=pd.Series([1,3,6,np.nan,44,1])
print(s)
dates = pd.date_range('20250701',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

df1=
