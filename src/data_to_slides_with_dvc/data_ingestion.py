from pathlib import Path

import polars as pl


def download_data(local_path: Path) -> None:
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
    data = pl.read_csv(url)
    data.write_parquet(local_path)
