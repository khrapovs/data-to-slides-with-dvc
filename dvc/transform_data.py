from pathlib import Path

import polars as pl

if __name__ == "__main__":
    data_path = Path(__file__).parents[1] / "data"
    raw_data_path = data_path / "raw_data.csv"
    transformed_data_path = data_path / "transformed_data.parquet"
    raw_data = pl.read_csv(
        raw_data_path,
        has_header=False,
        new_columns=[
            "class",
            "alcohol",
            "malic_acid",
            "ash",
            "alcalinity_of_ash",
            "magnesium",
            "total_phenols",
            "flavanoids",
            "nonflavanoid_phenols",
            "proanthocyanins",
            "color_intensity",
            "hue",
            "od280/od315_of_diluted_wines",
            "proline",
        ],
    )
    raw_data.write_parquet(transformed_data_path)
