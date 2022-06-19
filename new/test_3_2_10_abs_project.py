
# python test_3_2_10_abs_project.py


def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")