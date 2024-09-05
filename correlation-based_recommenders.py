import pandas as pd 
import numpy as np 

address1 = '.\\data\\rating_final.csv'
address2 = '.\\data\\chefmozcuisine.csv'
address3 = '.\\data\\geoplaces2.csv'
frame = pd.read_csv(address1)
cuisine = pd.read_csv(address2)
geodata = pd.read_csv(address3 , encoding='ISO-8859-1')

places = geodata[['placeID' , 'name']]
# print(places)
# print(cuisine.head())

rating = pd.DataFrame(frame.groupby('placeID')['rating'].mean())
rating['rating_count'] = pd.DataFrame(frame.groupby('placeID')['rating'].count())
# print(rating.describe())

the_most_popular_place = rating.sort_values('rating_count', ascending=False).head()
# print(the_most_popular_place)

# name of the place.....
the_most_popular_place_name = places[places['placeID']==135085]
the_most_popular_place_cuisine = cuisine[cuisine['placeID']==135085]
# print(the_most_popular_place_name , the_most_popular_place_cuisine)

# preparing data for analysis 
places_crosstab = pd.pivot_table(data=frame , values='rating' , index='userID' , columns='placeID')
# print(places_crosstab.head())
Tortas_ratings = places_crosstab[135085]
# print(Tortas_ratings[Tortas_ratings>=0])

# evaluating similarity based on correlation 
similar_to_Tortas = places_crosstab.corrwith(Tortas_ratings)
corr_Tortas = pd.DataFrame(similar_to_Tortas , columns =['PearsonR'])
corr_Tortas.dropna(inplace=True)
# print(corr_Tortas.head()) 

Tortas_corr_summary = corr_Tortas.join(rating['rating_count'])
Tortas_corr_summary[Tortas_corr_summary['rating_count']>=10].sort_values('PearsonR', ascending=False).head(10)
# print(Tortas_corr_summary)

places_corr_Torts = pd.DataFrame([135085 , 132754 , 135045 , 135062 , 135028 , 135042 , 135046] , index = np.arange(7) , columns = ['placeID'])
summary = pd.merge(places_corr_Torts  , cuisine , on='placeID')
print(summary)




