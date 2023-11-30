Rapport sur le Code : Analyse de Deux Heuristiques pour le Puzzle 8-Puzzle

Ce code a pour objectif de comparer deux heuristiques différentes pour résoudre le puzzle du 8-Puzzle, un jeu de réflexion classique. Les deux heuristiques examinées sont la Distance de Manhattan et la Commutation de Tuiles Restantes. Le code est structuré comme suit :

Génération d'un État Initial Aléatoire (fonction generer) :

Une fonction nommée generer est définie pour générer un état initial aléatoire du puzzle.
Cette fonction construit une chaîne de caractères représentant le puzzle en mélangeant les chiffres de 0 à 8 de manière aléatoire.
Les chiffres sont mélangés de sorte à éviter les doublons, assurant ainsi que chaque chiffre n'apparaisse qu'une seule fois.
Importation du Module 8puzzle :

Le code utilise la bibliothèque importlib pour importer un module nommé 8puzzle depuis une source externe. Ce module contient les fonctionnalités nécessaires pour résoudre le puzzle du 8-Puzzle.
Définition des États Objectif et Initial :

Les états objectif et initial du puzzle sont définis à l'aide d'instances de la classe EightPuzzle du module importé.
L'état objectif représente la configuration finale souhaitée du puzzle, tandis que l'état initial représente la configuration initiale à partir de laquelle la résolution commence.
Sélection des Heuristiques :

Deux heuristiques différentes sont sélectionnées pour évaluer la résolution du puzzle : la Distance de Manhattan (heuristique h) et la Commutation de Tuiles Restantes (heuristique h2).
Définition de la Méthode de Transition d'État :

Une méthode de transition d'état du puzzle est sélectionnée à l'aide de la variable output. Cette méthode détermine comment les états sont générés à partir de l'état actuel lors de la recherche.
Test des Heuristiques :

Le code effectue deux tests distincts pour chaque heuristique.
Pour chaque test, il mesure le temps nécessaire pour résoudre le puzzle à l'aide de l'heuristique respective.
Les résultats de chaque test sont affichés, montrant le chemin de résolution du puzzle et le temps d'exécution de l'heuristique.
Comparaison des Heuristiques :

Enfin, le code calcule la différence de temps d'exécution entre les deux heuristiques et l'affiche.
Cette comparaison permet d'évaluer la performance relative des deux heuristiques pour résoudre le puzzle du 8-Puzzle.
En résumé, ce code explore deux approches différentes pour résoudre le puzzle du 8-Puzzle en utilisant deux heuristiques distinctes. Il génère des états initiaux aléatoires, mesure le temps de résolution, et compare les performances des heuristiques pour déterminer laquelle est plus efficace dans ce contexte particulier.