from bs4 import BeautifulSoup
import requests


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "2000-08-12"


response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

titles = soup.select("div.o-chart-results-list-row-container ul li ul li h3#title-of-a-story")
song_names = [song.getText().strip() for song in titles]
print(song_names)
