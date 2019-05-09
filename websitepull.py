import re


def pdfpull(soup):
    download = soup.select(".downloads-container")
    pattern = "(https.[A-Za-z0-9:/\-\.&_%]*?english.pdf)"
    pdf = re.findall(pattern, str(download))

    # Remove Duplicates
    results = list(set(pdf))
    print('####PDF to Re-upload####')
    for i in range(len(results)):
        print(results[i])
    print()
    return 'will replace later'


def techspecpull(soup):
    techspec = soup.select("#dynamic-techspec")
    techspec = str(techspec[0]).replace("\n", "")
    techspec = techspec.replace("id=\"dynamic-techspec\"", "class=\"techSpecTable\"")
    return techspec.encode('utf-8')


def descriptionpull(soup):
    description = soup.select(".description")
    description = str(description[0]).replace("\n", "")
    return description.encode('utf-8')


def titlepull(soup):
    title = str(soup.title.string)
    pattern = "(Elcometer \d*) (.*)"
    titlebreakdown = re.findall(pattern, title)
    return titlebreakdown[0][1] + ' | ' + titlebreakdown[0][0]