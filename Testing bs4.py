from bs4 import BeautifulSoup
import requests
import re

url = "https://blast.elcometer.com/elcometer-1020-portable-abrasive-blast-machine-12bar-174psi/"

content = r = requests.get(url).text

soup = BeautifulSoup(content)

spareparts = soup.select(".spare-parts .style1")

print(spareparts)

description = soup.select(".description")
print('####Elcometer Product Description####')
print(str(description[0]).replace("\n", ""))
print()
techspec = soup.select("#dynamic-techspec")
techspec = str(techspec[0]).replace("\n", "")
print('####Elcometer Technical Specs####')
print(techspec)
print()
title = str(soup.title.string)

pattern = "(Elcometer \d*) (.*)"

titlebreakdown = re.findall(pattern, title)
print('####Elcometer New Title####')
print(titlebreakdown[0][1] + ' | ' + titlebreakdown[0][0])
print()
download = soup.select(".downloads-container")
pattern = "(https.[A-Za-z0-9:/\-\.&_%]*?english.pdf)"

pdf = re.findall(pattern, str(download))

# Remove Duplicates
results = list(set(pdf))
print('####PDF to Re-upload####')
for i in range(len(results)):
    print(results[i])
print()
