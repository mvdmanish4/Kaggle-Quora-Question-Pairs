import tensorflow.contrib.learn as skflow
from sklearn import datasets, metrics

#load dataset here from the csv file
trainingData = loadData()
classfier = skflow.TensorFlowLinearClassifier(n_classes=4)
classifier.fit(trainingData.features, trainingData.target)