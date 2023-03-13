import pandas as pd
a = pd.read_csv(r'movies_seperated_with_year2.csv')
b= pd.read_csv(r'movie.csv')
merged = a.merge(b, on='movieId')
merged.to_csv("movies_seperated_with_year2.csv", index=False)