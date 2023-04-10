import pytest


def test_01():
    assert 1 == 1

@pytest.mark.skip
def test_should_be_skipped() -> None:
    pass