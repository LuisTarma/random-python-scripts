from bs4 import BeautifulSoup
from urllib.request import urlopen

redditFile = urlopen("https://virtualpiano.net")
redditHtml = redditFile.read() 
redditFile.close()

soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))
