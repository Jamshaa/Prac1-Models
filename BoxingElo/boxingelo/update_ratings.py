import pandas as pd
from boxingelo.elo_calculator import EloCalculator

def update_elo_ratings(fights_file, ratings_file):
    """ Lee las peleas, actualiza los ratings y guarda los resultados. """
    # Cargar datos de peleas
    fights = pd.read_csv(fights_file)

    # Inicializar calculadora de Elo
    elo = EloCalculator()

    for _, row in fights.iterrows():
        winner, loser = row["winner"], row["loser"]
        elo.update_ratings(winner, loser)

    # Guardar los nuevos ratings en CSV
    ratings_df = pd.DataFrame(elo.get_all_ratings().items(), columns=["Boxer", "Elo"])
    ratings_df.to_csv(ratings_file, index=False)
    print(f"✅ Ratings actualizados y guardados en {ratings_file}")
