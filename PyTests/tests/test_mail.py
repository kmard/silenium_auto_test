
#pytest -s -v test_mail.py
import pytest

@pytest.fixture()
def set_up():
    print('\nlogin is complete')

def test_sebding_mail_1(set_up):
    print('letter sended_1')

def test_sebding_mail_2(set_up):
    print('letter sended_2')