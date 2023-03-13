import pandas as pd 

df = pd.read_csv(r'movies_seperated_with_year2.csv')
df.drop('genres_y', inplace=True, axis=1) 
df.to_csv('movies_seperated_with_year2.csv', index=False)