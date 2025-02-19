# -*- coding: utf-8 -*-
"""KNN Classifier

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I3inqNZHdbzf54JAvo42-WAbniMesrj9
"""

import pandas as pd
import numpy as np

from google.colab import files
upload = files.upload()

dataset = pd.read_csv('breast_cancer.csv')
dataset

print(dataset.shape)
print(dataset.head(5))

X = dataset.iloc[:, :-1].values
X

Y = dataset.iloc[:, -1].values
Y

!pip install scikit-learn

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=4)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
X_train

error = []
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

n_samples_train = X_train.shape[0]

error = []
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

n_samples_train = X_train.shape[0]

# Ensure n_neighbors is less than or equal to n_samples_train
for i in range(1, min(40, n_samples_train + 1)):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, y_train)
    pred_i = model.predict(X_test)
    error.append(np.mean(pred_i != y_test))

plt.figure(figsize=(12, 6))
plt.plot(range(1, min(40, n_samples_train + 1)), error, color='red', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3 , metric = 'cosine' , p=2)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
#cm = confusion_matrix(y_test, y_pred)
#print(cm)
print("Accuracy of the Model: {0}%".format(accuracy_score(y_test, y_pred) * 100)) # Changed to format with parentheses