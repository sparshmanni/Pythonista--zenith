import csv
data = ["Name", "Subject1", "Subject2", "Subject3"]
x = [
["hogg", 78, 68, 83],
["quinx", 91, 65, 72],
["marie", 90, 87, 81],
["scarlett", 56, 73, 96],
["vincie", 71, 87, 34],
["jonh", 92, 67, 49],
]
y = "file.csv"
with open(y, 'w') as work:
   z = csv.writer(work)
   z.writerow(data)
   z.writerows(x)
