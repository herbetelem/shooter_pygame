import pygame
import math

from game import Game
pygame.init()



# generer la fenetre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer et charger le background*
background = pygame.image.load('assets/bg.jpg')

# importer la bannier
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# import charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# import du son
sound_tir = pygame.mixer.Sound('assets/sounds/tir.ogg')
sound_game_over = pygame.mixer.Sound('assets/sounds/game_over.ogg')
sound_click = pygame.mixer.Sound('assets/sounds/click.ogg')

game = Game()

running = True

# boucle tant que running est vrai
while running:

    # appliquer le background
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencou ou pas
    if game.is_playing:
        # declencher les instructiond de la partie
        game.update(screen)
    # si le jeu n'est pas lancer
    else:
        # ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    # update le screen
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # check que l'event est le fait de fermer la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu ce ferme")

        # detecter si un joueur lache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est used pour tirer
            if event.key == pygame.K_SPACE:
                game.player.lauche_prejectile()
                sound_tir.play()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier que la souris est appyer au bon endroit
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lander
                sound_click.play()
                game.start()