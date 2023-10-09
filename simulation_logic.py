from enum import Enum
import random

from simulation_constants import *
from animal import *
from grille_animaux import *

def simulation_est_terminee(grille):
    if grille['nb_proies'] == 0 or grille['nb_predateurs'] == 0:
        return True
    else:
        return False

def rendre_animaux_disponibles(grille):
    # TODO: Parcourir chaque case de la grille et rendre tous les animaux disponibles (Booléen à True) pour la prochaine itération.
    for ligne in grille['matrice']:
        for cellule in ligne:
            if cellule['animal'] is not None:
                cellule['animal']['disponible'] = True
            else:
                pass
    return grille


def deplacer_animal(grille, ligne, col, animal):
    case = obtenir_case(grille, ligne, col)
    nb_voisins, lig_move, col_move = choix_voisin_autour(grille, ligne, col, Contenu.VIDE)
    definir_case(grille, case, lig_move, col_move)
    vider_case(grille, ligne, col)
    definir_disponibilite(animal, False)



def executer_cycle_proie(grille, ligne, col, animal):
    incrementer_age(animal, NB_JRS_PUBERTE_PROIE)
    if obtenir_age(animal) > MAX_AGE_PROIE:
        vider_case(grille, ligne, col)
        decrementer_nb_proies(grille)
    elif obtenir_age(animal) >= NB_JRS_PUBERTE_PROIE and obtenir_jours_gestation(animal) >= NB_JRS_GESTATION_PROIE:
        nb_voisins, lig_voisin, col_voisin = choix_voisin_autour(grille, ligne, col, Contenu.VIDE)
        if lig_voisin is not None and check_nb_proies(grille, NB_MAX_PROIES):
            case = creer_case(Contenu.PROIE, creer_animal())
            definir_case(grille, case, lig_voisin, col_voisin)
            incrementer_nb_proies(grille)
            definir_jours_gestation(animal, 0)
    else:
        nb_voisins, lig_voisin, col_voisin = choix_voisin_autour(grille, ligne, col, Contenu.VIDE)
        if lig_voisin is not None:
            case = obtenir_case(grille, ligne, col)
            definir_case(grille, case, lig_voisin, col_voisin)
            vider_case(grille, ligne, col)
        else:
            pass


def executer_cycle_predateur(grille, ligne, col, animal):
    incrementer_age(animal, NB_JRS_PUBERTE_PRED)
    if obtenir_energie(animal) < MIN_SANTE_PRED or obtenir_age(animal) > MAX_AGE_PRED:
        vider_case(grille, ligne, col)
        decrementer_nb_predateurs(grille)
    
    nb_voisins, lig_voisin, col_voisin = choix_voisin_autour(grille, ligne, col, Contenu.PROIE)
    if lig_voisin is not None:
        definir_disponibilite(animal, False)
        ajouter_energie(animal, AJOUT_ENERGIE)
        case = obtenir_case(grille, ligne, col)
        vider_case(grille, ligne, col)
        definir_case(grille, case, lig_voisin, col_voisin)
        decrementer_nb_proies(grille)
        if obtenir_age(animal) >= NB_JRS_PUBERTE_PRED and obtenir_jours_gestation(animal) >= NB_JRS_GESTATION_PRED:
            definir_jours_gestation(animal, 0)
            nb_voisins, lig_enfant, col_enfant = choix_voisin_autour(grille, ligne, col, Contenu.VIDE)
            if lig_enfant is not None:
                creer_case(Contenu.PREDATEUR, creer_animal())
                definir_case(grille, case, lig_enfant, col_enfant)
                incrementer_nb_predateurs(grille)
    else:
        ajouter_energie(animal, -1)
        nb_voisins, lig_voisin, col_voisin = choix_voisin_autour(grille, ligne, col, Contenu.VIDE)
        if lig_voisin is not None:
            case = obtenir_case(grille, ligne, col)
            vider_case(grille, ligne, col)
            definir_case(grille, case, lig_voisin, col_voisin)
        else:
            pass


def executer_cycle(grille):
    rendre_animaux_disponibles(grille)
    dim_lig, dim_col = obtenir_dimensions(grille)
    for ligne in range(0, dim_lig):
        for col in range(0, dim_col):
            if obtenir_etat(grille, ligne, col) is not Contenu.VIDE:
                animal = obtenir_animal(grille, ligne, col)
                if animal['disponible'] is True:
                    if obtenir_etat(grille, ligne, col) is Contenu.PROIE:
                        executer_cycle_proie(grille, ligne, col, obtenir_animal(grille, ligne, col))
                    elif obtenir_etat(grille, ligne, col) is Contenu.PREDATEUR:
                        executer_cycle_predateur(grille, ligne, col, obtenir_animal(grille, ligne, col))
                    else:
                        pass

