import pandas as pd 
import numpy as np 
import sklearn
from sklearn.decomposition import TruncatedSVD 

# preparing the data 
columns = ['user_ID' , 'item_ID' , 'rating' , 'timestamp']
frame = pd.read_csv('.\\data\\u.data' , sep='\t' , names=columns)
# print(frame.head())

columns = ['item_id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
          'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

movies = pd.read_csv('.\\data\\u.item', sep='|', names=columns, encoding='latin-1')
movie_names = movies[['item_id', 'movie title']]
# print(movie_names.head())

# combine data
combined_movies_data = pd.merge(frame, movie_names, left_on='item_ID', right_on='item_id')
combined_movies_data.groupby('item_id')['rating'].count().sort_values(ascending=False).head()

filter = combined_movies_data['item_id']==50
# print(combined_movies_data[filter]['movie title'].unique())

# bulding a utility matrix 
rating_crosstab = combined_movies_data.pivot_table(values='rating', index='user_ID', columns='movie title', fill_value=0)
# print(rating_crosstab.head())



X = rating_crosstab.T
X.shape

# DECOMPOSING THE MATRIX
SVD = TruncatedSVD(n_components=12, random_state=17)
resultant_matrix = SVD.fit_transform(X)
resultant_matrix.shape

# correlation matrix
corr_mat = np.corrcoef(resultant_matrix)
corr_mat.shape

# isolating starwars
movie_names = rating_crosstab.columns
movies_list = list(movie_names)
star_wars = movies_list.index('Star Wars (1977)')
star_wars
corr_star_wars = corr_mat[1398]
corr_star_wars.shape

# recommanding a highly correlated movie
print(list(movie_names[(corr_star_wars<1.0) & (corr_star_wars > 0.9)]))
