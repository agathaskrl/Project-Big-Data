import pandas as pd 
df = pd.read_csv(r'merged_movies_mo_tags.csv')
df.drop('genres_y', inplace=True, axis=1) 
df.to_csv('merged_movies_mo_tags.csv', index=False)
'''a = pd.read_csv(r'merged_movies_mo_tags.csv')
b= pd.read_csv(r'movie.csv')
merged = a.merge(b, on='movieId')
merged.to_csv("merged_movies_mo_tags.csv", index=False) '''