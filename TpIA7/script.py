from sklearn.metrics import confusion_matrix, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris


iris = load_iris()

donnees = pd.DataFrame(iris.data)

donnees.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

target = pd.DataFrame(iris.target)

x_train, x_test, y_train, y_test = train_test_split(donnees, target, test_size=0.30, random_state=1)

model_decisiontree = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5)

model_decisiontree.fit(x_train, y_train)

y_pred = model_decisiontree.predict(x_test)

precision = accuracy_score(y_test, y_pred) * 100
print(f"Accuracy: {precision:.2f}%")

from sklearn.metrics import confusion_matrix, classification_report

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Calculate and print Mean Absolute Error
print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))

# Calculate and print Mean Squared Error
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))

# Calculate and print Root Mean Squared Error
print('Root Mean Squared Error:', np.sqrt(mean_squared_error(y_test, y_pred)))

fn = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
cn = ['setosa', 'versicolor', 'virginica']

plt.figure(figsize=(7, 5))
plot_tree(model_decisiontree, feature_names=fn, class_names=cn, filled=True)
plt.show()