import pytest


@pytest.fixture()
def set_up():
    print('\nConnect ')
    yield
    print('\nDisconnect ')