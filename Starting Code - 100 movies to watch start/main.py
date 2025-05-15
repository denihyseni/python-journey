import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)

soup = BeautifulSoup(response.text,"html.parser")

movies = soup.select(selector="h3",class_="title")

names = []


for n in movies:
    names.insert(0, n.getText())



with open("movies.txt" , mode="a") as file:
    for _ in names:
        movie_names = _.strip("\n")
        file.write(f"{movie_names}\n")