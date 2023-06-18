from project import history, download, get_ticker


comp = get_ticker("GOOGL")
hist = history(comp, "1mo")
down = download("GOOGL", "2023-05-01", "2023-05-01")


def test_get_ticker():
    assert type(get_ticker("GOOGL")) == type(comp)


def test_history():
    assert type(history(comp, "1mo")) == type(hist)


def test_download():
    assert type(download("GOOGL", "2023-05-01", "2023-05-01")) == type(down)
