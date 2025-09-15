import pandas as pd 
import numpy as np
df = pd.read_csv('/content/RealEstate-USA.csv')
selected_columns = df[['brokered_by','price','acre_lot' ,'city' ,'house_size']]
selected_columns
price = selected_columns['price']
house_size = selected_columns['house_size']
brokered_by = selected_columns['brokered_by']
acre_lot = selected_columns['acre_lot']
city = selected_columns['city']
# Numpy basic statics::::::::::::::::::::::::::::::::::::::::::::::::
print("Price mean :", np.mean(price))
print("Price median :", np.median(price))
print("Price average :",np.average(price))
print("Price standard deviation :",np.std(price))
print("Price max :",np.max(price))
print("Price min :",np.min(price))
print("Price varience :", np.var(price))
# Basic statistic on house_size::::::::::::::::::::::::::::::::::::::
print("Price mean :", np.mean(house_size))
print("Price median :", np.median(house_size))
print("Price average :",np.average(house_size))
print("Price standard deviation :",np.std(house_size))
print("Price max :",np.max(house_size))
print("Price min :",np.min(house_size))
print("Price varience :", np.var(house_size))

# basic arithmetic Operations on price and house_size::::::::::::::::
np.add(price,house_size)
np.subtract(price,house_size)
np.multiply(price,house_size)
np.divide(price,house_size)
# Creating 2D and 3D arrays::::::::::::::::::::::::
array_2D = np.array([price,house_size])
Array_3D = np.array([price,house_size,acre_lot])
# Itrate in Price ::::::::::::
for val in np.nditer(price):
   print(val)
   for val in np.ndenumerate(price):
    print(val)
# Print 7 Common Properties of Price Array:::::::::::::::::::::::::
print("\nProperties of price array:")
print("ndim:", price.ndim)
print("shape:", price.shape)
print("size:", price.size)
print("dtype:", price.dtype)
print("itemsize:", price.itemsize)
print("nbytes:", price.nbytes)
print("type:", type(price))
# Apply Geometric Functions (sin, cos, etc.) on 2D Array:::::::::::::::::
sin_values = np.sin(array_2D)
cos_values = np.cos(array_2D)
tan_values = np.tan(array_2D)
print("Sin values:", sin_values)
print("Cos values:", cos_values)
print("Tan values:", tan_values)

  