import pandas as pd
pinakas=[]
df = pd.read_csv (r'movies_seperated.csv', encoding="utf-8") 
for index,row in df.iterrows(): 
    data=str(row[3])
    #print(row[1]) 
    #print(data)
    pinakas.append(data)
df['year']=pinakas
df.to_csv('movies_seperated_with_year.csv', index=False)