#!/usr/bin/env bash
# W3 - loads the yearly dataset into HDFS.
# Runs INSIDE the cluster, where the hdfs client and its configuration live:
#   docker compose -f compose-hdfs.yml exec namenode bash /scripts/load_to_hdfs.sh | tee out/02-load.log
# Must be re-runnable: after the cluster is destroyed you want to restore
# the state with one command, not twelve.
#
# Fill in the places marked TODO
#!/usr/bin/env bash
set -euo pipefail

HDFS_DIR="/taxi"
LOCAL_DIR="${1:-/mnt/host}"

echo "== creating target directory in HDFS =="
# TODO 1: utworzenie katalogu w HDFS
hdfs dfs -mkdir -p "$HDFS_DIR"

echo "== uploading files =="
for f in "$LOCAL_DIR"/yellow_tripdata_2024-*.parquet; do
  echo "  -> $(basename "$f")"
  # TODO 2: przesłanie pliku z nadpisaniem istniejącej kopii
  hdfs dfs -put -f "$f" "$HDFS_DIR/"
done

echo "== verification =="
# TODO 3: wyświetlenie plików i policzenie ich liczby
hdfs dfs -ls "$HDFS_DIR"
echo "Number of files: $(hdfs dfs -ls "$HDFS_DIR" | awk 'NR > 0 && $1 ~ /^-/ {count++} END {print count+0}')"
