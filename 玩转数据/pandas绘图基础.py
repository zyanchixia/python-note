# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 22:34:16 2018

"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
x = np.linspace(0,1)#x轴取0-1的区间
y = np.sin(4*np.pi*x)*np.exp(-5*x)
t = pd.DataFrame(y,index = x)
t.plot()