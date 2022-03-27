import pandas as pd

# From https://stackoverflow.com/questions/41286569/get-total-of-pandas-column and https://datascience.stackexchange.com/questions/77174/pandas-sum-of-multiple-specific-columns

df = pd.read_csv('sales.csv', index_col=0)
df.loc['Total'] = pd.Series([df['sales'].sum(),df['expenditure'].sum()], index = ['sales','expenditure'])

print(df)
