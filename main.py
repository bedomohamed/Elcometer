from bs4 import BeautifulSoup
import requests
from ElcometerSitePull import websitepull
import csv

lines = []

with open('./resources/ElcometerBlastSnap.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        newrow = []
        url = ', '.join(row)
        content = r = requests.get(url).text
        soup = BeautifulSoup(content, "html.parser")

        # Pull PDFs
        newrow.append(websitepull.pdfpull(soup))

        # Pull Technical Specifications
        newrow.append(websitepull.techspecpull(soup))

        # Pull Description Content
        newrow.append(websitepull.descriptionpull(soup))

        # Pull Title Content
        newrow.append(websitepull.titlepull(soup))

        lines.append(newrow)

print(lines)
with open('./resources/output.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(lines)

csvFile.close()
