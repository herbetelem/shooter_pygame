import pygame

# definir la classe du projectile du joueur
class Projectile(pygame.sprite.Sprite):

    # definir le constructeur
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # faire tourner le projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # si le projectile touche un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # suprimer le projectil si touche un monstre
            self.remove()
            # infliger des degat
            monster.damage(self.player.attack)

        # verifier si le projectile n'est plus dans l'ecran
        if self.rect.x > 1080:
            # suprimer le projectil en dehor de l'ecran
            self.remove()