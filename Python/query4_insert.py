from subprocess import list2cmdline
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
import pandas as pd
from ast import literal_eval

cloud_config= {
        'secure_connect_bundle': 'secure-connect-big-data.zip'
    }
auth_provider = PlainTextAuthProvider('EqnHqhrKSAYMiFMSRqgIxIjf', 'UxwRrWu6Z2-U.c5aBO2LwPEpJ8NMZ5t-5q.NXCEk-OphPU.cpRkMvsZj8rMIny7hOGJ8KlTg9BHJCq0NiI17_sZ+4e8mm6XpA7Lo+pBB7Trt,Cd-i0,zIRHLS8+i7Y_I')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('big_data')


insert = session.prepare("INSERT INTO query4 (movieId, rating, title, genres) VALUES (?, ?, ?, ?)")
 
df = pd.read_csv (r'movie_kai_mesos_oros.csv')
df['title'] = df['title'].apply(literal_eval)
df['genres'] = df['genres'].apply(literal_eval)
for index,row in df.iterrows():
        movieId=int(row[0])
        rating = float(row[1])
        title=row[2]
        genres=row[3]
       #eketelsh tou session
        session.execute(insert, [movieId, rating, title, genres])   
        
