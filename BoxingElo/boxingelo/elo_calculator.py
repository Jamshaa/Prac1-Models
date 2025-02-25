import math

class EloCalculator:
    def __init__(self, k_factor=32, base_rating=1500):
        self.k_factor = k_factor
        self.base_rating = base_rating
        self.ratings = {}

    def get_rating(self, boxer):
        """ Obtiene el Elo actual de un boxeador, o el base si no existe. """
        return self.ratings.get(boxer, self.base_rating)

    def expected_score(self, rating_a, rating_b):
        """ Calcula la probabilidad esperada de que A gane contra B. """
        return 1 / (1 + math.pow(10, (rating_b - rating_a) / 400))

    def update_ratings(self, winner, loser):
        """ Actualiza los ratings de los boxeadores después de una pelea. """
        rating_winner = self.get_rating(winner)
        rating_loser = self.get_rating(loser)

        expected_win = self.expected_score(rating_winner, rating_loser)
        expected_loss = self.expected_score(rating_loser, rating_winner)

        # Actualizar valores con la fórmula de Elo
        new_winner_rating = rating_winner + self.k_factor * (1 - expected_win)
        new_loser_rating = rating_loser + self.k_factor * (0 - expected_loss)

        self.ratings[winner] = round(new_winner_rating, 2)
        self.ratings[loser] = round(new_loser_rating, 2)

    def get_all_ratings(self):
        """ Retorna los ratings de todos los boxeadores. """
        return self.ratings
