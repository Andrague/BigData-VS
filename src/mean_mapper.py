import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    #Skip csv head
    if not row or row[0] == "VendorID":
        continue

    try:
        distance = float(row[4])
        zone = row[7]

        print(f"{zone}\t{distance}")

    except (ValueError, IndexError):
        continue
