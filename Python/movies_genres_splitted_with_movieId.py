import pandas as pd
pinakas=[]
df = pd.read_csv (r'movie.csv', encoding="utf-8")
for index,row in df.iterrows(): 
    #Edw kanw split gia na parw ta genres xwris | kai epeita ta bazw se lista kai epeita sto csv file 
    data=str(row[2]).split("|") 
    pinakas.append(data)
df['genres']=pinakas
df.drop('title', inplace=True, axis=1)   #drop ton titlo giati den to xreiazomai  
df = df.explode('genres').reset_index(drop=True)
df.to_csv('movies_genres_splitted.csv', index=False)