#%%
import pandas as pd

# df = data frame
df = pd.read_csv('../data/original.csv')
df

import matplotlib.pyplot as plt

x = df['x']
y = df['y']

# plt.scatter(x, y)

df.describe()

df.mean()

df_c = df - df.mean()

#%%
df_c.head(3)

df_c.describe()
#%%

x = df_c['x']
y = df_c['y']

plt.scatter(x, y)
plt.show()
#%%
xx = x * x
xy = x * y

a = xy.sum() / xx.sum()
a

#%% [markdown]
# ## 予測値の求め方
# $$
# \hat{y} = ax
# $$
# ## 傾き$a$の計算式
# $$
# a = \frac{\displaystyle{\sum_{n=1}^{N}}x_{n}y_{n}}
# {\displaystyle{\sum_{n=1}^{N}}n^{2}}
# $$

plt.scatter(x, y, label='y') # 実測値
plt.plot(x, a * x, label='y_hat', color='red') # 予測値
plt.legend() # 凡例の表示
plt.show()

#%%
x_new = 40
mean = df.mean()

xc = x_new - mean['x']
xc
yc = a * xc
y_hat = a * xc + mean['y']
y_hat
a
mean['y']
#%%
def predict(x):
  a = 10069.022519284063
  xm = 37.62222
  ym = 121065.0
  # 中心化
  xc = x - xm
  y_hat = a * xc + ym
  return y_hat

predict(40)
predict(30)
#%%
