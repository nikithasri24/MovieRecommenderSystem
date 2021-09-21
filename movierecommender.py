import numpy as np
import pandas as pd


column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=column_names)

movie_titles = pd.read_csv("Movie_Id_Titles")
df = pd.merge(df,movie_titles,on='item_id')
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())

moviemat = df.pivot_table(index='user_id',columns='title',values='rating')

starwars_user_ratings = moviemat['Star Wars (1977)']
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars = corr_starwars.join(ratings['num of ratings'])
top_5_rec=corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head(n=6)
print(top_5_rec[1:])
