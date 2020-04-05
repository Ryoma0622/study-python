#%% [markdown]
# $$
# \boldsymbol{X} = \begin{bmatrix}
# 1 & 2 & 3 \\
# 1 & 2 & 5 \\
# 1 & 3 & 4 \\
# 1 & 5 & 9 \\
# \end{bmatrix}
# , \ \boldsymbol{y} = \begin{bmatrix}
# 1 \\
# 5 \\
# 6 \\
# 8 \\
# \end{bmatrix}
# $$
# のとき
# $$
# \boldsymbol{w} = (\boldsymbol{X}^{T}\boldsymbol{X})^{-1}\boldsymbol{X}^{T}\boldsymbol{y}
# $$
# - Step1: $\boldsymbol{X}^{T}\boldsymbol{X}$
# - Step2: $(\boldsymbol{X}^{T}\boldsymbol{X})^{-1}$
# - Step3: $\boldsymbol{X}^{T}\boldsymbol{y}$
# - Step4: $\boldsymbol{w} = (\boldsymbol{X}^{T}\boldsymbol{X})^{-1}\boldsymbol{X}^{T}\boldsymbol{y}$
#%%
import numpy as np
# ## X の定義
X = np.array([
  [1, 2, 3],
  [1, 2, 5],
  [1, 3, 4],
  [1, 5, 9],
])
print(X)
# ## y の定義
y = np.array([
  [1],
  [5],
  [6],
  [8],
])
print(y)

import sklearn

# # 重回帰分析
from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=False)
model.fit(X, y)
model.coef_
model.score(X, y)
x = np.array([[1, 2, 3]])
model.predict(x)