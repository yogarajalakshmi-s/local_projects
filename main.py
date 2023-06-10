import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
movie_data = requests.get(URL).text

soup = BeautifulSoup(movie_data, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movies][::-1]
print(movie_titles)

with open(file="movies.txt", mode="w", encoding="utf-8") as file:
    for title in movie_titles:
        file.write(f"{title}\n")
