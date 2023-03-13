from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
import pandas as pd
import datetime

cloud_config= {
        'secure_connect_bundle': 'secure-connect-big-data.zip'
    }
auth_provider = PlainTextAuthProvider('EqnHqhrKSAYMiFMSRqgIxIjf', 'UxwRrWu6Z2-U.c5aBO2LwPEpJ8NMZ5t-5q.NXCEk-OphPU.cpRkMvsZj8rMIny7hOGJ8KlTg9BHJCq0NiI17_sZ+4e8mm6XpA7Lo+pBB7Trt,Cd-i0,zIRHLS8+i7Y_I')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('big_data')


insert = session.prepare("INSERT INTO rating (userId, movieId, rating, timestamp) VALUES (?, ?, ?, ?)")

#Read csv with pandas
df = pd.read_csv (r'rating.csv')
#insert the data from the csv to cassandra 
for index,row in df.iterrows():
        userId=int(row[0])
        movieId=int(row[1])
        rating=float(row[2])
        timestamp=datetime.datetime.strptime(row[3],"%Y-%m-%d %H:%M:%S")
        session.execute(insert, [userId, movieId, rating, timestamp])
 
