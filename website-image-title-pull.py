from bs4 import BeautifulSoup
import requests
import csv
data_list=[]
url = 'https://blast.elcometer.com/abrasive-media-valves/'
# get contents from url
content = requests.get(url).content
# get soup
soup = BeautifulSoup(content,'lxml') # choose lxml parser
for link in soup.find_all("div",attrs={"class" : "category-entry"}): #a loop that run over the page in the category entry class
    title = link.find("p",attrs={"class":"category-entry-title"}).get_text() #find the title in <p> category-entry-title
    image = link.find("img", attrs={"class":"category-entry-image"}).get("src") #find the image in category entry image
    new_data = { title, image}
    data_list.append(new_data)
with open ('selector.csv','w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(data_list)

csvFile.close()
