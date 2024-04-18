import pandas as pd
import numpy as np
import ast
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

df = pd.read_csv('/home/sasidharreddy/study/OELP/data.csv', delimiter=',')

name = []
genres = []

# Convert the string to a list using ast.literal_eval
for i in df['genres']:
    genres_list = ast.literal_eval(i)
    genres.append(genres_list)

for i in df['Name']:
    moviename = ast.literal_eval(i)
    name.append(moviename)

# Create a DataFrame with movie names as rows and genres as columns
unique_genres = np.unique([genre for sublist in genres for genre in sublist])
print(unique_genres)
matrix = [[1 if word in sublist else 0 for word in unique_genres] for sublist in genres]
print(matrix[1338])
