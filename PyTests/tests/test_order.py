
#pip3 install pytest-ordering
#pytest -s -v test_order.py
import pytest


@pytest.mark.run(order=2)
def test_method_1():
    print('test_method_1')

@pytest.mark.run(order=1)
def test_method_2():
    print('test_method_2')


def test_method_3():
    print('test_method_3')

def test_method_4():
    print('test_method_4')