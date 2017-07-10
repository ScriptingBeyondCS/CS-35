import random
import math

import sklearn
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

import json
import requests
import textblob

import nltk
from nltk.corpus import opinion_lexicon

print('Assembling data...')

# Get data from json file
f = open( 'app_reviews.json', "r" )
string_data = f.read()
dict_data = json.loads(string_data)

# random.seed(0)
random.shuffle(dict_data)

# Read all of the opinion words in from the nltk corpus.
pos=list(opinion_lexicon.words('positive-words.txt'))
neg=list(opinion_lexicon.words('negative-words.txt'))

#Store them as a set (it'll make our feature extractor faster).
pos_set = set(pos)
neg_set = set(neg)

#------------------------------------------------------------------------------------

# DEFINE YOUR FEATURES IN THIS FUNCTION
def review_features(review):
    """feature engineering for product reviews"""
    # CREATE A DICTIONARY OF FEATURES (such as sentiment analysis, product id, helpfulness, etc.)

    features = {"sample": 5}
    return features

#------------------------------------------------------------------------------------

# Convert dictionary of features to an array (these are our inputs)
features = [review_features(review) for review in dict_data]
v = DictVectorizer(sparse=False)
X = v.fit_transform(features)

# For printing purposes, data is a list of tuples with (review content, input features, score)
data = []
X_data = []
y_data = []
for i in range(len(dict_data)):
    data += [(dict_data[i], X[i], dict_data[i]['overall'])]
    X_data += [data[i][1]]
    y_data += [data[i][2]]

# Assemble data into training, devtest, and test sets
X_train = X_data[:5000]
y_train = y_data[:5000]

X_devtest = X_data[5000:6500]
y_devtest = y_data[5000:6500]

X_test = X_data[6500:]
y_test = y_data[6500:]

print('Running regression...')         

#------------------------------------------------------------------------------------
# USE CROSS VALIDATION TO GET BEST # OF N_ESTIMATORS AND MAX_DEPTH FOR RANDOM FOREST REGRESSOR
rforest = RandomForestRegressor()
rforest.fit(X_train, y_train)
predictions = rforest.predict(X_devtest)
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
# PRINT SOME VISUAL REPRESENTATION OF ERROR...FOR DEVTEST SET ONLY!!!
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
# DETERMINE HOW MANY PREDICTIONS FROM TEST SET WERE WITHIN 1 STAR
#------------------------------------------------------------------------------------

print("Score on test set:", rforest.score(X_test, y_test))