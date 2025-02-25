from boxingelo.update_ratings import update_elo_ratings
from boxingelo.visualize import plot_elo_ratings

if __name__ == "__main__":
    fights_file = "data/fights.csv"
    ratings_file = "data/elo_ratings.csv"

    # Actualizar ratings con los datos de peleas
    update_elo_ratings(fights_file, ratings_file)

    # Visualizar evolución del Elo
    plot_elo_ratings(ratings_file)

