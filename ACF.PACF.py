from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm 
import pandas as pd
from pandas import Series  
import numpy as np 
import matplotlib.pyplot as plt


#Below is the previously used method for calculating the PACF and ACF with outliers derived from a Z-score 
#Calculate Z-scores and create a Series of outliers 

def detect_outlier(data_1):
... 	threshold = 3
... 	mean_1 = np.mean(data_1)
... 	std_1 = np.std(data_1)
... 	for y in data_1:
... 		z_score=(y-mean_1)/std_1
... 		if np.abs(z_score)>threshold:
... 			itOutliers.append(y)
... 	return Series(itOutliers)

# y = Series of outliers to be used as a variable in the formula below  
#Used to create the ACF and PACF visual 
 def tsplot(y,lags=None,figsize=(12,7),style='bmh'):
... 	if not isinstance(y, pd.Series):
... 		y=pd.Series(y)
... 	with plt.style.context(style):
... 		fig = plt.figure(figsize=figsize)
... 		layout = (2,2)
... 		ts_ax = plt.subplot2grid(layout,(0,0),colspan=2)
... 		acf_ax = plt.subplot2grid(layout,(1,0))
... 		pacf_ax =plt.subplot2grid(layout, (1,1))
... 		y.plot(ax=ts_ax)
... 		p_value = sm.tsa.stattools.adfuller(y)[1]
... 		ts_ax.set_title('Time Series Analysis of Crypto Exchange Volume \n Dickey-Fuller: p={0:.5f}'.format(p_value))
... 		sm.graphics.plot_acf(y,lags=lags, ax=acf_ax)
... 		sm.graphics.plot_pacf(y,lags=lags, ax=pacf_ax)
... 		plt.tight_layout()




#Generic method for visualizing a PACF and ACF 


sm.graphics.tsa.plot_acf(data, lags=40)
sm.graphics.tsa.plot_pacf(data, lags=40)
plt.show()




##StatsModels reference link: 
https://www.statsmodels.org/stable/generated/statsmodels.graphics.tsaplots.plot_acf.html 