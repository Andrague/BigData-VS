import sys

out = sys.stdout
current_zone = None
counts = {}

def flush(zone, counts):
    for dist, c in counts.items():
        out.write(f"{zone}\t{dist}\t{c}\n")

for line in sys.stdin:
    parts = line.rstrip("\n").split("\t")
    if len(parts) != 3:
        continue
    zone, dist, c = parts
    if zone != current_zone:
        if current_zone is not None:
            flush(current_zone, counts)
        current_zone = zone
        counts = {}
    counts[dist] = counts.get(dist, 0) + int(c)

if current_zone is not None:
    flush(current_zone, counts)
