#Weeek3_task1_pandas
import pandas as pd
#1
df = pd.read_csv('RealEstate-USA.csv')
#2
print('the info od data is: ',    df.info())
print('the shape of data is: ', df.shape)
print('the columns of data is: ', df.columns)
print('the index of data is: ', df.index)
print('the describe of data is: ', df.describe())
print('the type of data is: ', df.dtypes)
#3
df.to_string()
#4
print('the first 5 rows of data is: ', df.head(7))
#5
print('the last 5 rows of data is: ', df.tail(9))
#6
df['city']
df['street']
#7
df[['city','street']]
#8
df.loc[5]
#9
df.loc[3:5:7]
#10
df.loc[3:9]
#11
df.loc[df['price'] > 100000]
#12
df.loc[df['city'] == 'Adjuntas']
#13
df.loc[df['city'] == 'Adjuntas'] 
(df['price'] < 180500)
#14
df.loc[7,['city','price', 'street' , 'zip_code' ,  'acre_lot']]
#15
df.loc[:,'city':'zip_code']
#16
df.loc[df['city'] == 'Adjuntas','city':'zip_code']
#17
df.iloc[5]
#18
df.iloc[[9,7,5]]
#19
df.iloc[5:13]
#20
df.iloc[:,2]
#21
df.iloc[:,[1,3,6]]
#22
df.iloc[2:6]
#23
df.iloc[[6,8,14],1:3]
#24
df.iloc[[1,5],1:4]
#25
new_row = {

'city': 'New City',
'price': 99999,
'street': 'New Street',
'zip_code': 12345,
'acre_lot':0.5,
'state': 'NC',
'house_size': 1500,
'status': 'NaN',
'bed': 4,
'bath': 3,
'prev_sold_date': 13/4/2009,
'brokered_by': 'NaN'}

df.loc[len(df)] = new_row
#26
df.drop(2)
#27
df.drop(df.index[4:7])
#28
df.drop(['house_size'], axis=1)
#29
df.drop(['house_size','state'], axis=1)
#30
df['state_change'] = df['state']
#31
df.rename(index={3:5})
#32
df.query('price < 127400 and city != "Adjuntas"')
#33
df.sort_values('price', ascending=True)
#34
df.groupby('city')['price'].sum()
#35
df.dropna()
#36
df.fillna(0)
# End of Assingment:::::::::::::::::::::::::::::::::::

