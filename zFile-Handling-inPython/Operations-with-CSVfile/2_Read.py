import csv
with open('file.csv','rt')as file:
   csv_rows = csv.reader(file)
   for row in csv_rows:
      print(row)
