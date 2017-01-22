import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
word_data = pickle.load( open("word_data_overfit.pkl", "r"))		
authors = pickle.load( open("email_authors_overfit.pkl", "r") )


### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]

### your code goes here
from sklearn.tree import DecisionTreeClassifier		
from sklearn.metrics import accuracy_score		
		
clf = DecisionTreeClassifier(min_samples_split=40)		
clf.fit(features_train, labels_train)		
pred = clf.predict(features_test)		
print "Accuracy:", accuracy_score(labels_test, pred)		
		
print "Important features:"		
for index, feature in enumerate(clf.feature_importances_):		
    if feature>0.2:		
        print "feature no", index        		
        print "importance", feature		
 		
"""		
 Result:		
 		
 For word_data and email_authors:		
 	Accuracy: 1.0		
 For word_data_overfit and email_authors_overfit:		
 	Accuracy: 0.959044369601		
 	Important Features:		
 		feature no: 33604		
 		Importance: 0.7674705882325		
 			
 """


