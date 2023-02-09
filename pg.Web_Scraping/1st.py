from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs =BeautifulSoup(html.read(), 'html.parser')
nameList = bs.find_all('span',{'calss':'green'})
for name in nameList:
    print(name.get_text())
