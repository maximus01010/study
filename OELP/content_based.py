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
writer_matrix=np.array(W)
