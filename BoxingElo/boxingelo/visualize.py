import pandas as pd
import matplotlib.pyplot as plt

def plot_elo_ratings(ratings_file):
    """ Grafica la evolución del Elo de los boxeadores. """
    ratings = pd.read_csv(ratings_file)
    ratings = ratings.sort_values(by="Elo", ascending=False)  # Ordenar por mejor Elo

    plt.figure(figsize=(10, 5))
    plt.barh(ratings["Boxer"], ratings["Elo"], color="skyblue")
    plt.xlabel("Elo Rating")
    plt.ylabel("Boxeador")
    plt.title("Ranking de Elo de Boxeadores")
    plt.gca().invert_yaxis()  # Mejor visualización
    plt.show()
