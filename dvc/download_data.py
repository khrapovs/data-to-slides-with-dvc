from pathlib import Path

from data_to_slides_with_dvc.data_ingestion import download_data

if __name__ == "__main__":
    local_path = Path(__file__).parents[1] / "data" / "raw_data.parqquet"
    download_data(local_path=local_path)
