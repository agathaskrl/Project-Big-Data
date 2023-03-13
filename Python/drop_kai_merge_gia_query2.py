import pandas as pd 
#gia drop apo ton allo pinaka kai to pairnw gia na balw ta mh se lista genres
'''df = pd.read_csv(r'movie_kai_mesos_oros.csv')
df.drop('genres', inplace=True, axis=1)
df.to_csv('movies_mesos_oros_tags_genres.csv', index=False) ''' 

#kai twra kanw merge me to movies gia na parw ta original genres
'''a = pd.read_csv(r'movies_mesos_oros_tags_genres.csv')
b= pd.read_csv(r'movie.csv')
merged = a.merge(b, on='movieId')
merged.to_csv("movies_mesos_oros_tags_genres.csv", index=False)'''

#kai twra kanw merge me ta tags wsta na ta exw ola se ena pinaka 
a = pd.read_csv(r'movies_mesos_oros_tags_genres.csv')
b= pd.read_csv(r'no_userId_timestamp_on_tags.csv')
merged = a.merge(b, on='movieId')
merged.to_csv("movies_mesos_oros_tags_genres.csv", index=False)