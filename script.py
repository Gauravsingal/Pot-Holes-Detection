# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 02:05:33 2018

@author: msbhakuni
"""

import pandas as pd

data = pd.read_csv('data_0.txt', delimiter= ' ')


data['p'] = 0

x = data.iloc[:, 0].values

y = data.iloc[:. 1].values

z = data.iloc[:, 2].values

p = data.iloc[:, 3].values


​
for i in range(997):
	if(z[i]>8 and z[i]<12 and z[i]>z[i+1] or x[i]>8 and x[i]<12 and x[i]>z[i+1]
    or  y[i]>8 and zy[i]<12 and y[i]>y[i+1] ):
            d = z[i] - z[i+1]
            if(d>4):
                p[i+1]=1
         
del data['p']


data.to_csv('final_data' ,  index = False)
	
​
	