from ast import literal_eval
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


insert = session.prepare("INSERT INTO query5 (movieId, title, tag, rating, genres) VALUES (?, ?, ?, ?, ?)")

#Read csv with pandas
df = pd.read_csv (r'merged_movies_mo_tags.csv',  encoding="utf-8", nrows=2000)
df['genres']=df['genres'].apply(literal_eval)


#insert the data from csv to cassandra 
for index,row in df.iterrows():
        movieId=int(row[0])
        rating=float(row[1])
        genres=row[2]
        tag=str(row[3])
        title=str(row[4])
        #eketelsh tou session
        session.execute(insert, [movieId, title, tag, rating, genres])