from pathlib import Path

from data_to_slides_with_dvc.data_ingestion import download_data


def test_download_data() -> None:
    local_path = Path(__file__).parent / "data.parquet"
    local_path.unlink(missing_ok=True)

    download_data(local_path=local_path)

    assert local_path.is_file()

    local_path.unlink()
