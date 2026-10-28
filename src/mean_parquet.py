import pandas as pd

file_path = "/data/yellow_tripdata_2024-01.parquet"

df = pd.read_parquet(file_path)

print(f"Liczba wierszy: {len(df)}")

memory_mb = df.memory_usage(deep=True).sum() / (1024 ** 2)
print(f"Pamięć DataFrame: {memory_mb:.2f} MB")

mean_distance = df["trip_distance"].mean()

print(f"Średni dystans przejazdu: {mean_distance}")
