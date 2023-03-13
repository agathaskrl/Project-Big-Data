from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
from timeit import default_timer as timer
import pandas as pd


cloud_config= {'secure_connect_bundle': 'secure-connect-big-data.zip'}
auth_provider = PlainTextAuthProvider('EqnHqhrKSAYMiFMSRqgIxIjf', 'UxwRrWu6Z2-U.c5aBO2LwPEpJ8NMZ5t-5q.NXCEk-OphPU.cpRkMvsZj8rMIny7hOGJ8KlTg9BHJCq0NiI17_sZ+4e8mm6XpA7Lo+pBB7Trt,Cd-i0,zIRHLS8+i7Y_I')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('big_data')

#Dhmiourgia function gia na kanei select na kanei to consistency kai na epistefei to xrono 
def query2():
    start = timer() #arxish metrhshs xronou 
    select = session.prepare("SELECT * FROM query2 WHERE title CONTAINS 'Jumanji' ALLOW FILTERING;")
    select.consistency_level = ConsistencyLevel.ONE
    rows = session.execute(select)

    end = timer() #telos metrhshs xronou 
    print(end - start) # print to xrono 
    return rows; 

res = query2()
res = pd.DataFrame(res) #Epistrofh result san data frame gia na bbgazei ta apotelesmata tou select 
print(res)




