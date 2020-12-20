from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://sprinkledfood.com/recipe/blueberry-vegan-balls/"
page = urlopen(url).read()
html = page.decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
li_tags = soup.find('li', attrs={'class':'single-meta-likes'})
span_tags = li_tags.find('span', attrs={'class':'slide-button-sub-label'})
likes = int(span_tags.string)
print(likes)
    
