import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from random import random
from sklearn_som.som import SOM

# Question 2: Load the wine dataset from sklearn:
wine = datasets.load_wine()

# We consider the data X and labels y as follows:
X = wine.data
label = wine.target

# Question 3: Creating a SOM model
som = SOM(m=16, n=16, dim=13, random_state=1234)
# Parameters m (vertical) and n (horizontal) represent the dimensions of the [m × n] matrix.
# The objective is to find the optimal parameters for this dataset. You can try different values for m, n, and dim.

# Question 4: The data X is used to train the model as follows:
som.fit(X)

# Question 5: We apply the trained model to "predict" the cluster associated with each record in X as follows:
predictions = som.predict(X)

# Question 6:  
# Convert this index into a position hx, yi on the two-dimensional grid
x = predictions // som.m
y = predictions % som.m


# Question 7: Now we are interested in visualizing the results:
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(5, 7))
colors = ['red', 'green', 'blue']
x = predictions // som.m + [random() for _ in range(len(predictions))]
y = predictions % som.m + [random() for _ in range(len(predictions))]
ax[0].scatter(x, y, c=label, cmap=ListedColormap(colors))
ax[0].title.set_text('After one epoch')

# Question 8: Test with some numbers of epochs:
som.fit(X, epochs=100)
predictions = som.predict(X)
x = predictions // som.m + [random() for _ in range(len(predictions))]
y = predictions % som.m + [random() for _ in range(len(predictions))]
ax[1].scatter(x, y, c=label, cmap=ListedColormap(colors))
ax[1].title.set_text('After 100 epochs')


# Question 9: Additionally, here's another possible visualization that uses a transformation of each row of X 
# into a vector of distances from each position on the two-dimensional grid:
plt.figure()
plt.imshow(som.transform(X))

# Question 10: Finally, display the graphs:
plt.show()
