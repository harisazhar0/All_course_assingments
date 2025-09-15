##Week6_Task_1_Linear_Regression::::::::::::::::::::::::
###:::::::::::::::::::::::::
import pandas as pd 

import numpy as np 

import seaborn as sns 

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

df = pd.read_csv('RealEstate-USA.csv')

df.columns
print('the df describe is :',df.describe())

print('the df shape is :',df.shape)

print('the df info is :',df.info())

print('the df dtype is :',df.dtypes)

print('the df head is :',df.head())

df['house_size'] = df['house_size'].fillna(df['house_size'].mean())

x = df[['house_size']]

y = df[['price']]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,random_state=42)

print(x_train.shape)

print(y_train.shape)

print(x_test.shape)
print(y_test.shape)

Lr = LinearRegression()

Lr.fit(x_train,y_train)

print('the coef is :',Lr.coef_)

print('the intercept is :',Lr.intercept_)

y_pred = Lr.predict(x_test)

def calculate_sale_amount(assessed_value, slope, intercept):

    return intercept + slope * assessed_value

slope = Lr.coef_[0][0]

intercept = Lr.intercept_[0]

sample_values = [1500, 2000, 2500]

for val in sample_values:

    result = calculate_sale_amount(val, slope, intercept)

    print(f"Assessed Value: {val} => Sale Amount: {result}")

print('MSE is :',mean_squared_error(y_test,y_pred))

print('R2 score is :',r2_score(y_test,y_pred))

print('MAE is :',mean_absolute_error(y_test,y_pred))

print('SQ of MSE is:',np.sqrt(mean_squared_error(y_test,y_pred)))


#Week6_Task_2_Linear_Regression::::::::::::::::::::::::
#### week6_Task2:::::::::::::::::::::::
import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
#1
url = r"C:\Users\hamza\Documents\Ai_assingments\zameencom-property-data-By-Kaggle-Short.csv"

df = pd.read_csv(url, sep = ';',on_bad_lines='skip')
#2
print(df.head(4))
print("data frame info is ",      df.info())

print("data frame describe is",   df.describe())

print("data frame shape is",      df.shape)

print("data frame columns are",   df.columns)

print("data frame dtypes are",    df.dtypes)

print("data frame null values are",df.isnull().sum())   
#3
x = df[['bedrooms']]
y = df['price']
#4
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)
print(x_train.shape)
print(y_train.shape)
#5
lr  = LinearRegression()
lr.fit(x_train,y_train)
#6
print('lr_coeff is :',lr.coef_)
#7
print('lr_intercept is :',lr.intercept_)
#8
def calculate_sale_amount(assessed_value, slope, intercept):
    return intercept + slope * assessed_value
slope = lr.coef_
intercept = lr.intercept_

sample_values = [1500, 2000, 2500]
for val in sample_values:
    result = calculate_sale_amount(val, slope, intercept)
    print(f"Assessed Value: {val} => Sale Amount: {result}")
#9
y_pred = lr.predict(x_test)
#10
print('MSE is :',mean_squared_error(y_test,y_pred))

print('R2 score is :',r2_score(y_test,y_pred))

print('MAE is :',mean_absolute_error(y_test,y_pred))

print('SQ of MAE is',np.sqrt(mean_absolute_error(y_test,y_pred)))



#Wee6_Task3_Linear_Regression:::::::::::::::::::::::::::::
###:::::::::::::::::::::::::
import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
#1
url = r'C:\Users\hamza\Documents\Ai_assingments\number-of-registered-medical-and-dental-doctors-by-gender-in-pakistan (1).csv'
df=pd.read_csv(url,index_col= "Years")
df
#2
print('df_info_is',             df.info() )

print('df_dtypes_is',           df.dtypes )

print('df_describe_is',         df.describe() )

print('shape_of_df_is :',       df.shape )
#3
# Remove commas and convert to float
df['Female Doctors'] = df['Female Doctors'].str.replace(',', '').astype(float)

df['Female Dentists'] = df['Female Dentists'].str.replace(',', '').astype(float)
x = df[['Female Doctors']]
y = df['Female Dentists']
#4
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3,random_state=42)
print(x_train.shape)
print(y_train.shape)
#5
lr  = LinearRegression()
lr.fit(x_train,y_train)
#6
slope = print('lr_coeff is :',lr.coef_)
#7
intercept = print('lr_intercept is :',lr.intercept_)
#8
def calculate_female_dent_based_on_fem_doc(Female_doctors, slope, intercept):
    return intercept + slope * Female_doctors
slope = lr.coef_[0]
intercept = lr.intercept_
sample_values = [1000, 2000, 3000]
for val in sample_values:
    result = calculate_female_dent_based_on_fem_doc(val, slope, intercept)
    print(f'Female Dentists: {val} => Female Doctors: {result}')

#9
y_pred = lr.predict(x_test)
#10
print('MSE is :',mean_squared_error(y_test,y_pred))

print('R2 score is :',r2_score(y_test,y_pred))

print('MAE is :',mean_absolute_error(y_test,y_pred))

print('SQ of MAE is',np.sqrt(mean_absolute_error(y_test,y_pred)))




