<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Polytechnique_Montr%C3%A9al_logo.jpg" />
</p>

# TP02 : structure de contrôle et de données
- [Directives particulières](#directives)
- [Introduction](#Introduction)
- [Objectifs](#Objectif)
- [Description: La dynamique proie-prédateur](#Description)
- [Déroulement de la simulation](#simulation)
- [Module animal](#animal)
- [Module grille animaux](#animaux)
- [Module simulation](#animaux)
- [Barème](#bareme)
- [Annexe: Guide et normes de codage](#annexe)

:alarm_clock: [Date de remise le dimanche 15 octobre à 23h59](https://www.timeanddate.com/countdown/generic?iso=20231015T235959&p0=165&font=cursive)

## Directives particulières <a name="directives"></a>
* Respecter [guide de codage](https://github.com/INF1007-Gabarits/Guide-codage-python) et les normes pep8;
* Noms de variables et fonctions adéquats (concis, compréhensibles);  
* Pas de librairies externes autres que celles déjà importées;  

## 1. Introduction <a name="Introduction"></a>
<p align='justify'>L'automate cellulaire, capable de calculabilité universelle malgré sa simplicité, est un concept captivant qui a séduit les scientifiques dans divers domaines allant de la biologie à la physique et à l'informatique. Parmi ces modèles, le "Jeu de la Vie", inventé par John Horton Conway en 1970, est particulièrement intrigant. Ce modèle, bien que simple en apparence, il génère une gamme impressionnante de comportements complexes, allant de formes statiques à des structures oscillantes et même des entités mobiles.</p>

<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/7/7a/Gol-gun.gif" alt="Jeu de la Vie" width="500">
</p>
<p align='justify'>Dans cette version adaptée, nous explorerons une dimension supplémentaire de complexité : une dynamique proies-prédateurs. Notre grille de simulation ne se contentera pas d'héberger des cellules "vivantes" ou "mortes", mais aussi des lapins, représentant les proies, et des loups, incarnant les prédateurs. Cette extension ajoute non seulement du réalisme à notre simulation, mais elle nous permet également de comprendre les systèmes dynamiques et les équilibres naturels qui en résultent.</p>

<p align='justify'>Ce laboratoire n'est pas simplement un exercice de programmation : c'est une aventure de découverte. À chaque ligne de code, nous dévoilons un peu plus du mystère des systèmes complexes qui émergent de règles simples. Préparez-vous à plonger dans le monde fascinant des automates cellulaires et des interactions proies-prédateurs, tout en maitrisant les compétences clés en programmation Python.
</p>

## 2. Objectifs: <a name="Objectif"></a>
<p align='justify'> Ce laboratoire vise principalement à:</p>

1.  Maitriser l'utilisation de structures de contrôle 
2.  Maitriser l'utilisation de structures de données complexes en Python, notamment les listes imbriquées et les dictionnaires.
3.  Approfondir la transcription d'algorithmes dans un langage de programmation pour modéliser des phénomènes réels.

## 3. Description: La dynamique proie-prédateur <a name="Description"></a>

<p align='justify'>Bien que le nom "Jeu de la vie" suggère un jeu, il s'agit en réalité d'une simulation. Le socle théorique de notre laboratoire est basé sur le jeu de la vie, un automate cellulaire développé par John H. Conway. Dans cette version enrichie, chaque cellule de notre grille peut accueillir un loup, un lapin ou rester vide. L'état de chaque cellule évolue en fonction de ses voisines, créant une danse dynamique entre les proies et les prédateurs.</p>

Pour ceux désireux d'approfondir leurs connaissances, nous recommandons de consulter la page [Wikipedia du Jeu de la Vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie) et [les équations de Lotka-Volterra](https://fr.wikipedia.org/wiki/%C3%89quations_de_Lotka-Volterra) qui offrent un aperçu mathématique de la dynamique proie-prédateur.


## 4. Déroulement de la simulation :<a name="simulation"></a>
<p align='justify'>La première étape dans la réalisation de notre simulation est la configuration initiale de la grille. Vous devrez définir un pourcentage de "remplissage" de la grille avec des loups et des lapins. Par exemple, si 30% de la grille est occupée, parmi ces occupants, 60% pourraient être des lapins et 40% des loups. </p>

<p align='justify'>Ensuite, chaque itération de notre simulation (un tour de boucle) évoluera en examinant l'état de chaque cellule en fonction de ses voisins immédiats. Par exemple, si un loup est adjacent à un lapin, il le consommera et gagnera de l'énergie. En dehors de ces interactions prédateur-proie, la simulation gère d'autres facteurs vitaux tels que le mouvement, la reproduction et la mortalité. Pour visualiser ces interactions, envisagez de consulter des schémas ou des simulations similaires en ligne.</p>

## 5. Module animal <a name="animale"></a>

<p align='justify'>Pour la simulation, nous devons connaître l'âge de l'animal, une mesure de son énergie restante (un prédateur qui ne se nourrit pas perd de l'énergie), la durée de la gestation (exprimée en jours, où un jour correspond à un cycle de simulation), ainsi qu'une valeur booléenne indiquant s'il est apte à se déplacer.</p>

<p align='justify'>Le champ « .disponible » nous indique si l'animal a déjà été déplacé durant le cycle en cours. En réalité, les animaux se déplacent simultanément, mais dans une simulation basée sur une grille, comme celle que nous prévoyons d'implémenter, le parcours se fait soit de haut en bas et de gauche à droite, soit le contraire. Cette approche supprime l'effet de simultanéité. Ainsi, il est possible de déplacer un animal et de le retrouver plus loin lors du parcours de la grille. C'est pourquoi, après avoir déplacé un animal, nous assignons la valeur `False` à cette propriété. De cette manière, nous nous assurons de déplacer uniquement les animaux qui sont disponibles pour le faire, c'est-à-dire ceux qui n'ont pas encore été déplacés lors du cycle en cours. À la fin de chaque cycle, tous les animaux redeviennent disponibles.</p>

<p align='justify'>Ce module offre des fonctions permettant l'accès en lecture et en écriture aux attributs d'une variable de type "animal" passée en paramètre. </p>

### 5.1. creer_animal
Cette fonction permet de créer un nouvel animal avec des propriétés spécifiques.
- **Entrée** : 
  - age (int, défaut=0): L'âge de l'animal en jours/jours de simulation.
  - jrs_gestation (int, défaut=0):  Si l'animal est en gestation, c'est le nombre de jours depuis le début de la gestation.
  - energie (int, défaut=MIN_ENERGIE): Le niveau d'énergie actuel de l'animal. Cela peut déterminer la capacité de l'animal à se déplacer, à chasser, à fuir, etc.
  - disponible (bool, défaut=True): Un booléen indiquant si l'animal est disponible au déplacement.
- **Sortie** :
  - un dictionnaire représentant l'animal
- **Exemple** :
  ```python
  creer_animal(5, 3, 20, True)
   ```
  Sortie attendue : 
  ```python
  {"age": 5, "jrs_gestation": 3, "energie": 20, "disponible": True}
  ```

### 5.2. obtenir_age
Cette fonction récupère l'âge d'un animal donné.
- **Entrée** : 
  - animal(dict): un dictionnaire représentant l'animal
- **Sortie** :
  - L'âge de l'animal
- **Exemple** :
  ```python
  animal = creer_animal(5, 3, 20, True)
  print(obtenir_age(animal))
   ```
  Sortie attendue : 
  ```python
  5
  ```


### 5.3. obtenir_jours_gestation
Cette fonction est utilisée pour obtenir les jours de gestation d'un animal donné.
- **Entrée** : 
  - animal(dict): un dictionnaire représentant l'animal
- **Sortie** :
  - Le nombre de jours depuis le début de la gestation
- **Exemple** :
  ```python
  animal = creer_animal(5, 3, 20, True)
  print(obtenir_jours_gestation(animal))
   ```
  Sortie attendue : 
  ```python
  3
  ```

### 5.4. obtenir_energie
Cette fonction permet de récupérer le niveau d'énergie actuel d'un animal.
- **Entrée** : 
  - animal(dict): un dictionnaire représentant l'animal
- **Sortie** :
  - Le niveau d'énergie actuel de l'animal
- **Exemple** :
  ```python
  animal = creer_animal(5, 3, 20, True)
  print(obtenir_energie(animal))
   ```
  Sortie attendue : 
  ```python
  20
  ```

### 5.5. obtenir_disponibilite
Cette fonction renvoie le statut de disponibilité de l'animal au déplacement.
- **Entrée** : 
  - animal(dict): un dictionnaire représentant l'animal
- **Sortie** :
  - Le statut de disponibilité  de l'animal
- **Exemple** :
  ```python
  animal = creer_animal(5, 3, 20, True)
  print(obtenir_disponibilite(animal))
   ```
  Sortie attendue : 
  ```python
  True
  ```

### 5.6. incrementer_age
Cette fonction est utilisée pour augmenter l'âge de l'animal d'une unité. Si l'animal a atteint l'âge de la puberté, ses jours de gestation augmentent également.
- **Entrée** : 
  - animal(dict): un dictionnaire représentant l'animal
  - puberte(int): l'âge de puberté
- **Exemple** :
  ```python
  animal = creer_animal(5, 3, 20, True)
  incrementer_age(animal, 6)
   ```
  Sortie attendue : 
  ```python
  {"age": 6, "jrs_gestation": 4, "energie": 20, "disponible": True}
  ```

### 5.7. definir_jours_gestation
Cette fonction permet de définir les jours de gestation d'un animal. Elle serait principalement utilisée pour suivre combien de jours il reste avant que l'animal ne donne naissance.
- **Entrée** : 
  - animal(dict, défaut=None): un dictionnaire représentant l'animal
  - jours (int) : Le nombre de jours à définir pour la gestation de l'animal.
- **Exemple** :
  ```python
  animal = creer_animal(5, 50, 20, True)
  definir_jours_gestation(animal, 40)
   ```
  Sortie attendue : 
  ```python
  {"age": 6, "jrs_gestation": 40, "energie": 20, "disponible": True}
  ```

### 5.8. ajouter_energie
Elle sert à augmenter la quantité d'énergie de l'animal d'une quantité spécifiée, simulant par exemple le fait qu'un animal ait mangé.
- **Entrée** : 
  - animal(dict, défaut=None): un dictionnaire représentant l'animal
  - quantite (int) : La quantité d'énergie à ajouter à l'animal.
- **Exemple** :
  ```python
  animal = creer_animal(5, 50, 20, True)
  ajouter_energie(animal, 20)
   ```
  Sortie attendue : 
  ```python
  {"age": 6, "jrs_gestation": 50, "energie": 40, "disponible": True}
  ```

### 5.9. definir_disponibilite
Cette fonction permet de définir si un animal est disponible au déplacement ou non.
- **Entrée** : 
  - animal(dict, défaut=None): un dictionnaire représentant l'animal
  - disponibilite (bool) : La disponibilité à définir pour l'animal (True signifie qu'il est disponible, False qu'il ne l'est pas). 
- **Exemple** :
  ```python
  animal = creer_animal(5, 50, 20, True)
  definir_disponibilite(animal, False)
   ```
  Sortie attendue : 
  ```python
  {"age": 6, "jrs_gestation": 50, "energie": 20, "disponible": False}
  ```

## 6. Module grille animaux <a name="animaux"></a>
<p align='justify'>Pour représenter l'environnement, nous utilisons une liste de listes, simulant un tableau à deux dimensions, où chaque case peut accueillir un animal. Chaque case possède également un état (ou contenu) permettant d'identifier l'espèce de l'animal qui s'y trouve, ou d'indiquer si elle est vide. Il est essentiel de connaître les dimensions de la grille (en termes de largeur et de longueur en cases) ainsi que le nombre de proies et de prédateurs présents dans celle-ci.</p>

### 6.1. creer_case
Cette fonction crée une nouvelle case (comme dans une grille) avec un état spécifique (p.ex. si la case contient une proie, un prédateur ou est vide) et éventuellement un animal.
- **Entrée** : 
  - animal(dict, défaut=None): un dictionnaire représentant l'animal
  - etat(Contenu): L'état de la case (proie, prédateur ou vide).
- **Sortie** :
  - un dictionnaire représentant la case
- **Exemple** :
  ```python
  animal = creer_animal(5, 3, 20, True)
  creer_case(Contenu.PROIE, animal)
   ```
  Sortie attendue : 
  ```python
  {"etat": Contenu.PROIE, "animal": {"age": 5, "jrs_gestation": 3, "energie": 20, "disponible": True}}
  ```

### 6.2. creer_grille
Cette fonction crée une nouvelle grille avec des dimensions spécifiées et remplit chaque case avec l'état VIDE.  
- **Entrée** : 
  - nb_ligne(int): Nombre de lignes de la grille.
  - nb_colonnes(int): Nombre de colonnes de la grille.
- **Sortie** :
  - Une structure représentant la grille.
- **Exemple** :
  ```python
  nb_lignes = 2
  nb_colonnes = 2
  grille = creer_grille(nb_lignes, nb_colonnes)
   ```
  Sortie attendue : 
  ```python
  grille = {"matrice": [[{"etat": Contenu.VIDE, "animal": None}, {"etat": Contenu.VIDE, "animal": None}],
                        [{"etat": Contenu.VIDE, "animal": None}, {"etat": Contenu.VIDE, "animal": None}]],
            "nb_proies": 0,
            "nb_predateurs": 0,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  ```

### 6.3. obtenir_case
Cette fonction récupère une case spécifique dans une grille.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
  - ligne(int): L'index de la ligne de la grille.
  - colonne(int): L'index de la colonne de la grille.
- **Sortie** :
  - La case à  la position
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.PROIE, "animal": {"age": 1, "jrs_gestation": 0, "energie": 50, "disponible": True}}
  case_12 = {"etat": Contenu.VIDE, "animal": None}
  case_21 = {"etat": Contenu.VIDE, "animal": None}
  case_22 = {"etat": Contenu.PREDATEUR, "animal": {"age": 2, "jrs_gestation": 0, "energie": 40, "disponible": False}}
  
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  case = obtenir_case(grille, 0, 0)
  ```
  Sortie attendue : 
  ```python
  case = {"etat": Contenu.PROIE, "animal": {"age": 1, "jrs_gestation": 0, "energie": 50, "disponible": True}
  ```



### 6.4. obtenir_etat
Cette fonction renvoie l'état d'une case donnée (par exemple, si la case est vide ou contient une proie).
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
  - ligne(int): L'index de la ligne de la grille.
  - colonne(int): L'index de la colonne de la grille.
- **Sortie** :
  - Contenu (l'état de la case, p.ex. Contenu.VIDE, Contenu.PROIE, ...)
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.PROIE, "animal": {"age": 1, "jrs_gestation": 0, "energie": 50, "disponible": True}}
  case_12 = {"etat": Contenu.VIDE, "animal": None}
  case_21 = {"etat": Contenu.VIDE, "animal": None}
  case_22 = {"etat": Contenu.PREDATEUR, "animal": {"age": 2, "jrs_gestation": 0, "energie": 40, "disponible": False}}
  
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  etat = obtenir_etat(grille, 0, 0)
   ```
  Sortie attendue : 
  ```python
  Contenu.PROIE
  ```



### 6.5. obtenir_animal
Cette fonction permet de récupérer l'animal présent dans une case donnée.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
  - ligne(int): L'index de la ligne de la grille.
  - colonne(int): L'index de la colonne de la grille.
- **Sortie** :
  - L'animal dans la case
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.PROIE, "animal": {"age": 1, "jrs_gestation": 0, "energie": 50, "disponible": True}}
  case_12 = {"etat": Contenu.VIDE, "animal": None}
  case_21 = {"etat": Contenu.VIDE, "animal": None}
  case_22 = {"etat": Contenu.PREDATEUR, "animal": {"age": 2, "jrs_gestation": 0, "energie": 40, "disponible": False}}
  
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  animal = obtenir_animal(grille, 0, 0)
   ```
  Sortie attendue : 
  ```python
  {"age": 1, "jrs_gestation": 0, "energie": 50, "disponible": True}
  ```


### 6.6. definir_animal
Cette fonction est utilisée pour définir ou remplacer l'animal présent dans une case donnée.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
  - ligne(int): L'index de la ligne de la grille.
  - colonne(int): L'index de la colonne de la grille.
  - animal (dict): un dictionnaire représentant un animal
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.PROIE, "animal": {"age": 1, "jrs_gestation": 0, "energie": 50, "disponible": True}}
  case_12 = {"etat": Contenu.VIDE, "animal": None}
  case_21 = {"etat": Contenu.VIDE, "animal": None}
  case_22 = {"etat": Contenu.PREDATEUR, "animal": {"age": 2, "jrs_gestation": 0, "energie": 40, "disponible": False}}
  
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  definir_animal(grille, creer_animal(1, 0, 50, True), 0, 1)
   ```
  Sortie attendue : 
  ```python
  grille = {"matrice": [[{"etat": Contenu.PROIE, "animal": {"age": 5, "jrs_gestation": 3, "energie": 20, "disponible": True}}, 
                       {"etat": Contenu.VIDE, "animal": {"age": 5, "jrs_gestation": 3, "energie": 20, "disponible": True}}],
                      [{"etat": Contenu.VIDE, "animal": None}, 
                       {"etat": Contenu.PREDATEUR, "animal": {"age": 2, "jrs_gestation": 0, "energie": 40, "disponible": False}}]],
          "nb_proies": 1,
          "nb_predateurs": 1,
          "nb_lignes": 2,
          "nb_colonnes": 2}
  ```


  

### 6.7. definir_case
Cette fonction met à jour l'état de la case située à la ligne et la colonne données.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
  - etat(CONTENUE): L'état à mettre à jour (proie, prédateur ou vide).
  - ligne(int): L'index de la ligne de la grille.
  - colonne(int): L'index de la colonne de la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PREDATEUR, "animal": creer_animal()}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  definir_case(grille, Contenu.PREDATEUR, 0, 1)
   ```
  Sortie attendue : 
  ```python
  grille = {"matrice": [[case_11, {"etat": Contenu.PREDATEUR, "animal": creer_animal()}],
                        [case_21, case_22]],
            "nb_proies": 0,
            "nb_predateurs": 2,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  ```
  
### 6.8. vider_case
Cette fonction Écraser la case située à la ligne et la colonne données avec une case vide
- **Entrée** :
  - grille(dict): Une structure représentant la grille.
  - ligne(int): L'index de la ligne de la grille.
  - colonne(int): L'index de la colonne de la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PREDATEUR, "animal": creer_animal()}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  grille = {"matrice": [[case_11, {"etat": Contenu.PREDATEUR, "animal": creer_animal()}],
                        [case_21, case_22]],
            "nb_proies": 0,
            "nb_predateurs": 2,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  vider_case(grille, 0, 1)
   ```
  Sortie attendue : 
  ```python
  grille = {"matrice": [[case_11, {"etat": Contenu.VIDE, "animal": None}],
                        [case_21, case_22]],
            "nb_proies": 0,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}

  ```
  
### 6.9. obtenir_population
Cette fonction récupère le nombre de proies et de prédateurs dans une grille.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
- **Sortie** :
  - Le nombre de proies et de prédateurs dans cette ordre
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PREDATEUR, "animal": creer_animal()}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  obtenir_population(grille)
   ```
  Sortie attendue : 
  ```python
  (1, 1)
  ```
  
### 6.10. obtenir_dimensions
Cette fonction récupère les dimensions de la grille.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
- **Sortie** :
  - Les dimensions de la grille ligne et colonne
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PREDATEUR, "animal": creer_animal()}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  obtenir_dimensions(grille)
   ```
  Sortie attendue : 
  ```python
  (2, 2)
  ```
  
### 6.11. incrementer_nb_proies
Cette fonction incrémente le nombre de proies dans la grille.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PREDATEUR, "animal": creer_animal()}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  incrementer_nb_proies(grille)
   ```
  Sortie attendue : 
  ```python
  grille["nb_proies"] = 2
  ```
  
### 6.12. decrementer_nb_proies
Cette fonction décrémente le nombre de proies dans la grille.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_22 = {"etat": Contenu.PREDATEUR, "animal": None}
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 2,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  decrementer_nb_proies(grille)
   ```
  Sortie attendue : 
  ```python
  grille["nb_proies"] = 1
  ```
  
### 6.13. incrementer_nb_predateurs
Cette fonction incrémente le nombre de prédateurs dans la grille.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PREDATEUR, "animal": creer_animal()}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  incrementer_nb_predateurs(grille)
   ```
  Sortie attendue : 
  ```python
  grille["nb_predateurs"] = 2
  ```
  

### 6.14. decrementer_nb_predateurs
Cette fonction décrémente le nombre de prédateurs dans la grille.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PREDATEUR, "animal": creer_animal()}
  case_22 = {"etat": Contenu.PREDATEUR, "animal": None}
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 2,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  decrementer_nb_predateurs(grille)
   ```
  Sortie attendue : 
  ```python
  grille["nb_predateurs"] = 1
  ```
  

### 6.15. check_nb_proies
Cette fonction vérifie si le nombre actuel de proies dans la grille est inférieur à max_val 
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
- **Sortie** :
  - Un booléen pour vérifier si le nombre actuel de proies dans la grille est inférieur à max_val 
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PREDATEUR, "animal": creer_animal()}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 5,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  max_val = 10
  check_nb_proies(grille, max_val) 
   ```
  Sortie attendue : 
  ```python
  True
  ```
  


### 6.16. ajuster_position_pour_grille_circulaire
Cette fonction ajuste les coordonnées de position (lig, col) en utilisant les dimensions dim_lig et dim_col de la grille pour s'assurer que les lapins ou les loups ne sortent pas de la grille, mais plutôt réapparaissent de l'autre côté, créant ainsi un effet de "bouclage".
- **Entrée** : 
  - lig(int): Ligne actuelle.
  - col(int): Colonne actuelle.
  - dim_lig(int): Nombre total de lignes dans la grille.
  - dim_col(int): Nombre total de colonnes dans la grille.
- **Sortie** :
  - La nouvelle position
- **Exemple** :
  ```python
  lig = -1
  col = 3
  dim_lig = 2
  dim_col = 2
  lig, col= ajuster_position_pour_grille_circulaire(lig, col, dim_lig, dim_col)
  ```
  Sortie attendue : 
  ```python
  lig = 1
  col = 1
  ```
  


### 6.17. choix_voisin_autour
Cette fonction cherche tous les voisins autour de la cellule (ligne, col) qui correspondent au "contenu" donné.
<p align="center">
    <img src="assets/Algo_1.svg" alt="choix_voisin_autour">
</p>

- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
  - etat(CONTENUE): L'état à mettre à jour (proie, prédateur ou vide).
  - ligne(int): L'index de la ligne de la grille.
  - colonne(int): L'index de la colonne de la grille.
- **Sortie** :
  - Le nombre total des voisins, ainsi que les coordonnées d'un voisin choisi aléatoirement.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PREDATEUR, "animal": creer_animal()}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  ligne = 1
  colonne = 1
  etat = Contenu.PROIE
  nb_voisin, coordonnees = choix_voisin_autour(grille, ligne, colonne, etat)
   ```
  Sortie attendue : 
  ```python
  nb_voisin = 1
  coordonnees = [0, 1]
  ```
  


### 6.18. remplir_grille
Cette fonction cherche tous les voisins autour de la cellule (ligne, col) qui correspondent au "contenu" donné.
<p align="center">
    <img src="assets/Algo_2.svg" alt="remplir_grille">
</p>


- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
  - pourcentage_proie(float): Le pourcentage de proies à remplir dans la grille.
  - pourcentage_predateur(float): Le pourcentage de prédateurs à remplir dans la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.PREDATEUR, "animal": creer_animal()}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  pourcentage_proie = 0.5
  pourcentage_predateur = 0.5
  remplir_grille(grille, pourcentage_proie, pourcentage_predateur)
  ```
  Sortie attendue : 
  ```python
  grille["nb_proies"] = 2
  grille["nb_predateurs"] = 2
  ```
  


## 7. Module simulation <a name="simulation"></a>
### 7.1. rendre_animaux_disponibles
Cette fonction parcourir chaque case de la grille et rendre tous les animaux disponibles pour la prochaine itération.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.PROIE, "animal": {"age": 1, "jrs_gestation": 0, "energie": 5, "disponible": False}}
  case_12 = {"etat": Contenu.PREDATEUR, "animal": {"age": 2, "jrs_gestation": 1, "energie": 4, "disponible": False}}
  case_21 = {"etat": Contenu.VIDE, "animal": None}
  case_22 = {"etat": Contenu.PROIE, "animal": {"age": 0, "jrs_gestation": 0, "energie": 6, "disponible": False}}
  
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 2,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  
  rendre_animaux_disponibles(grille)
  ```
  Sortie attendue : 
  ```python
  case_11["animal"]["disponible"] = True
  case_12["animal"]["disponible"] = True
  case_22["animal"]["disponible"] = True
  ```
  

### 7.2. deplacer_animal
Cette fonction cherche un emplacement vide où déplacer l'animal, effectuer le déplacement et mettre à jour l'état et la disponibilité de l'animal.
- **Entrée** : 
   - grille(dict): Une structure représentant la grille.
  - animal (dict): un dictionnaire représentant un animal
  - ligne(int): L'index de la ligne de la grille.
  - colonne(int): L'index de la colonne de la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.PROIE, "animal": {"age": 2, "jrs_gestation": 0, "energie": 8, "disponible": True}}
  case_12 = {"etat": Contenu.VIDE, "animal": None}
  case_21 = {"etat": Contenu.VIDE, "animal": None}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 0,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  
  ligne = 0
  colonne = 0
  animal = case_11["animal"]
  
  deplacer_animal(grille, ligne, colonne, animal)
  ```
  Sortie attendue : 
  ```python
  grille["matrice"][0][0]["etat"] = Contenu.VIDE
  grille["matrice"][0][0]["animal"] = None
  
  # Une des cellules voisines, par exemple:
  grille["matrice"][0][1]["etat"] = Contenu.PROIE
  grille["matrice"][0][1]["animal"] = {"age": 2, "jrs_gestation": 0, "energie": 8, "disponible": False}
  ```
  
### 7.3. executer_cycle_proie
Cette fonction gère le cycle de vie d'une proie à une position donnée sur la grille.
  1. Vieillir l'animal. Si l'âge dépasse MAX_AGE_PROIE, le retirer de la grille et décrémenter le compteur de proies.
  2. Si l'animal est en âge de se reproduire et a attendu suffisamment (NB_JRS_GESTATION_PROIE), tenter de générer un nouveau bébé proie. Pour ce faire, chercher un voisin vide autour de la proie. Si un voisin est trouvé, créer un bébé proie et le placer dans la grille.
  3. Sinon, déplacer l'animal vers une case vide à proximité.
     
<p align="center">
    <img src="assets/Algo_3.svg" alt="remplir_grille">
</p>

- **Entrée** : 
   - grille(dict): Une structure représentant la grille.
  - animal (dict): un dictionnaire représentant un animal
  - ligne(int): L'index de la ligne de la grille.
  - colonne(int): L'index de la colonne de la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": {"age": 3, "jrs_gestation": 2, "energie": 10, "disponible": True}}
  case_21 = {"etat": Contenu.VIDE, "animal": None}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  
  grille = {"matrice": [[case_11, case_12], 
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 0,
            "nb_lignes": 2,
            "nb_colonnes": 2
  }
  executer_cycle_proie(grille, 0, 1, case_12["animal"])

   ```
  Sortie attendue : 
  ```python
  # On s'attend à ce que la proie se reproduise et place son bébé dans une case voisine, par exemple case_11.
  case_11["etat"] = Contenu.PROIE
  case_11["animal"] = {"age": 0, "jrs_gestation": 0, "energie": 10, "disponible": False}
  grille["nb_proies"] = 2
  ```
  


### 7.4. executer_cycle_predateur 
Cette fonction gère le cycle de vie d'un prédateur à une position donnée sur la grille.
  1. Vieillir l'animal. Si l'âge dépasse MAX_AGE_PRED ou si le prédateur manque d'énergie (énergie < MIN_ENERGIE), le retirer de la grille et décrémenter le compteur de prédateurs.
  2. Si le prédateur peut manger une proie dans une case voisine, le faire en le déplaçant dans la case de la proie et en incrémentant son énergie de AJOUT_ENERGIE (n'oubliez pas de décrémenter le compteur de proies). Après avoir mangé, si le prédateur est en âge de se reproduire et a attendu suffisamment (NB_JRS_GESTATION_PRED), tenter de générer un nouveau bébé prédateur. Pour ce faire, chercher un voisin vide autour du prédateur. Si un voisin est trouvé, créer un bébé prédateur et le placer dans la grille.
  3. Sinon, déplacer l'animal vers une case vide à proximité et décrémenter son énergie de 1.
     
<p align="center">
    <img src="assets/Algo_4.svg" alt="remplir_grille">
</p>

- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
  - animal (dict): un dictionnaire représentant un animal
  - ligne(int): L'index de la ligne de la grille.
  - colonne(int): L'index de la colonne de la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": creer_animal()}
  case_21 = {"etat": Contenu.VIDE, "animal": None}
  case_22 = {"etat": Contenu.PREDATEUR, "animal": creer_animal(age=NB_JRS_PUBERTE_PRED + 1, energie=2, jrs_gestation=NB_JRS_GESTATION_PRED + 1)}
  
  grille = {"matrice": [[case_11, case_12],
                        [case_21, case_22]],
            "nb_proies": 1,
            "nb_predateurs": 1,
            "nb_lignes": 2,
            "nb_colonnes": 2}
  
  ligne = 1
  colonne = 1
  animal = grille["matrice"][ligne][colonne]["animal"]
  
  executer_cycle_predateur(grille, ligne, colonne, animal)

   ```
  Sortie attendue : 
  ```python
  grille["matrice"][0][1] == {"etat": Contenu.PREDATEUR, "animal": ...}  # Prédateur ayant mangé la proie
  grille["matrice"][1][1] == {"etat": Contenu.PREDATEUR, "animal": ...}  # Nouveau prédateur né
  grille["nb_proies"] == 0
  grille["nb_predateurs"] == 2
  ```
  


### 7.5. executer_cycle
Cette fonction est une fonction d'orchestration qui parcourt l'ensemble de la grille et exécute le cycle de vie approprié pour chaque animal (proie ou prédateur) présent sur la grille. Elle commence par rendre tous les animaux "disponibles" pour des actions comme le déplacement ou la reproduction, puis itère sur chaque cellule de la grille pour appeler soit executer_cycle_proie soit executer_cycle_predateur en fonction de l'animal occupant la cellule.
<p align="center">
    <img src="assets/Algo_5.svg" alt="remplir_grille">
</p>

- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
- **Exemple** :
  ```python
  case_11 = {"etat": Contenu.VIDE, "animal": None}
  case_12 = {"etat": Contenu.PROIE, "animal": {"age": 1, "jrs_gestation": 0, "energie": 10, "disponible": False}}
  case_13 = {"etat": Contenu.VIDE, "animal": None}
  case_14 = {"etat": Contenu.PREDATEUR, "animal": {"age": 3, "jrs_gestation": 1, "energie": 7, "disponible": False}}
  
  case_21 = {"etat": Contenu.PREDATEUR, "animal": {"age": 2, "jrs_gestation": 1, "energie": 8, "disponible": False}}
  case_22 = {"etat": Contenu.VIDE, "animal": None}
  case_23 = {"etat": Contenu.PROIE, "animal": {"age": 1, "jrs_gestation": 0, "energie": 9, "disponible": False}}
  case_24 = {"etat": Contenu.VIDE, "animal": None}
  
  case_31 = {"etat": Contenu.PROIE, "animal": {"age": 0, "jrs_gestation": 0, "energie": 10, "disponible": False}}
  case_32 = {"etat": Contenu.VIDE, "animal": None}
  case_33 = {"etat": Contenu.VIDE, "animal": None}
  case_34 = {"etat": Contenu.PREDATEUR, "animal": {"age": 1, "jrs_gestation": 0, "energie": 5, "disponible": False}}
  
  case_41 = {"etat": Contenu.VIDE, "animal": None}
  case_42 = {"etat": Contenu.PROIE, "animal": {"age": 0, "jrs_gestation": 0, "energie": 10, "disponible": False}}
  case_43 = {"etat": Contenu.PREDATEUR, "animal": {"age": 4, "jrs_gestation": 2, "energie": 6, "disponible": False}}
  case_44 = {"etat": Contenu.VIDE, "animal": None}
  
  grille = {"matrice": [[case_11, case_12, case_13, case_14],
                        [case_21, case_22, case_23, case_24],
                        [case_31, case_32, case_33, case_34],
                        [case_41, case_42, case_43, case_44]],
          "nb_proies": 4,
          "nb_predateurs": 4,
          "nb_lignes": 4,
          "nb_colonnes": 4}
  
  executer_cycle(grille)
   ```
  Sortie attendue : 
  ```python
  grille = {"matrice": [[{"etat": Contenu.VIDE, "animal": None}, {"etat": Contenu.VIDE, "animal": None}, 
                         {"etat": Contenu.VIDE, "animal": None}, {"etat": Contenu.PREDATEUR, "animal": {"age": 4, "jrs_gestation": 2, "energie": 6, "disponible": False}}],
                        [{"etat": Contenu.VIDE, "animal": None}, {"etat": Contenu.VIDE, "animal": None}, 
                         {"etat": Contenu.PROIE, "animal": {"age": 2, "jrs_gestation": 0, "energie": 8, "disponible": False}}, {"etat": Contenu.VIDE, "animal": None}],
                        [{"etat": Contenu.VIDE, "animal": None}, {"etat": Contenu.VIDE, "animal": None}, 
                         {"etat": Contenu.VIDE, "animal": None}, {"etat": Contenu.PREDATEUR, "animal": {"age": 2, "jrs_gestation": 1, "energie": 4, "disponible": False}}],
                        [{"etat": Contenu.VIDE, "animal": None}, {"etat": Contenu.VIDE, "animal": None}, 
                         {"etat": Contenu.PREDATEUR, "animal": {"age": 5, "jrs_gestation": 3, "energie": 5, "disponible": False}}, {"etat": Contenu.VIDE, "animal": None}]],
        "nb_proies": 1,
        "nb_predateurs": 3,
        "nb_lignes": 4,
        "nb_colonnes": 4}
  ```


### 7.6. simulation_est_terminee
Cette fonction vérifie si une simulation est terminée. La simulation est considérée comme terminée si toutes les proies ou tous les prédateurs ont été éliminés de la grille. La fonction retourne True dans ce cas, et False sinon.
- **Entrée** : 
  - grille(dict): Une structure représentant la grille.
- **Sortie** :
  - Un booléen pour vérifier si la simulation est terminée.

- **Exemple** :
  ```python
  grille = creer_grille(2, 2)
  incrementer_nb_proies(grille)
  print(simulation_est_terminee(grille))
  ```

  Sortie attendue : 
  ```python
  True
  ```

## 8. Barème /100 <a name="bareme"></a>

|**Nom des fonctions**|**Nombre de points attribuer**|
| :- | :- |
|creer_animal                              | 2  |
|obtenir_age                               | 1  |
|obtenir_jours_gestation                   | 1  |
|obtenir_energie                           | 1  |
|obtenir_disponibilite                     | 1  |
|incrementer_age                           | 2  |
|definir_jours_gestation                   | 1  |
|ajouter_energie                           | 1  |
|definir_disponibilite                     | 1  |
|creer_case                                | 2  |
|creer_grille                              | 4  |
|obtenir_case                              | 1  |
|obtenir_etat                              | 1  |
|obtenir_animal                            | 1  |
|definir_animal                            | 1  |
|definir_case                              | 1  |
|vider_case                                | 1  |
|obtenir_population                        | 1  |
|obtenir_dimensions                        | 1  |
|incrementer_nb_proies                     | 1  |
|decrementer_nb_proies                     | 1  |
|incrementer_nb_predateurs                 | 1  |
|decrementer_nb_predateurs                 | 1  |
|check_nb_proies                           | 1  |
|ajuster_position_pour_grille_circulaire   | 1  |
|choix_voisin_autour                       | 8  |
|remplir_grille                            | 10 |
|rendre_animaux_disponibles                | 8  |
|deplacer_animal                           | 8  |
|executer_cycle_proie                      | 12 |
|executer_cycle_predateur                  | 14 |
|executer_cycle                            | 8  |
|simulation_est_terminee                   | 1  |

## Annexe: Guide et normes de codage <a name="annexe"></a>
- [Le guide maison](https://github.com/INF1007-Gabarits/Guide-codage-python) de normes supplémentaires à respecter
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. 
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)

