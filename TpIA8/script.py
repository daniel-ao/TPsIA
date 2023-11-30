import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from scipy import interp
from sklearn.metrics import roc_auc_score
import pandas as pd

wine = datasets.load_wine()

# Question 2: Retrieve the object containing all information about the dataset using the load_wine() method
wine = datasets.load_wine()

# Q3: Retrieve wine data, build a dataframe, and assign to variable X.
X = pd.DataFrame(wine.data)

# Q4: Retrieve example classes from the target attribute. Build a dataframe and assign to variable y.
y = pd.DataFrame(wine.target)

# Q5: Analyze the dimensions of y using the shape property.
y.shape

# Q6: Since ROC is applicable for binary classification, and we have three classes, we need to create three binary classifiers.
# Convert y to binary using label_binarize().
y = label_binarize(y, classes=[0, 1, 2])

# Q7: 
'''
Explanation: The label_binarize function transforms the multi-class labels into binary format.
Each column corresponds to one class, and each row represents an instance. 
The value 1 in a column indicates the presence of that class for the corresponding instance, and 0 indicates the absence.
'''

# Q8: Assign the number of classes present in the dataset to the variable n_classes:
y = label_binarize(y, classes=[0, 1, 2])
n_classes = y.shape[1]  # because y.shape = (178, 3)

# Q9: Assign the number of examples in the dataset to the variable n_samples, 
# and the number of features to the variable n_features:
n_samples, n_features = X.shape

# Q10: Build training and test sets named X_train, X_test, y_train, y_test.
#  For example, we can use proportions like 70% for training and 30% for testing for the first evaluation,
#  and 50% for both training and testing for the second evaluation. Other combinations can be tried.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)


# Q11: Build the model using the "decision tree" classifier.
model_decisiontree = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)
model_decisiontree.fit(X_train, y_train)

# Q12: What are the predicted classes by the model?
# Assign the result to the variable y_score and analyze its content:
y_score = model_decisiontree.predict(X_test) 


# Q13: Recall that the ROC curve needs, for different thresholds,
# the false positive rate (to be placed on the x-axis) 
# and the true positive rate (to be placed on the y-axis). 
# Also, the model quality is given by the area under the curve (AUC).

# Create three dictionaries and name them tfp, tvp, and roc_auc:
tfp = dict()  # dictionary with false positives
tvp = dict()  # dictionary with true positives
roc_auc = dict()


# Q14: The roc_curve() method returns three vectors: a vector with different thresholds ordered in descending order,
# referred to as thresholds; a vector with different false positive rates, where the element i corresponds to the false positive rate for the threshold thresholds[i]; 
# and the third array with different true positive rates, where the element i corresponds to the true positive rate for the threshold thresholds[i].

# The following loop will help us obtain these three arrays. 
# n_classes is the number of classes obtained in question 8. 
# It will calculate the necessary data for constructing the ROC curve for each class:
for i in range(n_classes):
    tfp[i], tvp[i], thresholds = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(tfp[i], tvp[i])  # calculate the area under the curve


# Q15: Display the curve for class 1.

# The attributes lw corresponds to the intensity we want to give to the curve lines, lw=0 means no curve;
# label contains the label we would like to associate with the curve.
# linestyle contains the type of the curve plot.
plt.figure()
plt.plot(tfp[1], tvp[1], color='green', lw=2, label='ROC curve (AUC = %0.3f)' % roc_auc[1])

# The formatting directive "%0.3f" is used to display the area under the curve for class 1 with 3 decimal places.


# Q16: To include in the graph the theoretical line corresponding to a model with AUC = 0.5 (f(x) = x)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='dashdot')

# Q17: Set the boundaries of the curve with plt.xlim([0.0, 1.0]) and plt.ylim([0.0, 1.0]),
# meaning that the domain of false and true positives is [0, 1].
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])

# Q18: Place the labels associated with the x-axis and y-axis on the curve.
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')

# Q19: Give a title to the curve using the title() method.
plt.title('Example of ROC Curve')

# Q20: Place the legend of the curve at the bottom right of the figure (lower right).
plt.legend(loc="lower right")

# Q21: Finally, display the ROC curve:
plt.show()

