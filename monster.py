import pygame
import random

# definir la classe du monstre
class Monster(pygame.sprite.Sprite):


    # definir la method de construction
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.max_velocity = 3
        self.min_velocity = 1
        self.velocity = random.randint(self.min_velocity, self.max_velocity)
        self.monster_killed = 0

    def damage(self, amount):
        # Infliger les degats
        self.health -= amount

        # verifier si le mob est a 0 hp
        if self.health <= 0:
            # reaparaitre comme un nouveau monstre
            self.monster_killed += 1
            if self.monster_killed > 20:
                self.min_velocity = 3
                self.max_velocity = 5
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(self.min_velocity, self.max_velocity)
            self.health = self.max_health



    def update_health_bar(self, surface):
        # dessiner l'arriere plan de la barre de vie du monstre
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        # dessiner la barre de vie du monstre
        pygame.draw.rect(surface, (255, 20, 20), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement ne ce fait que si pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else :
            # infliger des degats au joueur
            self.game.player.damage(self.attack)