#%% [markdown]
# # 行列演算の基礎
# $$
# \boldsymbol{w} = (\boldsymbol{X}^{T}\boldsymbol{X})^{-1}\boldsymbol{X}^{T}\boldsymbol{y}
# $$
# ## TODO
# - ベクトルの定義
# - 行列の定義
# - 転置
# - 逆行列
# - 行列積

import numpy as np

# ## ベクトルの定義
x = np.array([
  [1],
  [2],
  [3]
])
print(x)

# ## 行列の定義
X = np.array([
  [1, 2],
  [3, 4]
])
print(X)

# ## 転置
Xt = X.T
print(Xt)

# ## 逆行列
# linear algebra: 線形代数
X_inv = np.linalg.inv(X)
print(X_inv)

# ## 行列積
XX_inv = np.dot(X, X_inv)
print(XX_inv)

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

# ## Step1
XtX = np.dot(X.T, X)
print(XtX)

# ## Step2
XtX_inv = np.linalg.inv(XtX)
print(XtX_inv)

# ## Step3
Xty = np.dot(X.T, y)
print(Xty)

# ## Step4
w = np.dot(XtX_inv, Xty)
print(w)
