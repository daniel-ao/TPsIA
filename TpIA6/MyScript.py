from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns

X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Display the content of X and y
print("Contents of X (samples):")
print(X)
print("\nContents of y (labels):")
print(y_true)
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Clustered Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
# Show the figure
plt.show()

# 6. Build the k-Means model with 4 clusters
kmeans = KMeans(n_clusters=4)  # Create a KMeans object with 4 clusters
kmeans.fit(X)  # Apply the fit method to fit the model to the data

# 7. Predict the classes for the elements in X
y_kmeans = kmeans.predict(X)

# Question 8
#Quelle est la classe prédite pour le deuxième élément de X ? Quelle est sa vraie classe ?
#Que constatez vous ?
# Predicted class for the second element of X
predicted_class_for_2nd_element = y_kmeans[1]
# True class of the second element of X
true_class_for_2nd_element = y_true[1]
# Compare the predicted class to the true class
print(f"Predicted class for the 2nd element: {predicted_class_for_2nd_element}")
print(f"True class for the 2nd element: {true_class_for_2nd_element}")

# 9. What is the predicted class for the fifth element of X?
#    What is its true class?
# Quelle est la classe prédite pour le cinquième élément de X ? Quelle est sa vraie classe ?
# Que constatez vous ?
print("Predicted class for the 5th element of X:", y_kmeans[4])  # Index 4 for the fifth element
print("True class of the 5th element of X:", y_true[4])

# 10. Display the true classes for all elements of X
# Afficher les classes de tous les éléments de X
print("True classes of all elements in X:")
print(y_true)

# 11. Display the predicted classes for all elements of X
# Afficher les classes prédites pour tous les éléments de X
print("Predicted classes for all elements in X:")
print(y_kmeans)

#Exercise 2:
#[3.1]
#Read the file

df = pd.read_csv('wine.csv')

# 14. Display the first 10 elements of the dataset
# 14. Afficher les 10 premieres éléments du jeu de données
print(df.head(10))
# 15. Display the last 10 elements of the dataset
# 15. Afficher les 10 derniers éléments du jeu de données
print(df.tail(10))

# 16. Display all the information about the dataset
# 16. Afficher toutes les informations concernant le jeu de données
df.info()

# 17. Take a look at the result. Are there any missing values?
# 17. Jetez un coup d'oeil au résultat. Y a-t-il des valeurs nulles?
missing_values = df.isnull().sum()
print("Missing Values / Valeurs manquantes:")
print(missing_values)

# 19. What are the data types of the variables in the dataset?
# 19. Quels sont les types de données des variables dans le jeu de données?
data_types = df.dtypes
print("Data Types / Types de données:")
print(data_types)

# 20. What are the labels in the DataFrame?
# 20. Quelles sont les étiquettes du DataFrame?
labels = np.unique(df['Class'])
print("Labels / Étiquettes:")
print(labels)

# Step 35: Customize the plot and display it
plt.xlabel("PCA Dimension 1")
plt.ylabel("PCA Dimension 2")
plt.title("Scatter Plot of Clusters")
plt.legend()
plt.show()

#[3.2]

# 22. Convert the DataFrame to a Numpy Array
# 22. Convertir le DataFrame en tableau Numpy
donnees = df.to_numpy()

# 23. Create a PCA object to reduce dimensions to 2
# 23. Créez un objet PCA pour réduire les dimensions à 2
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(donnees)


# 25. Instantiate a KMeans object with 3 clusters 
# 25. Instanciez un objet KMeans avec 3 clusters
kmeans = KMeans(n_clusters=3)

# 26. Use the fit_predict() method to get predicted labels with K-Means 
# 26. Utilisez la méthode fit_predict() pour obtenir les étiquettes prédites avec K-Means
classes = kmeans.fit_predict(reduced_data)

# 27. Find the unique values of the classes 
# 27. Trouvez les valeurs uniques des classes
labels_uniques = np.unique(classes)

# [3.3]

# 29. Read the dataset from "World_happiness_dataset_2019.csv" and assign it to the variable df
df = pd.read_csv("World_hapiness_dataset_2019.csv")

# 30. Create a scatter plot to visualize the relationship between a country's GDP per capita and their happiness score
plt.scatter(df["GDP per capita"], df["Score"])
plt.xlabel("GDP per capita")
plt.ylabel("Happiness Score")
plt.title("Scatter Plot of GDP per capita vs Happiness Score")
plt.show()

# 32. Use seaborn to create a scatter plot
sns.scatterplot(data=df, x="GDP per capita", y="Score")
plt.xlabel("GDP per capita")
plt.ylabel("Happiness Score")
plt.title("Seaborn Scatter Plot of GDP per Capita vs Happiness Score")
plt.show()

# 33. Visualize the data by category using catplot in seaborn
sns.catplot(data=df, x="GDP per capita", y="Score")
plt.xlabel("GDP per capita")
plt.ylabel("Happiness Score")
plt.title("Seaborn Categorical Plot of GDP per Capita vs Happiness Score")
plt.show()

# 34. Create scatter plots for different clusters
classe = df["Class"]
for label in labels_uniques:
    to_plot = reduced_data[np.where(classe == label)[0]]
    plt.scatter(to_plot[:, 0], to_plot[:, 1], s=20)

# Question 35 can be found on line: 93
