class Morpion:
    def __init__(self):
        self.plateau = [[' ' for _ in range(3)]
                        for _ in range(3)]  # plateau de 3x3
        self.joueur = 'X'  # Joueur par défaut

    def afficher(self):
        """Affiche le plateau de jeu."""
        pass

    def jouer_coup(self, ligne, colonne):
        """ Code pour jouer un coup """
        pass

    def jouer(self):
        """ Code pour gérer le jeu"""
        pass
