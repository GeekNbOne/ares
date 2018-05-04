import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Portfolio(object):

    def __init__(self):
        self._securities = {}
        self._holdings = []
        self._risk_factor_pool = RiskFactorPool()


class RiskFactorPool(object):
    pass


class RiskFactor(object):
    pass


class SimpleRiskFactor(RiskFactor):

    def __init__(self, name, data=None):
        self._data = pd.Series()
        self._data.index.name = 'date'
        self._data.name = name

    @property
    def name(self):
        return self._data.name


idx = pd.bdate_range('2017-01-01', '2018-01-01')
data = np.random.normal(0,0.12/ np.sqrt(250),size=len(idx))
data = np.exp(np.cumsum(data))

sr = pd.Series(data,index=idx)

sr.plot()
plt.show()