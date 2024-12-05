from pathlib import Path

import polars as pl
from joblib import dump
from loguru import logger
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier

if __name__ == "__main__":
    data_path = Path(__file__).parents[1] / "data"
    transformed_data_path = data_path / "transformed_data.parquet"
    model_path = data_path / "model.joblib"

    transformed_data = pl.read_parquet(transformed_data_path)

    x_data = transformed_data.select(pl.selectors.exclude("class"))
    y_data = transformed_data.select("class")

    model = Pipeline([("scaler", MinMaxScaler()), ("classifier", DecisionTreeClassifier())])

    logger.info("Will train model...")

    model = model.fit(X=x_data, y=y_data)
    dump(value=model, filename=model_path)

    logger.info(f"Finished training model and saved to {model_path}.")
