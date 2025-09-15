#Week3_task3_pandas

import pandas as pd
#1
url = r'C:\Users\hamza\Documents\Ai_assingments\macro_monthly.csv'
df = pd.read_csv(url)
#2
print('Data frame info()'  ,      df.info())
print('Data frame shape'  ,       df.shape)
print('Data frame describe' ,    df.describe())
print('Data frame dtypes' ,      df.dtypes)
#3
df.to_string()
#4
print('the first 5 rows of data is: ', df.head(4))
#5
print('the last 5 rows of data is: ', df.tail(4))
#6
df['Industrial_Production']
df['Manufacturers_New_Orders: Durable Goods']
#7
df[['Industrial_Production','Manufacturers_New_Orders: Durable Goods']]
#8
df.loc[3]
#9
df.loc[3:5:7]
#10
df.loc[5:15]
#11
df.loc[df['Year'].isin([1993 , 1994 , 1997])&(df['Unemployment_Rate'] >= 1)]
#12
df.loc[:, 'Industrial_Production']
df.loc[:, 'Manufacturers_New_Orders: Durable Goods']
df.loc[:, 'Retail_Sales']
df.loc[:, 'Personal_Consumption_Expenditures']
#13
df.loc[df['Industrial_Production'] <=0.5]
#14
yes = df.loc[df['Industrial_Production'] <=0.5]
yes1 = yes.loc[yes['Consumer_Price Index'] > 0.2]
print(yes1)
#15
df.iloc[4]
#16
df.iloc[2:7]
#17
df.iloc[10:23]
#18
df.iloc[:,5]
#19
df.iloc[:,[2,3,8]]
#20
df.iloc[:,2:8]
#21
df.iloc[[4,5,7,25],[3,5,7]]
#22
df.iloc[3:34,3:6]
#23
11 == {
    'Year': 2020,
    'Month': 12,
    'Industrial_Production': 0.3,
    'Manufacturers_New_Orders: Durable Goods': 0.4,
    'Retail_Sales': 0.5,
    'Personal_Consumption_Expenditures': 0.6,
    'Consumer_Price Index': 0.7,
    'Unemployment_Rate': 0.8,
    'Personal_Consumption_Expenditures': 'NaN',
    'National_Home_Price_Index':'NaN',
    'All_Employees(Total_Nonfarm)':'NaN',
    'Labor_Force_Participation_Rate':'NaN',
    'Federal_Funds_Effective_Rate' :'NaN',
    'Building_Permits' : 'NaN',
    'Money_Supply_(M2)':'NaN',
    'Personal_Income' : 'NaN',
    'Trade_Balance' : 'NaN',
    'Consumer_Sentiment': 'NaN',
    'Consumer_Confidence': 0.9
}
df.loc[len(df)] = 11
#24
df.drop(11)
#25
df.drop(df.index[5:9])
#26
df.drop(['All_Employees(Total_Nonfarm)'], axis=1)
#27
df.drop(['Personal_Consumption_Expenditures' , 'National_Home_Price_Index'], axis=1)
#28
df.rename(columns={'Personal_Consumption_Expenditures' : 'Personal_Consumption_Expenditures_Changed'})
#29
df.query('Year == 1992 and Industrial_Production <= 0.5 and `Consumer_Price Index` > 0.2')
#30
df.sort_values(by = 'Consumer_Price Index', ascending = True)
#31
df.groupby('Year')['Industrial_Production'].sum()
#32
df.dropna() 
#33
df.fillna(0)