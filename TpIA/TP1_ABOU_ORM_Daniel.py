import importlib
from random import randint
import time



# Fonction pour générer un état aléatoire du puzzle
def generer():
    res = ""
    n = 0
    res2 = ""
    while len(res) != 9:
        n = randint(0,8)
        # Évitez les doublons en ajoutant seulement des nombres uniques
        if str(n) not in res:
            res = res + str(n)
    for i in range(8):
        res2 = res2 + res[i] + " "# Ajoutez un espace entre les chiffres
    return res2 + res[8]


# Import du module '8puzzle' depuis une bibliothèque externe
puzzle = importlib.import_module("8puzzle")


# Définition de l'état objectif et de l'état initial du puzzle
goal = puzzle.EightPuzzle("1 2 3 4 5 6 7 8 0")
initial = puzzle.EightPuzzle("1 2 4 8 7 0 6 3 5")


# Sélection des deux heuristiques à tester : Manhattan Distance et Tile Switches Remaining
h = puzzle.EightPuzzle.manhatten_distance
h2 = puzzle.EightPuzzle.tile_switches_remaining
output = puzzle.EightPuzzle.state_transition


# Test de l'heuristique de Manhattan Distance
print("Test de manhattan \n")
start_time = time.time()


# Utilisation de la recherche A* avec l'heuristique de Manhattan Distance
print (initial.a_star(goal, h, output))
temps_exec = time.time() - start_time
print("\nL'Heuristique de manhattan à pris "+str(temps_exec)+" secondes")


# Test de l'heuristique de Tile Switches Remaining
print("\nTest de Tile switch \n")
start_time2 = time.time()


# Utilisation de la recherche A* avec l'heuristique de Tile Switches Remaining
print (initial.a_star(goal, h2, output))
temps_exec2 = time.time() - start_time2
print("\nL'Heuristique de Tile switch à pris "+str(temps_exec2)+" secondes")


# Affichage de la différence de temps d'exécution entre les deux heuristiques
print("\nLa différence de ces 2 heuristiques est de "+str(temps_exec2-temps_exec)+" secondes")



'''
Ce code aide à évaluer quelle heuristique fonctionne le mieux pour résoudre
le puzzle 8-Puzzle en mesurant leur efficacité respective.
L'heuristique de Manhattan s'est révélée plus rapide dans ce test particulier.

'''