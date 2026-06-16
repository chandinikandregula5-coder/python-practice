'''
DATA ANALYSIS
this process of inspecting,cleaning,transforming and modeling data to discover useful insights
descriptive analysis
1.-------------------
summarizing data

2.diagnostic analysis
---------------------
understanding causes

3.predictive analysis
---------------------
forecasting   future out comes

4.prescriptive analysis
-----------------------
suggesting actins based on data

5.why DA
---------
To improve deciscions making
detects trends and patterns

numpy(numerical python)
-----------------------
this python library for numerical computing. it provides support for multi dimensional arrays ,and linear algebra operations,making it essential for data analysis.....


using numpy in DA
-----------------
improved performance
simplifies complex operations
easy data manipulation.......


import numpy as np
arr_1 = np.array([[4,5,6,7],[1,2,3,4]])
print(arr_1)

import numpy as np
arr_1 = np.array([[4,5,6,7],[1,2,3,4]])
print(arr_1)
print(arr_1.shape)

import numpy as np
arr_1 = np.array([[4,5,6,7],[1,2,3,4]])
print(arr_1)
print(arr_1.shape)
reshaped=arr_1.reshape(3,2)
print(reshaped)

import numpy as np
arr_1 = np.array([[10,20,30,40,50,60])
print(arr_1)
print(arr_1*2)

import numpy as np
arr_1 = np.array([10,20,30])
nrm_copy = arr_1.view()
arm_1[0]=100
print(nrm_copy)
print(arr_1)

copy_dee = arr_1.copy()
arr_1[1]=200
print(copy dee)
print(arr_1)


pandas
---------
the pandas is a powerful data manipulation and analysis library..
where it provides data structure like series and dataframe for efficiency data handling....
import pandas as pd
any_=pd.series([2999,15999,52999,4999,1999]index=['Earbuds','smartphone','Lap','watch','footware'])
print(any_)

method series
-------------
mean()
sum()
max()
min()
apply()
map()

data frame
----------
'''
data = {'Ear buds','Smartphone','lap''watch','footware']
'Brand':['noise','oneplus','HP','BOLT,nike'],}

