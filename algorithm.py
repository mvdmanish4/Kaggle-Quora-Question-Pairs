#Decision Tree Classifier
import sklearn
from sklearn import tree
features = [[140,"smooth"],[130,"smooth"],
[150,"bumpy"],[170,"bumpy"]]

#140 is the feature such as term frequency
#smooth = 1 (smooth is the question)
#bumpy = 0 (bumpy is another question)

binFeatures = [[140,1],[130,1],
[150,0],[170,0]]

labels = ["a","a","b","b"]

#a = 1
#b = 0

binLabels = [1,1,0,0]

#Classifier Object
clf = tree.DecisionTreeClassifier()

#Training algorithm is included in classifier object and is called fit
#Think of fit as synonym for "Find Patterns in Data"
clf = clf.fit(binFeatures,binLabels)

#Input to the classifier is the feature of new fruit
#You can give any number of inputs in classifier
print (clf.predict([[150,0]]))
if clf.predict([[150,0]]) == 1:
	print ("a")
else:
	print ("b")

print (type(clf.predict([[150,0]])))

#Learn how to set features
#Learn numpy and scikit learn libraries
#Implement learning algorithm by storing input data in training set after processing
C