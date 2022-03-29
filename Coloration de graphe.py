"""
Coloriage de graphe
"""

"""
Deux sommets voisins dans un graphe ne doivent pas être coloriés de la même couleur, on veut utiliser le moins de couleurs possibles
"""

"""
Quelle stratégie pour utiliser le moins de couleurs possibles ?
"""

"""
Créer un graphe aléatoire de taille n, un nombre d'arête en n^2 style n^2/5...
"""

"""
Fonction qui vérifie qu'un coloriage est correcte
"""

"""
Se débrouiller pour colorier le graphe avec le moins de couleurs possibles
"""

"""
On commence par colorier les sommets de plus haut degré
"""


"""
Importation des bibliothèques nécessaires
"""
from random import randrange

def graphe_aleatoire(n):
    graphe=[[i] for i in range(n)]
    matriceAdjacence=[[0 for i in range(n)] for j in range(n)]
    nbAretes = 0
    while nbAretes < (n**2//5):
        (i,j) = (randrange(n),randrange(n))
        if i != j and matriceAdjacence[i][j] == 0:
            nbAretes += 1
            matriceAdjacence[i][j]=1
            matriceAdjacence[j][i]=1
    return matriceAdjacence

M = graphe_aleatoire(20)

def liste_degrés(matriceAdjacence):
    n=len(matriceAdjacence)
    degrés=[[0,i] for i in range(n)]
    for i in range(n):
        for j in range(n):
            degrés[i][0]+=matriceAdjacence[i][j]
    return degrés

def maximum_tableau_degrés(tableauDegrés):
    candidat = 0
    for k in range(1,len(tableauDegrés)):
        if tableauDegrés[k][0]>tableauDegrés[candidat][0]:
            candidat=k
    return tableauDegrés[candidat]

def tri_degre_décroissant(matriceAdjacence):
    tableauDegrés=liste_degrés(matriceAdjacence)
    def aux(tableauTrie,restants):
        if restants==[]:
            return tableauTrie
        else:
            for i in range(len(restants)):
                restants[i].append(i)
            maximum=maximum_tableau_degrés(restants)
            tableauTrie.append(maximum[1])
            restants.pop(maximum[2])
            for i in range(len(restants)):
                restants[i].pop()
            return aux(tableauTrie,restants)
    tableauTrie=aux([],tableauDegrés)
    return tableauTrie

def liste_voisins(matriceAdjacence,sommet):
    tableau=[]
    for i in range(len(matriceAdjacence)):
        if matriceAdjacence[sommet][i]==1:
            tableau.append(i)
    return tableau
            
def graphe_initial(n):
    return [[i] for i in range(n)]

def coloration_graphe(n):
    matriceAdjacence=graphe_aleatoire(n)
    print(1)
    tableauTrie=tri_degre_décroissant(matriceAdjacence)
    graphe=graphe_initial(n)
    graphe[tableauTrie[0]].append(0)
    for i in range(1,len(tableauTrie)):
        couleursUtilisées=[]
        tableau_voisins=liste_voisins(matriceAdjacence,i)
        for j in tableauTrie[:i]:
            if not(graphe[j][1] in couleursUtilisées) and j in tableau_voisins:
                couleursUtilisées.append(graphe[j][1])
        couleur=0
        print(couleursUtilisées)
        while couleur in couleursUtilisées:
            couleur+=1
        graphe[tableauTrie[i]].append(couleur)
    return graphe
            
            
            
            
            
            
            
            
            
            
            
            
            