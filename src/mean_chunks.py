import pandas as pd

file_path = "/data/yellow_tripdata_2024-01.csv"
chunksize = 1_000_000

chunk_means = []
total_distance = 0.0
total_valid = 0
total_rows = 0

for i, chunk in enumerate(
    pd.read_csv(file_path, chunksize=chunksize, low_memory=False), start=1
):
    distances = chunk["trip_distance"]
    chunk_rows = len(chunk)
    chunk_mean = distances.mean()
    chunk_median = distances.median()

    print(
        f"Porcja {i}: wiersze={chunk_rows:,}, "
        f"średnia={chunk_mean:.4f}, mediana={chunk_median:.4f}"
    )

    chunk_means.append(chunk_mean)
    total_distance += distances.sum()
    total_valid += distances.count()
    total_rows += chunk_rows
mean_of_means = sum(chunk_means) / len(chunk_means)
weighted_mean = total_distance / total_valid

print(f"\nŁączna liczba wierszy: {total_rows:,}")
print(f"(a) Średnia ze średnich porcji: {mean_of_means:.4f}")
print(f"(b) Średnia z sumy / liczby wartości: {weighted_mean:.4f}")
