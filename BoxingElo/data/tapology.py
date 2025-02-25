import requests
from bs4 import BeautifulSoup

URL = "https://www.tapology.com/rankings/pro-boxing"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Extraer nombres de boxeadores
boxers = [b.text.strip() for b in soup.select(".ranking-listing a")]

print(boxers)  # Lista de nombres de boxeadores
