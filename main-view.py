import pygame

import simulation_logic as logic
from simulation_constants import *
from view_constants import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("INF1007 - TP2")

        self.screen = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))

        self.background_image = pygame.image.load(CHEMIN_IMAGE_FOND)
        self.background_image = pygame.transform.scale(
            self.background_image, (LARGEUR_ECRAN, HAUTEUR_ECRAN)
        ).convert()

        self.font = pygame.font.Font(CHEMIN_POLICE, TAILLE_POLICE)
        self.title_text = self.font.render(TITRE, True, COULEUR_TEXTE)

        self.initialiser_nouvelle_simulation()

    def afficher_statistiques(self):
        nb_lapins, nb_loups = logic.obtenir_population(self.grille)

        lapin_text = self.font.render(
            f'{nb_lapins} Lapin{"s" * (nb_lapins > 1)}', True, COULEUR_TEXTE
        )
        loup_text = self.font.render(
            f'{nb_loups} Loup{"s" * (nb_loups > 1)}', True, COULEUR_TEXTE
        )
        cycle_text = self.font.render(f"Cycle: {self.n_cycles}", True, COULEUR_TEXTE)

        surfaces = [lapin_text, loup_text, cycle_text]

        total_text_width = sum(surface.get_width() for surface in surfaces)
        total_spacing = LARGEUR_ECRAN - total_text_width
        spacing_between = total_spacing // (len(surfaces) + 1)

        x_position = spacing_between

        for surface in surfaces:
            self.screen.blit(surface, (x_position, 95))
            x_position += surface.get_width() + spacing_between

    def obtenir_couleur_case(self, ligne, col):
        if logic.obtenir_etat(self.grille, ligne, col) == logic.Contenu.PROIE:
            age = logic.obtenir_age(logic.obtenir_animal(self.grille, ligne, col))
            return (
                COULEUR_PROIE_AVANT_PUBERTE
                if age < NB_JRS_PUBERTE_PROIE
                else COULEUR_PROIE_APRES_PUBERTE
            )

        elif logic.obtenir_etat(self.grille, ligne, col) == logic.Contenu.PREDATEUR:
            if logic.obtenir_energie(logic.obtenir_animal(self.grille, ligne, col)) < (
                MIN_ENERGIE / 2
            ):
                return COULEUR_PRED_MANQUE_ENERGIE
            else:
                age = logic.obtenir_age(logic.obtenir_animal(self.grille, ligne, col))
                return (
                    COULEUR_PRED_AVANT_PUBERTE
                    if age < NB_JRS_PUBERTE_PRED
                    else COULEUR_PRED_APRES_PUBERTE
                )
        return COULEUR_CASE

    def afficher_grille(self):
        self.screen.blit(self.background_image, (0, 0))

        for ligne in range(NB_LIGNE):
            for col in range(NB_COLONNE):
                x = col * (DIMENSION_CASE + MARGE_CASE) + MARGE_SUPP_LATERALES
                y = ligne * (DIMENSION_CASE + MARGE_CASE) + GRID_Y_INITIAL
                color = self.obtenir_couleur_case(ligne, col)

                pygame.draw.rect(
                    self.screen,
                    COULEUR_BORDURE_CASE,
                    (x, y, DIMENSION_CASE, DIMENSION_CASE),
                    1,
                )
                pygame.draw.rect(
                    self.screen,
                    color,
                    (x + 1, y + 1, DIMENSION_CASE - 2, DIMENSION_CASE - 2),
                )

        self.screen.blit(
            self.title_text, (LARGEUR_ECRAN // 2 - self.title_text.get_width() // 2, 20)
        )

        self.afficher_statistiques()
        pygame.display.flip()

    def initialiser_nouvelle_simulation(self):
        self.grille = logic.creer_grille(NB_LIGNE, NB_COLONNE)
        logic.remplir_grille(self.grille, POURCENTAGE_CASES_PROIES, POURCENTAGE_CASES_PREDATEURS)
        self.n_cycles = 0

    def attendre_bouton_recommencer(self):
        recommencer_text = self.font.render(
            "Appuyez sur R pour recommencer", True, COULEUR_TEXTE
        )
        self.screen.blit(
            recommencer_text,
            (
                LARGEUR_ECRAN // 2 - recommencer_text.get_width() // 2,
                HAUTEUR_ECRAN // 2,
            ),
        )
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    return True

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.afficher_grille()

            if not logic.simulation_est_terminee(self.grille):
                logic.executer_cycle(self.grille)
                self.n_cycles += 1
                pygame.time.wait(DUREE_CYCLE)
            else:
                if self.attendre_bouton_recommencer():
                    self.initialiser_nouvelle_simulation()
                else:
                    running = False


if __name__ == "__main__":
    game = Game()
    game.run()
