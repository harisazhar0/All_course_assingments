# Week_6_Multi_Linear_regression:::::::::::::::::::::
###########:::::::::::::::::Task_4_:_:_:_:_

import pandas as pd 

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
#11
url = r'C:\Users\hamza\Documents\Ai_assingments\50_Startups (1).csv'
df = pd.read_csv(url)
pd.DataFrame(df)
#12
df.head(3)
df.info()
df.shape
df.describe()
df.dtypes
#13
variable = ['R&D Spend','Administration', 'Marketing Spend']
#14
sns.regplot(x ='R&D Spend' ,y = 'Profit',data = df )
sns.regplot(x = 'Marketing Spend',y = 'Profit',data = df )
sns.regplot(x = 'Administration',y = 'Profit',data = df )
#15
corr_met = df[['R&D Spend','Administration', 'Marketing Spend']].corr()
sns.heatmap(corr_met)
#16
x = df[variable]
y = df['Profit']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=42)
#17
lr = LinearRegression()
lr.fit(x_train,y_train)
#18
lr.coef_
lr.intercept_
#19
y_pred = lr.predict(x_test)
#20
print('MSE is :',mean_squared_error(y_test,y_pred))

print('R2 score is :',r2_score(y_test,y_pred))

print('MAE is :',mean_absolute_error(y_test,y_pred))

print('SQ of MAE is',np.sqrt(mean_absolute_error(y_test,y_pred)))



### Week_6_Task_5_Multi_Line:::::::::::::::::::::
#:::::::::::::::::::::::::
import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
#11
url = r'C:\Users\hamza\Documents\Ai_assingments\housing.csv'
df = pd.read_csv(url)
#12
df.head(3)
df.info()
df.shape
df.describe()
df.dtypes
#13
correlation = df.corr(numeric_only=True)
correlation['median_income'].sort_values()
#15
corr_mep = df[['housing_median_age', 'total_rooms', 'population', 'households', 'median_income','median_house_value']].corr()
sns.heatmap(corr_mep)

df.drop(['ocean_proximity','latitude','longitude','total_bedrooms'],axis=1,inplace=True)
variable = ['housing_median_age', 'total_rooms', 'population', 'households', 'median_income','median_house_value']

x = df[variable]
y = df['median_income']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=42)
print(x_train.shape)
print(y_train.shape)

#4
lr = LinearRegression()
lr.fit(x_train,y_train)
#5
lr.coef_
lr.intercept_
#6
y_pred = lr.predict(x_test)
#7
print('MSE is :',mean_squared_error(y_test,y_pred))
print('R2 score is :',r2_score(y_test,y_pred))
print('MAE is :',mean_absolute_error(y_test,y_pred))
print('SQ of MAE is',np.sqrt(mean_absolute_error(y_test,y_pred)))



#Week_6_Task_6_Multiple_Lineareg:::::::::::::::::::::::::::::::::::::
##:::::::::::::::::::::::::::::::::::::::::::::::
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/regression_sprint/mtcars.csv'

df = pd.read_csv(url)

df.head()

df.info()

df.shape

df.describe()

df.dtypes

correlation = df.corr(numeric_only=True)
correlation['mpg'].sort_values()

sns.regplot(x ='mpg' ,y = 'wt',data = df )
sns.regplot(x ='mpg' ,y = 'hp',data = df )
sns.regplot(x ='mpg' ,y = 'qsec',data = df )
sns.regplot(x ='mpg' ,y = 'disp',data = df )
sns.regplot(x ='mpg' ,y = 'drat',data = df )
sns.regplot(x ='mpg' ,y = 'cyl',data = df )
sns.regplot(x ='mpg' ,y = 'gear',data = df )
sns.regplot(x ='mpg' ,y = 'carb',data = df )
sns.regplot(x ='mpg' ,y = 'vs',data = df )
sns.regplot(x ='mpg' ,y = 'am',data = df )

corr_mep = df[['mpg', 'wt', 'hp', 'qsec', 'disp', 'drat', 'cyl', 'gear', 'carb', 'vs', 'am']].corr()
sns.heatmap(corr_mep)

variable = ['wt', 'hp', 'qsec', 'disp', 'drat', 'cyl', 'gear', 'carb', 'vs', 'am']

x = df[variable]
y = df['mpg']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=42)
print(x_train.shape)
print(y_train.shape)

lr = LinearRegression()
lr.fit(x_train,y_train)
lr.coef_
lr.intercept_
y_pred = lr.predict(x_test)

print('MSE is :',mean_squared_error(y_test,y_pred))
print('R2 score is :',r2_score(y_test,y_pred))
print('MAE is :',mean_absolute_error(y_test,y_pred))
print('SQ of MAE is',np.sqrt(mean_absolute_error(y_test,y_pred)))




