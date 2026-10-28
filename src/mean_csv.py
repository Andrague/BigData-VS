import pandas as pd

file_path = "/data/yellow_tripdata_2024-01.csv"
df = pd.read_csv(file_path, low_memory=False)

print(f"Liczba wierszy: {len(df)}")

mean_distance = df["trip_distance"].mean()

print(f"Średni dystans przejazdu: {mean_distance}")
