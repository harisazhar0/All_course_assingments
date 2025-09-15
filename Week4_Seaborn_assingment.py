# Week 4 Seaborn Assignment
# Load the dataset
import pandas as pd

url = "https://raw.githubusercontent.com/ShahzadSarwar10/Fullstack-WITH-AI-B-3-SAT-SUN-6Months-Explorer/main/DataSetForPractice/RealEstate-USA.csv"
df = pd.read_csv(url)

print(df)

df.head()
df.info()
df.describe()
df.dtypes
df.shape
import seaborn as sns
import matplotlib.pyplot as plt
# Set the style of seaborn
# lineplot of city and price ::::::::::::::::
sns.lineplot(x='city', y = 'price', data = df)
plt.title('City vs Price')
plt.xlabel('City')
plt.ylabel('Price')
plt.show()
# Kdeplot of zip_code and price::::::::::::::::::
sns.kdeplot(x='zip_code',y='price',data = df)
plt.title('zip_code vs price')
plt.xlabel('zip_code')
plt.ylabel('price')
plt.show()
# Scatter plot of zip_code and price:::::::::::::::::
sns.scatterplot(x='zip_code', y='price', data=df)
plt.title('Zip Code vs Price')
plt.show()
# Bar plot of zip_code and price:::::::::::::::::
sns.barplot(x='zip_code', y='price', data=df)
plt.title('Zip Code vs Price')
plt.show()
# Box plot of zip_code and price:::::::::::::::::
sns.boxplot(x='zip_code', y='price', data=df)       
plt.title('Zip Code vs Price')
plt.show()
# Heatmap of the zip_code and price:::::::::::::::::
sns.heatmap(df[['zip_code', 'price']].corr())
plt.title('Heatmap of Zip Code and Price')
plt.show()
