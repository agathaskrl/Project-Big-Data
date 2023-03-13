import pandas as pd 

df = pd.read_csv(r'new_grouped_rating.csv')
df.drop('userId', inplace=True, axis=1) 
df.to_csv('no_userId_rating_grouped.csv', index=False)