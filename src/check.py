from pathlib import Path

import pandas as pd

DATA = Path("/data/yellow_tripdata_2024-01.parquet")
OUT = Path("/out")

df = pd.read_parquet(DATA)

stats = (
    df.groupby("PULocationID")["trip_distance"]
    .agg(
        count="count",
        mean="mean"
    )
    .reset_index()
)

#IDs to avoid sortings problems
stats["PULocationID"] = stats["PULocationID"].astype(str)

print("=== PARQUET REFERENCE ===")
print(f"Number of zones: {len(stats)}")


# Read results from cluster
def read_result(filename, value_name):
    path = OUT / filename
    result = pd.read_csv(
        path,
        sep="\t",
        header=None,
        dtype=str,
    )

    result = result.iloc[:, :3].copy()
    columns = ["zone", value_name]
    if result.shape[1] == 3:
        columns.append("count")
    result.columns = columns
    result["zone"] = result["zone"].astype(str)
    result[value_name] = pd.to_numeric(
        result[value_name], errors="coerce"
    )

    if "count" in result.columns:
        result["count"] = pd.to_numeric(
            result["count"], errors="coerce"
        )

    return result


mean_result = read_result("z1-mean.tsv", "cluster_mean")
avg_result = read_result("z2-avg.tsv", "combiner_mean")

# Compare normal mapReducer
comparison = stats.merge(
    mean_result,
    left_on="PULocationID",
    right_on="zone",
    how="inner",
)

print("\Zadanie1:")
print(f"Parquet zones: {len(stats)}")
print(f"Cluster zones: {len(mean_result)}")
print(f"Matched zones: {len(comparison)}")

if "count" in mean_result.columns:
    count_match = (
        comparison["count_x"] == comparison["count_y"]
    )
    print(f"Equal course counts: {count_match.sum()}/{len(comparison)}")
else:
    print("Course counts: not available in z1-mean.tsv")

comparison["mean_diff"] = (
    comparison["mean"] - comparison["cluster_mean"]
).abs()

print(
    "Maximum mean difference:",
    f"{comparison['mean_diff'].max():.5f}"
)

avg_comparison = stats.merge(
    avg_result,
    left_on="PULocationID",
    right_on="zone",
    how="inner",
)

avg_comparison["difference"] = (
    avg_comparison["mean"]
    - avg_comparison["combiner_mean"]
).abs()

different = avg_comparison[
    avg_comparison["difference"] > 0.01
]

print("\nZadanie2:")
print(f"\nZones compared: {len(avg_comparison)}")
print(f"\nZones differing by more than 0.01: {len(different)}")
print("\nTen largest differences:")

top10 = avg_comparison.nlargest(10, "difference")
top10 = avg_comparison.nlargest(10, "difference")

print(
    top10[
        [
            "PULocationID",
            "mean",
            "combiner_mean",
            "difference",
        ]
    ].to_string())
