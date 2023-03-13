import pandas as pd
import numpy as np
#coding=utf-8 

df=pd.read_csv (r'tag.csv')
df=df.groupby(['movieId'])['tag'].unique().apply(list)
df.to_csv('new_grouped_tag.csv')
