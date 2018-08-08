import utils
import numpy as np
from collections import Counter
from sklearn.linear_model import LogisticRegression
import scipy.stats
from sgd_classifier import BasicSGDClassifier
import sst
import random
import os
from sklearn.metrics import classification_report
import vsm
from sklearn.feature_extraction.text import CountVectorizer
from PorterStemmer import PorterStemmer
from collections import defaultdict
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# import data

def fit_maxent_classifier(X, y, testFeatureVectors): 
    mod = LogisticRegression(fit_intercept=True)
    mod.fit(X, y)
    pred = mod.predict(testFeatureVectors)
    return pred
    
# create train, val, and test data

pred = fit_maxent_classifier(x_train, y_train, x_val)

correct = 0
total = len(y_val)
for i in range(0, len(y_val)):
    if (y_test[i]==pred[i]):
        correct+=1
        
print(correct)
print(total)
print(correct/total)
