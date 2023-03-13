from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
import pandas as pd

cloud_config= {
        'secure_connect_bundle': 'secure-connect-big-data.zip'
    }
auth_provider = PlainTextAuthProvider('EqnHqhrKSAYMiFMSRqgIxIjf', 'UxwRrWu6Z2-U.c5aBO2LwPEpJ8NMZ5t-5q.NXCEk-OphPU.cpRkMvsZj8rMIny7hOGJ8KlTg9BHJCq0NiI17_sZ+4e8mm6XpA7Lo+pBB7Trt,Cd-i0,zIRHLS8+i7Y_I')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('big_data')


insert = session.prepare("INSERT INTO movies (movieId, title, genres) VALUES (?, ?, ?)")
 
df = pd.read_csv (r'movie.csv')

for index,row in df.iterrows():
        movieId=int(row[0])
        title=str(row[1])
        genres=str(row[2])
        session.execute(insert, [movieId, title, genres])
 
