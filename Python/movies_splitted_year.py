import pandas as pd
pinakas=[]
df = pd.read_csv (r'movies_seperated_with_year.csv', encoding="utf-8") 
for index,row in df.iterrows(): 
     data=str(row[3]).split(")")
     pinakas.append(data)
df['year']=pinakas
df.to_csv('movies_seperated_with_year.csv', index=False)