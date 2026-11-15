import sys

out = sys.stdout
current_zone = None
counts = {}

def emit(zone, counts):
    values = sorted(counts, key=float)          
    n = sum(counts.values())
    lo = (n - 1) // 2                           
    hi = n // 2                               
    seen = 0
    v_lo = v_hi = None
    for v in values:
        seen += counts[v]
        if v_lo is None and seen > lo:
            v_lo = float(v)
        if seen > hi:
            v_hi = float(v)
            break
    median = (v_lo + v_hi) / 2                 
    out.write(f"{zone}\t{median:.3f}\t{n}\t{len(values)}\n")

for line in sys.stdin:
    parts = line.rstrip("\n").split("\t")
    if len(parts) != 3:
        continue
    zone, dist, c = parts
    if zone != current_zone:
        if current_zone is not None:
            emit(current_zone, counts)
        current_zone = zone
        counts = {}
    counts[dist] = counts.get(dist, 0) + int(c)

if current_zone is not None:
    emit(current_zone, counts)
