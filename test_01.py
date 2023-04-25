import pytest


def test_01():
    assert 1 == 1


@pytest.mark.skip
def test_should_be_skipped() -> None:
    pass


@pytest.mark.skipif(4 > 0, reason="Skipped because 4>1")
def test_should_be_skipped_if() -> None:
    assert 1 == 2


@pytest.mark.xfail
def test_expected_failure():
    assert 12 > 5


class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f"{self.name}: {self.stock_symbol}"

@pytest.fixture
def company():
    company = Company("MSD", "cow")
    return company

def test_use_fixture(company):
    print(f'Printing {company} from fixture')

@pytest.mark.parametrize(
    "company_name",
    ["Spotify", "Telegram", "Monobank"],
    ids=["Spotify Test", "Telegram Test", "Monobank Test"])
def test_parametrized(company_name):
    print(f"\n Test with {company_name}")

def raise_exception():
    raise ValueError("I am the exception")

def test_exception():
    with pytest.raises(ValueError) as e:
        raise_exception()
    assert "I am the exception" == str(e.value)
#check the beeminder