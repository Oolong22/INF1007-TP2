from enum import Enum
import random

from simulation_constants import *
from animal import *


class Contenu(Enum):
    VIDE = 0
    PROIE = 1
    PREDATEUR = 2


def creer_case(etat=Contenu.VIDE, animal=None):
    case = {'etat': etat, 'animal': animal}
    return case

def definir_case(grille, case, ligne, col):
    grille['matrice'][ligne][col] = case
    return grille

def creer_grille(nb_lignes, nb_colonnes):
    grille = {'matrice': [list({'etat': Contenu.VIDE, 'animal': None} for n in range(0, nb_colonnes)) for m in range(0, nb_lignes)], 
            "nb_proies": 0,
            "nb_predateurs": 0,
            "nb_lignes": nb_lignes,
            "nb_colonnes": nb_colonnes
              }

    return grille


def obtenir_population(grille):
    return (grille['nb_proies'], grille['nb_predateurs'])


def obtenir_dimensions(grille):
    return (len(grille['matrice']), len(grille['matrice'][0]))


def obtenir_animal(grille, ligne, col):
    animal = grille['matrice'][ligne][col]['animal']
    return animal


def incrementer_nb_proies(grille):
    grille['nb_proies'] += 1
    return grille


def decrementer_nb_proies(grille):
    grille['nb_proies'] -= (1 if grille['nb_proies'] > 0 else +0)
    return grille


def incrementer_nb_predateurs(grille):
    grille['nb_predateurs'] += 1
    return grille

def decrementer_nb_predateurs(grille):
    grille['nb_predateurs'] -= (1 if grille['nb_predateurs'] > 0 else +0)
    return grille


def check_nb_proies(grille, max_val):
    if grille['nb_proies'] >= max_val:
        return False
    else:
        return True

def obtenir_case(grille, ligne, colonne):
    # TODO: 
    case = grille['matrice'][ligne][colonne]
    return case

def vider_case(grille, ligne, col):
    case_vide = {'etat': Contenu.VIDE, 'animal': None}
    grille['matrice'][ligne][col] = case_vide
    return grille


def definit_etat(grille, etat, ligne, col):
    grille['matrice'][ligne][col]['etat'] = etat
    return grille
    


def definir_animal(grille, animal, ligne, col):
    grille['matrice'][ligne][col]['animal'] = animal
    return grille


def obtenir_etat(grille, ligne, colonne):
    etat = grille['matrice'][ligne][colonne]['etat']
    return etat


def generer_entier(min_val, max_val):
    random_number = random.randint(min_val, max_val + 1)
    return random_number


def ajuster_position_pour_grille_circulaire(lig, col, dim_lig, dim_col):
    if lig < 0:
        while lig < 0:
            lig = lig + dim_lig
    elif lig >= dim_lig:
        while lig >= dim_lig:
            lig = lig - dim_lig
    else:
        pass

    if col < 0:
        while col <0:
            col = col + dim_col
    elif col >= dim_col:
        while col >= dim_col:
            col = col - dim_col
    else:
        pass
    return lig, col


def choix_voisin_autour(grille, ligne, col, contenu: Contenu):
    tabcases = []
    lig_voisin = None
    col_voisin = None
    dim_lig, dim_col = obtenir_dimensions(grille)
    for i in range(ligne - 1, ligne + 2): 
        for j in range(col - 1, col + 2):
            if i != ligne or j != col:
                i2, j2 = ajuster_position_pour_grille_circulaire(i, j, dim_lig, dim_col)
                animal = obtenir_animal(grille, i2, j2)
                if grille['matrice'][i2][j2]['etat'] == contenu and grille['matrice'][i2][j2]['animal'] == None:
                    coords = (i2, j2)
                    tabcases.append(coords)
                elif grille['matrice'][i2][j2]['etat'] == contenu and grille['matrice'][i2][j2]['animal']['disponible'] == True:
                    coords = (i2, j2)
                    tabcases.append(coords)
                elif grille['matrice'][i2][j2]['etat'] == contenu and grille['matrice'][i2][j2]['animal']['disponible'] == False:
                    pass
    if tabcases != []:
        lig_voisin, col_voisin = random.choice(tabcases)
        return len(tabcases), lig_voisin, col_voisin
    else:
        return len(tabcases), None, None


def remplir_grille(grille, pourcentage_proie, pourcentage_predateur):
    dim_lig, dim_col = obtenir_dimensions(grille)
    cases_totales = dim_lig * dim_col
    nb_proies = int(cases_totales * float(pourcentage_proie))
    nb_predateurs = int(cases_totales * float(pourcentage_predateur))
    possible_positions = []
    for m in range(0, dim_lig):
        for n in range(0, dim_col):
            coordinates = (m, n)
            possible_positions.append(coordinates)
    random.shuffle(possible_positions)
    if nb_proies > 0:
        for proie in range(0, nb_proies):
            age = generer_entier(0, MAX_AGE_PROIE)
            if age >= NB_JRS_PUBERTE_PROIE:
                    jours_gestation = generer_entier(1, NB_JRS_GESTATION_PROIE)
                    case = creer_case(Contenu.PROIE, creer_animal(age, jours_gestation, MIN_ENERGIE, True))
                    x, y = possible_positions.pop()
                    definir_case(grille, case, x, y)
            incrementer_nb_proies(grille)
    if nb_predateurs > 0:
        for predateur in range(0, nb_predateurs):
            age = generer_entier(1, MAX_AGE_PRED)
            if age >= NB_JRS_PUBERTE_PRED:
                    jours_gestation = generer_entier(0, NB_JRS_GESTATION_PRED)
                    case = creer_case(Contenu.PREDATEUR, creer_animal(age, jours_gestation, MIN_ENERGIE, True))
                    x, y = possible_positions.pop()
                    definir_case(grille, case, x, y)
            incrementer_nb_predateurs(grille)