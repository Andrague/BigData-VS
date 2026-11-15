import csv
import sys

reader = csv.reader(sys.stdin)

for row in reader:
    if len(row) <= 7:
        continue

    # Skip header,it is.
    if row[0] == "VendorID":
        continue
    zone = row[7]
    distance = row[4]
    if not zone or not distance:
        continue
    try:
        zone = int(zone)
        value = float(distance)
    except ValueError:
        continue

    print(f"{zone}\t{value}\t1")
