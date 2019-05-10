from bs4 import BeautifulSoup
import urllib.request
import csv
url_list=[""]
resp = urllib.request.urlopen("https://blast.elcometer.com/")
soup = BeautifulSoup(resp, 'lxml')
with open('Url_list.csv','w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    for link in soup.find_all('a', href = True, string = True):
        url_list.append(link['href'])
        writer.writerow(url_list)

csvFile.close()
