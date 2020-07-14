from player import Player
from monster import Monster
import pygame

# créer une classe game
class Game:

    def __init__(self):
        # definir si le jeu a commencer ou pas
        self.is_playing = False
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()


    def game_over(self):
        # remettre le jeu a neuf, reinitialiser toutes les variables
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # afficher le joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # recuperer les projectiles du joeur
        for projectiles in self.player.all_projectiles:
            projectiles.move()

        # appliquer les projectiles
        self.player.all_projectiles.draw(screen)

        # recuperer les monstre du jeux et les move
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer l'ensemble de monstre
        self.all_monsters.draw(screen)

        # check ver la ou le joueur veu aller
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)