import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generating some sample data
data = {
    'Year': [2010, 2011, 2012, 2013, 2014],
    'Revenue': [50000, 60000, 75000, 90000, 100000],
    'Profit': [20000, 25000, 30000, 35000, 40000]
}

df = pd.DataFrame(data)

# Data analysis
print("Mean Revenue:", np.mean(df['Revenue']))
print("Max Profit:", np.max(df['Profit']))

# Data visualization
plt.figure(figsize=(8, 6))
plt.plot(df['Year'], df['Revenue'], marker='o', color='b', label='Revenue')
plt.plot(df['Year'], df['Profit'], marker='s', color='r', label='Profit')
plt.xlabel('Year')
plt.ylabel('Amount ($)')
plt.title('Revenue and Profit Over Time')
plt.legend()
plt.grid(True)
plt.show()