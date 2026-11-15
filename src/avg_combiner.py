import sys

current_zone = None
total_distance = 0.0
count = 0

def output_result():
    if current_zone is not None:
        average = total_distance / count
        print(f"{current_zone}\t{average:.4f}")


for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    zone, distance = line.split("\t")
    distance = float(distance)

    if current_zone is None:
        current_zone = zone

    if zone != current_zone:
        output_result()

        current_zone = zone
        total_distance = 0.0
        count = 0

    total_distance += distance
    count += 1

output_result()
