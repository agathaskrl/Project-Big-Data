import pandas as pd 

df= pd.read_csv(r'/content/drive/MyDrive/AgathaDb/rating.csv') 

rt=df.groupby(['movieId']).mean() 
rt.to_csv('/content/drive/MyDrive/AgathaDb/new_grouped_rating.csv')