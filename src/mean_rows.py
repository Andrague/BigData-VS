# bez argumentu cały plik, z argumentem tylko pierwsze N wierszy
import sys
import pandas as pd

file_path = "/data/yellow_tripdata_2024-01.csv"
nrows = int(sys.argv[1]) if len(sys.argv) > 1 else None
df = pd.read_csv(file_path, nrows=nrows, low_memory=False)
rows = len(df)
memory_bytes = df.memory_usage(deep=True).sum()
memory_mb = memory_bytes / (1024 ** 2)

print(f"Wiersze: {rows:,}")
print(f"Dane: {memory_mb:.0f} MB")
