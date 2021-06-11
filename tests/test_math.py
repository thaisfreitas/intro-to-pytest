import pytest
# -------------------------------------------------------------------------
# most simple test
# -------------------------------------------------------------------------
@pytest.mark.math
def test_one_plus_one_simple():
    assert 1 + 2 == 3
# -------------------------------------------------------------------------
# Assersion introspection
# -------------------------------------------------------------------------
def test_one_plus_one_with_var():
    a = 1
    b = 2
    c = 3
    assert a + b == c

# -------------------------------------------------------------------------
# A test function that verifies an expection
# -------------------------------------------------------------------------

def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str (e.value)