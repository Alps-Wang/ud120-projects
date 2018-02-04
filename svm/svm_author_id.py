#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

### import package
from sklearn.svm import SVC

### create classifier
###clf = SVC(kernel = "linear")

clf = SVC(kernel = "rbf",C=10000)


### time cli.fit
t0 = time()


### get 1% of original size, tossing out 99% of the training data.
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

### fit classifier
clf.fit(features_train,labels_train)

print "training time:", round(time()-t0, 3), "s"



### time cli.pred
t0 = time()

### make prediction
pred = clf.predict(features_test)

print "testing time:", round(time()-t0, 3), "s"


### calculate accuracy
#from sklearn.metrics import accuracy_score
#acc = accuracy_score(pred, labels_test)
#print acc

#print pred[10]
#print pred[26]
#print pred[50]

print sum(pred)

#def submitAccuracy():
#    return acc

#submitAccuracy()
#########################################################


