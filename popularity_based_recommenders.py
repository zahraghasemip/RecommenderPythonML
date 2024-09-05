import pandas as pd 
import numpy as np 

address1 = '.\\data\\rating_final.csv'
address2 = '.\\data\\chefmozcuisine.csv'
frame = pd.read_csv(address1)
cuisine = pd.read_csv(address2)

rating_count = pd.DataFrame(frame.groupby('placeID')['rating'].count())
sort_rating = rating_count.sort_values('rating' , ascending=False).head()
print(sort_rating)

most_rated_places = pd.DataFrame([135085,132825,135032,132834,135052], index=np.arange(5), columns=['placeID'])
summary = pd.merge(most_rated_places , cuisine , on='placeID')
print(summary)
cuisine_type = cuisine['Rcuisine'].describe()
print(cuisine_type)
