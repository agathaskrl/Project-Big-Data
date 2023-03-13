import pandas as pd 

df = pd.read_csv(r'no_userId_timestamp_on_tags.csv')
df.drop('userId', inplace=True, axis=1) 
df.to_csv('no_userId_timestamp_on_tags.csv', index=False)