import pandas as pd
#coding=utf-8 
pinakas=[]
pinkas2=[] 
df = pd.read_csv (r'movie.csv', encoding="utf-8")
for index,row in df.iterrows(): 
    data=str(row[1]).split(" ")
    data2=str(row[2]).split("|") 
    #print(row[1]) 
    #print(data)
    pinakas.append(data)
    pinkas2.append(data2)
df['title']=pinakas
df['genres']=pinkas2
df.to_csv('movies_seperated1.csv', index=False)