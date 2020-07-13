from player import Player


# créer une classe game
class Game:

    def __init__(self):
        # generer notre joueur
        self.player = Player()
        self.pressed = {}