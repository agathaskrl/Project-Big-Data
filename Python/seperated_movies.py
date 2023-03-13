import pandas as pd 

df = pd.read_csv (r'movie.csv')

for index,row in df.iterrows(): 
    data1=(row[1].split(" "))
    data2=(row[2].split("|"))
    df.to_csv('movies_seperated.csv')
