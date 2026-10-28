from collections import Counter

import pandas as pd

counts = Counter()
for chunk in pd.read_csv("/data/yellow_tripdata_2024-01.csv",
                         usecols=["trip_distance"], chunksize=1_000_000):
    counts.update(chunk["trip_distance"].value_counts().to_dict())

hist = pd.Series(counts).sort_index()
cum = hist.cumsum()
n = cum.iloc[-1]

left = hist.index[cum.searchsorted((n - 1) // 2, side="right")]
right = hist.index[cum.searchsorted(n // 2, side="right")]

print(f"Mediana trip_distance: {(left + right) / 2:.2f}")
print(f"Liczba różnych wartości w stanie: {len(counts):,}")
