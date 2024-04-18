import pandas as pd
import ast
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

df = pd.read_csv('/home/sasidharreddy/study/OELP/data.csv', delimiter=',')
df_key=pd.read_csv('/home/sasidharreddy/study/OELP/keywords.csv', delimiter='\t')
name=[]
genres=[]
story=[]
rating=[]
directors=[]
pop_of_directors=[]
cast=[]
pop_of_cast=[]
for i in df['Name']:
    mve_list = ast.literal_eval(i)
    name.append(mve_list[0])
df['story'] = df['story'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stopwords.words('english')]))
for i in df['genres']:
    genres_list = ast.literal_eval(i)
    genres.append(genres_list)
for i in df['story']:
    storyline=ast.literal_eval(i)
    story.append(storyline[0].split())
for i in df['rating']:
    rating_list=ast.literal_eval(i)
    rating.append(rating_list)

d1={}
cas,rank1=[],[]
for i in df['cast']:
    i=ast.literal_eval(i)
    for j in i:
        cas.append(j)
for i in df['popularity of cast']:
    i=ast.literal_eval(i)
    for j in i:
        if j is None:
            j=5000
        rank1.append(j)
for i in range(len(cas)):
    d1[cas[i]] = rank1[i]

C = []                             # M is the matrix where each row represents each movie and column represents each unique keyword
for i in df['cast']:
    x = eval(i)
    l = []
    for j in d1.keys():
        if(j in x):
            if(int(d1[j])==0):
                l.append(0.09)
            else:
                l.append(1-(int(d1[j])/11000))
        else:
            l.append(0)
    C.append(l)

d={}
dir,rank=[],[]
for i in df['directors']:
    i=ast.literal_eval(i)
    for j in i:
        dir.append(j)
for i in df['popularity of director']:
    i=ast.literal_eval(i)
    for j in i:
        rank.append(j)
for i in range(len(dir)):
    d[dir[i]] = rank[i]

R = []                             # M is the matrix where each row represents each movie and column represents each unique keyword
for i in df['directors']:
    x = eval(i)
    l = []
    for j in d.keys():
        if(j in x):
            if(int(d[j])==0):
                l.append(0.09)
            else:
                l.append(1-(int(d[j])/11000))
        else:
            l.append(0)
    R.append(l)
s = set()                           # set of all unique keywords
for i in df_key['k_h']:
    x = eval(i)
    for j in x.keys():
        s.add(j)                             
M = []                             # M is the matrix where each row represents each movie and column represents each unique keyword
for i in df_key['k_h']:
    x = eval(i)
    l = []
    for j in s:
        if(j in x.keys()):
            if(x[j]==0):
                l.append(0.5)
            else:
                l.append(int(x[j]))
        else:
            l.append(0)
    M.append(l)

d2={}
writ,rank2=[],[]
for i in df['writers']:
    i=ast.literal_eval(i)
    for j in i:
        writ.append(j)
for i in df['popularity of writer']:
    i=ast.literal_eval(i)
    for j in i:
        if j is None:
            j=5000
        rank2.append(j)
for i in range(len(writ)):
    d2[writ[i]] = rank2[i]

W = []                             # M is the matrix where each row represents each movie and column represents each unique keyword
for i in df['writers']:
    x = eval(i)
    l = []
    for j in d2.keys():
        if(j in x):
            if(int(d2[j])==0):
                l.append(0.09)
            else:
                l.append(1-(int(d2[j])/11000))
        else:
            l.append(0)
    W.append(l)

unique_genres = np.unique([genre for sublist in genres for genre in sublist])
unique_story=np.unique([sto for sublist in story for sto in sublist])

genre_matrix = [[1 if word in sublist else 0 for word in unique_genres] for sublist in genres]
key_word_matrix = np.array(M)
cast_matrix=np.array(C)
director_matrix=np.array(R)
writer_matrix=np.array(W)
story_matrix=[[1 if word in sublist else 0 for word in unique_story] for sublist in story]
print(len(genre_matrix[0]))
print(len(key_word_matrix[0]))
print(len(cast_matrix[0]))
print(len(director_matrix[0]))
print(len(writer_matrix[0]))
print(len(story_matrix[0]))
#normalizing the matrices
def normalize_matrix(matrix, new_min, new_max):
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    matrix_range = max_val - min_val

    normalized_matrix = (matrix - min_val) / matrix_range * (new_max - new_min) + new_min
    return normalized_matrix


genre_normalized_matrix = normalize_matrix(genre_matrix, 0, 1)
key_words_normalized_matrix = normalize_matrix(key_word_matrix, 0, 1)
cast_genre_normalized_matrix = normalize_matrix(cast_matrix, 0, 1)
director_normalized_matrix = normalize_matrix(director_matrix, 0, 1)
writer_normalized_matrix = normalize_matrix(writer_matrix, 0, 1)
story_normalized_matrix = normalize_matrix(story_matrix, 0, 1)

final_matrix=np.hstack((genre_normalized_matrix,key_words_normalized_matrix,cast_genre_normalized_matrix,director_normalized_matrix,writer_normalized_matrix,story_normalized_matrix))
print(len(final_matrix[0]))
cos_sim1=cosine_similarity(final_matrix)

from sklearn.decomposition import NMF
# Sample movie-feature matrix (replace this with your actual data)
movie_feature_matrix = np.array(final_matrix)

# Number of latent features (adjust based on your preference)
n_features = 44
# Perform NMF for matrix factorization
model = NMF(n_components=n_features, init='random', random_state=42)
movie_factors = model.fit_transform(movie_feature_matrix)
feature_weights = model.components_

# Print the original matrix
#print("Original Matrix:")
#print(movie_feature_matrix)

# Print the decomposed matrices
#print("\nMovie Factors:")
#print(np.round(movie_factors, 2))

#print("\nFeature Weights:")
#print(np.round(feature_weights, 2))
# Reconstruct the original matrix

reconstructed_matrix = np.dot(movie_factors, feature_weights)
# Print the reconstructed matrix
print("\nReconstructed Matrix:")
print(np.round(reconstructed_matrix, 2))

cos_sim=cosine_similarity(reconstructed_matrix)
cos_final=(0.6)*cos_sim1+(0.4)*cos_sim

movie_name = 'Avengers: Infinity War'
try:
    index = name.index(movie_name)
    print(f"The index of {movie_name} in the list is {index}.")
except ValueError:
    print(f"{movie_name} is not present in the list.")

import numpy as np
print(index)
# Assuming you have an array named 'your_array'
max_array=np.array(cos_final[index])
print(max_array)

# Get the indices of the 11 maximum values
max_indices = np.argsort(max_array)[:-22:-1]

# Print the indices
print("Indices of the 11 maximum values:")
print(max_indices)
inde=0
for i in max_indices:
    inde=inde+1
    print(f'{inde}-{name[i]}')