import pandas as pd
import ast
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

df = pd.read_csv('/home/sasidharreddy/study/OELP/data.csv', delimiter=',')
#print(df['directors'])
#print(df['popularity of director'][16])
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
print(d[16])
