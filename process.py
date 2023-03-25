import pandas as pd, numpy as np
from scipy import stats
                                            # tfidf          # bag-of-words
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

import re, json, pickle, openpyxl, os, re, random
from enum import Enum

import spacy, nltk
from nltk.corpus import wordnet

from fields import *

# nlp = spacy.load("pt_core_news_sm")
class Documents(Enum):
    DRE = 1
    BALANCETE = 2


def find_synonyms(words, qty):

    new_words = []
    for word in words:
        if len(word.split(' ')) > 1:
            word = word.split(' ')[0]

        synonyms=[];
        for syn in wordnet.synsets(word, lang='por'):
            for lemma in syn.lemmas(lang='por'):
                synonyms.append(lemma.name())

        print(synonyms)
        if len(synonyms) > 0:
            new_words.append(np.random.choice(synonyms, size=qty))
        else:
            new_words.append(word)

    return new_words


def vectorize_csv(df, only_strings=False, method='tfidf'):
    
    if only_strings:
        is_word = r'[A-Za-z\s]+'
        words = []
        for column in df.select_dtypes(include=['object']):
            for cell in df[column]:
                if isinstance(cell, str):
                    matches = re.findall(is_word, cell)
                    words.extend(matches)
        text = ' '.join(words)
        
    else:
        flatten = df.astype(str).values.flatten()
        text = ' '.join(flatten)

    print(text)
    vectorizer = TfidfVectorizer()
    if method == 'bagwords':
        vectorizer = CountVectorizer()

    print(method)
    vector = vectorizer.fit_transform([text]).toarray()[0]
    print(vector)
    # return vector


def classify_sheet(sheet):

    valid_sheet = clean_sheet(sheet)
    vectorize_csv(valid_sheet, method='bagwords')

    # model = 'svm'
    # clf = pickle.loads(open(f"models/{model}.pkl", "rb"))
    # clf.predict(X)

    type_ = 0
    return type_


def clean_sheet(sheet):
    """
    Remove noise data, like nans and sheet header
    """

    #clean nan cols and rows
    sheet = sheet.dropna(how='all', axis=1).dropna(how='all', axis=0)

    #most frequent row nans pattern
    mode = stats.mode(sheet.isna().sum(axis=1), keepdims=True)[0][0]

    #assuming this as where to scrap data
    data = pd.concat([row for _, row in sheet.iterrows() if row.isna().sum() == mode], axis=1).T

    valid_data = pd.concat([col for _, col in data.items() if col.isna().sum() < len(col)*0.1], axis=1)

    return valid_data


# def process(sheet):
    
#     print(sheet.shape)


