import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 3.9, 6.1])

print(x.mean())
print(y.mean())

xc = x - x.mean()
print(xc)

yc = y - y.mean()
print(yc)

xx = xc * xc

print(xx)

xy = xc * yc
print(xy)

xsum = xx.sum()
ysum = xy.sum()
xy.sum()

a = xy.sum() / xx.sum()
print(a)