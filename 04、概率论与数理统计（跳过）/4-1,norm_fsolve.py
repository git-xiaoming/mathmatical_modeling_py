#程序文件Pex4_1.py
from scipy.stats import norm    # 正态分布
from scipy.optimize import fsolve   # 解方程
print("p=",norm.cdf(6,3,5)-norm.cdf(2,3,5))
f=lambda c: norm.cdf(2*c,3,5)-norm.cdf(-3*c,3,5)-0.6
print("c=",fsolve(f,0))
