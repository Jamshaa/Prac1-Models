import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_tapology(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: No se pudo acceder a Tapology")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    fights = []

    fight_rows = soup.find_all("div", class_="fightCard")
    for fight in fight_rows:
        try:
            boxer_a = fight.find("div", class_="fighterA").text.strip()
            boxer_b = fight.find("div", class_="fighterB").text.strip()

            if "winner" in fight.find("div", class_="fighterA").get("class", []):
                winner, loser = boxer_a, boxer_b
            else:
                winner, loser = boxer_b, boxer_a

            fights.append([winner, loser])
        except AttributeError:
            continue

    return fights


def save_fights_to_csv(fights, filename):
    df = pd.DataFrame(fights, columns=["winner", "loser"])
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    url = "https://www.tapology.com/fightcenter"
    fights = scrape_tapology(url)
    if fights:
        save_fights_to_csv(fights, "data/fights.csv")
        print("Datos guardados en data/fights.csv")
