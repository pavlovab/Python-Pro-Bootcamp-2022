from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

with open("movies.txt", "a") as file:
    for movie in reversed(all_movies):
        file.write(f"{movie.getText()}\n")
