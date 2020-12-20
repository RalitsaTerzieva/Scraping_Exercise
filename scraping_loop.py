from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://sprinkledfood.com/category/deserts/'
html = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
Title = soup.find_all("h3", {"class":"entry-title"})
for i in Title:
    name_recipe = i.find("a", {"rel":"bookmark"}).get_text()
    print(name_recipe)

