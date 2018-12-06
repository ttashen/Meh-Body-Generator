import numpy as np
import pandas as pd
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.stem.snowball import EnglishStemmer
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize, WordPunctTokenizer, RegexpTokenizer
from nltk.tokenize import sent_tokenize
from sklearn.decomposition import PCA
from sklearn.svm import SVC


def nlp_content(content):
    '''
    Takes a panda series of product content and returns a series of list 
    of tokenized, non-digis, non-stopwords, lemmatized words
    
    INPUT: panda series
    OUTPUT: panda series
    '''
#     lower cases
    lower_content = content.apply(lambda x: str(x).lower())
#     tokenize content and removing punctuation
    tokenizer = RegexpTokenizer(r'\w+')
    tokenized = lower_content.apply(lambda x: tokenizer.tokenize(x))
#     remove stopwords
    stop_words = set(stopwords.words('english'))
    no_stopwords = tokenized.apply(lambda x : [word for word in x if word not in stop_words])
#     take out lone digits but leaves 1080p-like words
    no_digits = no_stopwords.apply(lambda x : [word for word in x if word.isdigit()==False])
#     lemmatizing words
    lemmatizer = WordNetLemmatizer()
    lemmatized = no_digits.apply(lambda x: [lemmatizer.lemmatize(word) for word in x])
    
    return lemmatized
    
def create_description(lemmatized_names, lemmatized_specs):
    '''
    Takes lemmatized names and lemmatized specs panda series, whose rows are lists of words,
    and combine the two lists of words into one, and put the words back to a string for each row.
    
    INPUT: two panda series
    OUTPUT: one panda series
    '''
    dd = pd.concat([lemmatized_names,lemmatized_specs], axis=1)
    d = dd.apply( lambda x: x.item_name + x.item_features, axis=1)
    
    return d


def tfidf_content(lemmatized_content):  
#     put list of words back to string format for vectorizing
    simplified = lemmatized_content.apply(lambda x: ' '.join(x))
    vectorizer = TfidfVectorizer(stop_words='english', max_features=100000)
    X = vectorizer.fit_transform(simplified)
    x = pd.DataFrame(X.toarray())
    
    return x
    
    

   
    