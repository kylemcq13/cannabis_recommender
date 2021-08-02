import pandas as pd
from nltk import word_tokenize
import re


def effects_reco(effect1, effect2, effect3, df):
    
    # remove characters, make lower case, tokenize
    df['cleaned_effects'] = df['Effects'].apply(\
    lambda x : ' '.join([(word.lower()) \
    for word in word_tokenize(re.sub(r'([^\s\w]|_)+', ' ', str(x)))]))

    # count the user input words
    df['word1'] = df['cleaned_effects'].str.contains(effect1).astype(int)
    df['word2'] = df['cleaned_effects'].str.contains(effect2).astype(int)
    df['word3'] = df['cleaned_effects'].str.contains(effect3).astype(int)

    # add column to sum up the word match score
    df['score'] = df['word1'] + df['word2'] + df['word3']

    # return top recos, sort by Rating and word match score
    df.sort_values(by=['Rating', 'score'], inplace=True, ascending=False)

    return df[['Strain', 'Type', 'Flavor', 'Description']][0:5]
