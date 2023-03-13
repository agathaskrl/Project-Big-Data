import pandas as pd
a = pd.read_csv(r'new_grouped_tag.csv')
b= pd.read_csv(r'movie_kai_mesos_oros.csv')
# kanw merge dyo arxeia sto movieId gia na parw ena teliko merged arxeio 
merged = a.merge(b, on='movieId')
merged.to_csv("movie_kai_mesos_oros_kai_tags.csv", index=False)