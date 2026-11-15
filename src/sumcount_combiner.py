
import sys
from collections import defaultdict

totals = defaultdict(lambda: [0.0, 0])

for line in sys.stdin:
    parts = line.strip().split("\t")

    if len(parts) != 3:
        continue

    zone, distance_sum, count = parts

    try:
        totals[zone][0] += float(distance_sum)
        totals[zone][1] += int(count)
    except ValueError:
        continue

for zone in sorted(totals, key=int):
    distance_sum, count = totals[zone]
    print(f"{zone}\t{distance_sum}\t{count}")
