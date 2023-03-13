from ast import literal_eval
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
from timeit import default_timer as timer
import pandas as pd


cloud_config= {
        'secure_connect_bundle': 'secure-connect-big-data.zip'}
auth_provider = PlainTextAuthProvider('EqnHqhrKSAYMiFMSRqgIxIjf', 'UxwRrWu6Z2-U.c5aBO2LwPEpJ8NMZ5t-5q.NXCEk-OphPU.cpRkMvsZj8rMIny7hOGJ8KlTg9BHJCq0NiI17_sZ+4e8mm6XpA7Lo+pBB7Trt,Cd-i0,zIRHLS8+i7Y_I')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('big_data')
 #function gia gia na parw to xrono kai na kanei ki to insert
def query2():
    start = timer()
    insert = session.prepare("INSERT INTO query2 (movieId, title, tag, rating, genres) VALUES (?, ?, ?, ?, ?)")

#Read csv with pandas
    df = pd.read_csv (r'movies_mesos_oros_tags_genres.csv', encoding="utf-8", nrows=1000) # gia xilia rows giati alliws tha epairne para poly xrono 
    df['title']=df['title'].apply(literal_eval)
    insert.consistency_level = ConsistencyLevel.QUORUM

#insert the data from the csv to cassandra 
    for index,row in df.iterrows():
        movieId=int(row[0])
        rating=float(row[1])
        title=row[2]
        genres=str(row[3])
        tag=str(row[4])
      
       
        
        session.execute(insert, [movieId, title, tag, rating, genres]) 
    end = timer() #stop tou xronou 
    print(end - start) #ektypwsh ths timhs gia to time 
#kalw to function gia na ta ektelesei       
query2()
