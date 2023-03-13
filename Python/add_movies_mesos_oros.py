import pandas as pd 
#coding=utf-8 
pinakas=[]
pinkas2=[] 
df = pd.read_csv (r'movie.csv', encoding="utf-8")
df['title'].split("(", expand=True)
df.to_csv("movie2.csv", index=False)

