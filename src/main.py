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
