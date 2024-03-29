# ARMA
import pandas as pd, numpy as np
import statsmodels.api as sm
import matplotlib.pylab as plt
import statsmodels.tsa.arima.model
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plt.rc('axes', unicode_minus=False)
plt.rc('font', family='SimHei')
plt.rc('font', size=16)
d = pd.read_csv('sunspots.csv')
dd = d['counts']
years = d['year'].values.astype(int)

# 画出原始数据的折线图，初步确定观测数据是否平稳
plt.plot(years, dd.values, '-*')
plt.figure()

# 进一步判断是否平稳
ax1 = plt.subplot(121)
plot_acf(dd, ax=ax1, title='自相关')
ax2 = plt.subplot(122)
plot_pacf(dd, ax=ax2, title='偏自相关')

# 确定p，q的值，使AIC,BIC尽量最小
for i in range(1, 6):
    for j in range(1, 6):
        md = sm.tsa.ARMA(endog=dd, order=(i, j)).fit(disp=0)
        print([i, j, md.aic, md.bic])
zmd = sm.tsa.ARMA(endog=dd, order=(4, 2)).fit()
print(zmd.summary())  # 显示模型的所有信息

residuals = pd.DataFrame(zmd.resid)
fig, ax = plt.subplots(1, 2)
residuals.plot(title="残差", ax=ax[0])
residuals.plot(kind='kde', title='密度', ax=ax[1])
plt.legend('')
plt.ylabel('')

dhat = zmd.predict()
plt.figure()
plt.plot(years[-20:], dd.values[-20:], 'o-k')
plt.plot(years[-20:], dhat.values[-20:], 'P--')
plt.legend(('原始观测值', '预测值'))
dnext = zmd.predict(d.shape[0], d.shape[0])
print(dnext)  # 显示下一期的预测值
plt.show()
