from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen("https://blast.elcometer.com/")
soup = BeautifulSoup(resp, 'lxml')

for link in soup.find_all('a', href=True):
    print(link['href'])
