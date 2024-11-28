from pathlib import Path

import polars as pl
from loguru import logger


def download_data(local_path: Path) -> None:
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
    logger.info(f"Will download data from {url} to {local_path}...")
    data = pl.read_csv(url)
    data.write_parquet(local_path)
    logger.info("Finished downloading data.")
