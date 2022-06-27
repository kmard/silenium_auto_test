
#pytest -s -v test_mail.py


def test_sebding_mail_1(set_up, some):
    print('letter sended_1')


def test_sebding_mail_2(set_up):
    print('letter sended_2')


def test_sebding_mail_3(set_up, some):
    # 2/0
    print('letter sended_3')
