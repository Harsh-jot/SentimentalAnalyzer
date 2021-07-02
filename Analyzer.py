# Load and prepare the dataset
import nltk
from nltk.corpus import movie_reviews
import random

documents = [(list(movie_reviews.word(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# Define the feature extractor

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
  document_words = set(document)
  features = {}
  for word in word_features:
    features['contains({})'.fromat(word)] = (word in document_words)
    return features
  
  # Train Naive Bayes classifier
  featuresers = [(document_features(d), c) for (d,c) in documents]
  train_set, test_set = features[50:], ffeaturesets[:50]
  classfier = nltk.NaiveBayesClassfier.train(train_set)
  
  # Test the classfier
  print(nltk.classfy.accuracy(classfier, test_set))
