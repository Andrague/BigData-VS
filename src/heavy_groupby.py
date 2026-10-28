import pandas as pd

file_path = "/data/yellow_tripdata_2024-01.parquet"
df = pd.read_parquet(file_path)
res = df.groupby(["PULocationID", "DOLocationID"]).apply(
    lambda g: g.sort_values("trip_distance"),
    include_groups=False,
)

print(f"Liczba grup: {df.groupby(['PULocationID', 'DOLocationID']).ngroups}")
print(f"Liczba wierszy wyniku: {len(res)}")

