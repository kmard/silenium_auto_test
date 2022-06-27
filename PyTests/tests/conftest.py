import pytest


@pytest.fixture()
def set_up():
    print('\nConnect ')
    yield
    print('\nDisconnect ')

# cls,function
@pytest.fixture(scope='module')
def some():
    print('\nBEGIN')
    yield
    print('END ')