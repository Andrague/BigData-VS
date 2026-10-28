import pandas as pd

ROWS = 200_000

csv_path = "/data/yellow_tripdata_2024-01.csv"
parquet_path = "/data/yellow_tripdata_2024-01.parquet"

# CSV: odczytaj bezpośrednio pierwsze 200 000 wierszy
df_csv = pd.read_csv(csv_path, nrows=ROWS)

# Parquet: wczytaj dane, a następnie wybierz pierwsze 200 000 wierszy
df_parquet = pd.read_parquet(parquet_path).head(ROWS)

# Zbierz typy i zajętość pamięci dla każdej kolumny
csv_memory = df_csv.memory_usage(deep=True, index=False)
parquet_memory = df_parquet.memory_usage(deep=True, index=False)

comparison = pd.DataFrame({
    "CSV dtype": df_csv.dtypes.astype(str),
    "CSV memory (bytes)": csv_memory,
    "Parquet dtype": df_parquet.dtypes.astype(str),
    "Parquet memory (bytes)": parquet_memory,
})

print(f"Liczba wierszy CSV: {len(df_csv)}")
print(f"Liczba wierszy Parquet: {len(df_parquet)}")
print("\nPorównanie kolumn:")
print(comparison.to_string())

print("\nŁączna zajętość pamięci w RAM:")
print(f"CSV:     {csv_memory.sum():,} bytes")
print(f"Parquet: {parquet_memory.sum():,} bytes")
