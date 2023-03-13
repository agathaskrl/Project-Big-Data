import pandas as pd
a = pd.read_csv(r'movie_kai_mesos_oros.csv')
b= pd.read_csv(r'no_userId_timestamp_on_tags.csv')
merged = a.merge(b, on='movieId')
merged.to_csv("merged_movies_mo_tags.csv", index=False)