# Week3_task2_pandas
#Question no 1::::::::
import pandas as pd
dict1 = {
    "Names": ['Ali','Hassan','Abdullah','Uzair','Ramzan','Hamza'],
    "Scores": [244,255,266,288,300,234],
    "Shifts": ['first','first','second','first','first','second'],
    "%_tage": [90 , 92 , 93 , 96 , 98 , 89]
}
df = pd.DataFrame(dict1)
df
#Question no 2 ::::::::
exam_data = {
    'Name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 
    'Kevin', 'Jonas'], 
    'Score': [12.5, 9, 16.5, 34 , 9, 20, 14.5, 45, 8, 19], 
    'Attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
    'Qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
} 
labels = [1,2,3,4,5,6,7,8,9,10]
#2.1
df2 = pd.DataFrame(exam_data,index= labels)
df2
#2.2
df2.head(3)
#2.3
df2[['Name','Score']]
#2.4
df2.loc[[1,3,5,7],['Name','Score']]
#2.5
df2[df2['Attempts'] > 2]
#2.6
df2.shape
#2.7
df2[(df2['Score'] >= 15) & (df2['Score'] <= 20)]
#2.8
df2[(df2['Attempts'] < 2) & (df2['Score'] > 15)]
#2.9
df2.loc['11', 'Score'] = 11.5
#2.10
df2['Score'].mean()
#2.11
k = {
    'Name':['hamad'],
    'Score': [24],
    'Attempts':[3],
    'Qualify':['no']
}
df2.loc[len(df2)] = k
df2.drop(11)
#2.12
df.sort_values(by=['names', 'scores'], ascending=[False,True])
#2.13
df2['Qualify'].replace({'yes': True, 'no': False})
#2.14
df2['Name'] = df2['Name'].replace('James', 'Suresh')
#2.15
df2.drop('Attempts', axis=1)
#2.16
df2.to_csv('exam_data.tsv', sep = '\t',index=False)