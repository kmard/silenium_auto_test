import pytest

#(venv) PS C:\Projects_Python\silenium_auto_test> pytest -v  test_xfail.py
# https://pytest-docs-ru.readthedocs.io/ru/latest/skipping.html

@pytest.mark.xfail(strict=True,reason='error')
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False