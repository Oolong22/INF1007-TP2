from enum import Enum
import random

from simulation_constants import *
from animal import *
from grille_animaux import *

def simulation_est_terminee(grille):
    # TODO: Vérifier si la simulation est terminée.
    # Elle se termine lorsque le nombre de proies ou le nombre de prédateurs est égal à zéro.
    # Renvoyer un booléen indiquant l'état de la simulation.
    pass


def rendre_animaux_disponibles(grille):
    # TODO: Parcourir chaque case de la grille et rendre tous les animaux disponibles (Booléen à True) pour la prochaine itération.
    pass


def deplacer_animal(grille, ligne, col, animal):
    # TODO: Trouver un voisin vide où déplacer l'animal, effectuer le déplacement et mettre à jour l'état
    # et la disponibilité de l'animal. Utiliser "choix_voisin_autour", "definit_etat", "definir_animal",
    # "definir_disponibilite" et "vider_case" pour réaliser ces étapes.
    pass


def executer_cycle_proie(grille, ligne, col, animal):
    # TODO: Gérer le cycle de vie d'une proie à une position donnée sur la grille.
    # 1. Vieillir l'animal. Si l'âge dépasse MAX_AGE_PROIE, le retirer de la grille et décrémenter le compteur de proies.
    # 2. Si l'animal est en âge de se reproduire et a attendu suffisamment (NB_JRS_GESTATION_PROIE), tenter de générer un nouveau bébé proie.
    #    Pour ce faire, chercher un voisin vide autour de la proie. Si un voisin est trouvé, créer un bébé proie et le placer dans la grille.
    # 3. Sinon, déplacer l'animal vers une case vide à proximité.
    pass


def executer_cycle_predateur(grille, ligne, col, animal):
    # TODO: Gérer le cycle de vie d'un prédateur à une position donnée sur la grille.
    # 1. Vieillir l'animal. Si l'âge dépasse MAX_AGE_PRED ou si le prédateur manque d'énergie (énergie < MIN_ENERGIE), le retirer
    #    de la grille et décrémenter le compteur de prédateurs.
    # 2. Si le prédateur peut manger une proie dans une case voisine, le faire en le déplaçant dans la case de la proie et en
    #    incrémentant son énergie de AJOUT_ENERGIE (n'oubliez pas de décrémenter le compteur de proies). Après avoir mangé, si le
    #    prédateur est en âge de se reproduire et a attendu suffisamment (NB_JRS_GESTATION_PRED), tenter de générer un nouveau bébé
    #    prédateur. Pour ce faire, chercher un voisin vide autour du prédateur. Si un voisin est trouvé, créer un bébé prédateur et
    #    le placer dans la grille.
    # 3. Sinon, déplacer l'animal vers une case vide à proximité et décrémenter son énergie de 1.
    pass


def executer_cycle(grille):
    # TODO: Marquer tous les animaux comme disponibles pour ce cycle, puis parcourir la grille pour exécuter la bonne procédure
    # du cycle de vie pour chaque animal. Il est nécessaires d'utiliser au minimum les fonctions "rendre_animaux_disponibles",
    # "executer_cycle_proie" et "executer_cycle_predateur".
    pass
