# Created by Patalin.py
# Follow @Patalin.py on Instagram for more small projects like this
from bs4 import BeautifulSoup
import requests

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
website = response.text
soup = BeautifulSoup(website, 'html.parser')

# Scraping the movie titles
movies_titles = soup.find_all(name='h3', class_='title')

# Reverse the list so it starts from 1 not 100
movies_list_reversed = [movie.getText() for movie in movies_titles][::-1]

# Create a file called movies and add all 100 movies
with open('movies.txt', 'w') as file:
    for movie in movies_list_reversed:
        file.write(f'{movie}\n')




