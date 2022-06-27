
#pytest -s -v test_mail.py
import pytest

@pytest.fixture()
def set_up():
    print('\nConnect ')
    yield
    print('\nDisconnect ')

def test_sebding_mail_1(set_up):
    print('letter sended_1')

def test_sebding_mail_2(set_up):
    print('letter sended_2')

def test_sebding_mail_3(set_up):
    # 2/0
    print('letter sended_3')


