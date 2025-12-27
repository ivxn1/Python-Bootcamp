import requests
from bs4 import BeautifulSoup
from requests import request

with open("./movies.txt", 'w') as f:
    response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/").text

    soup = BeautifulSoup(response, 'html.parser')
    print(soup)