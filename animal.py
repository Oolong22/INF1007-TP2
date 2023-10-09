from simulation_constants import MIN_ENERGIE

def creer_animal(age=0, jrs_gestation=0, energie=MIN_ENERGIE, disponible=True):
    animal = {'age': age, 'jrs_gestation': jrs_gestation, 'energie': energie, 'disponible': disponible}
    return animal


def obtenir_age(animal):
    return animal['age']


def obtenir_jours_gestation(animal):
    return animal['jrs_gestation']


def obtenir_energie(animal):
    return animal['energie']


def obtenir_disponibilite(animal):
    return animal['disponible']


def incrementer_age(animal, puberte):
    animal['age'] += 1
    if animal['age'] >= puberte:
        animal['jrs_gestation'] += 1
    else:
        pass


def definir_jours_gestation(animal, jrs_gestation):
    animal['jrs_gestation'] = jrs_gestation


def ajouter_energie(animal, ajout_energie):
    animal['energie'] += ajout_energie


def definir_disponibilite(animal, disponibilite):
    animal['disponible'] = disponibilite