import pandas as pd
pinakas=[]
df = pd.read_csv (r'movies_seperated.csv', encoding="utf-8") 
for index,row in df.iterrows(): 
    #parinw apo to telos, dhaldh sth thesh -3 pou jekinaei to telos ths paranthesh kai synhthw seinai to year 
    data=str(row[1][-7:-3])

    pinakas.append(data) #eisxwrhsh twn dedomenwn sto list 
df['year']=pinakas #to keli year tha parei ta deodmena ths listas pinakas
df.to_csv('movies_seperated_with_year.csv', index=False) #dhmioyrgia neou csv file 