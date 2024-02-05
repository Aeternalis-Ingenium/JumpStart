from src import __version__


def test_version(test_app):
    assert __version__ == test_app.version
