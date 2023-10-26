from bs4 import BeautifulSoup
import requests


url = 'https://mtgdecks.net/Commander/nekusar-the-mindrazer-decklist-by-ishita-junpei-1771025'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html') 

table = soup.find('table')

print(table)