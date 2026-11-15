import sys
import math

DIST_COL = 4   
ZONE_COL = 7  

out = sys.stdout
for line in sys.stdin:
    fields = line.rstrip("\n").split(",")
    if len(fields) <= ZONE_COL:
        continue
    try:
        zone = int(float(fields[ZONE_COL]))
        dist = float(fields[DIST_COL])
    except ValueError:          
        continue
    if not math.isfinite(dist):
        continue
    out.write(f"{zone}\t{dist}\t1\n")
