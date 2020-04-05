#%%
import numpy as np
import pandas as pd

df = pd.read_csv('../data/housing.csv')
df.head()
len(df)
df.describe()

import seaborn as sns
sns.distplot(df['y'])
