import csv

lines = [['1', ' Jack', ' Michigan'], ['2', ' Marie', ' California']]

with open('./resources/output.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(lines)

csvFile.close()