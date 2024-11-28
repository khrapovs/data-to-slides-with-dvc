from data_to_slides_with_dvc.main import main


def test_main() -> None:
    assert main(2) == 4
