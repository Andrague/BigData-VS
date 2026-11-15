
import sys

current_zone = None
total_sum = 0.0
total_count = 0


def emit(zone, distance_sum, count):
    if count > 0:
        mean = distance_sum / count
        print(f"{zone}\t{mean:.3f}")


for line in sys.stdin:
    parts = line.strip().split("\t")

    if len(parts) != 3:
        continue

    zone, distance_sum, count = parts

    try:
        distance_sum = float(distance_sum)
        count = int(count)
    except ValueError:
        continue

    if current_zone is not None and zone != current_zone:
        emit(current_zone, total_sum, total_count)
        total_sum = 0.0
        total_count = 0

    current_zone = zone
    total_sum += distance_sum
    total_count += count

if current_zone is not None:
    emit(current_zone, total_sum, total_count)
