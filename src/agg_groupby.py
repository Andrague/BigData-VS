import pandas as pd

file_path = "/data/yellow_tripdata_2024-01.parquet"
df = pd.read_parquet(file_path)

res = df.groupby(["PULocationID", "DOLocationID"])["trip_distance"].agg(
    ["count", "mean"]
)

print(f"Liczba grup: {len(res)}")
print("\nTrzy najliczniejsze pary stref:")
print(res.sort_values("count", ascending=False).head(3).to_string())
