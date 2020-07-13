import pygame
from game import Game
pygame.init()



# generer la fenetre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

# importer et charger le background*
background = pygame.image.load('assets/bg.jpg')

game = Game()

running = True

# boucle tant que running est vrai
while running:

    # appliquer le background
    screen.blit(background, (0, -200))

    # afficher le joueur
    screen.blit(game.player.image, game.player.rect)

    # recuperer les projectiles du joeur
    for projectiles in game.player.all_projectiles:
        projectiles.move()

    # appliquer les projectiles
    game.player.all_projectiles.draw(screen)

    # check ver la ou le joueur veu aller
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False