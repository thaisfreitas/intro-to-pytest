import pytest
# --------------------------
# Multiplication test ideias
# --------------------------

# two positive integers
# identity: multiplying any number by 1
# zero: multiplying any number by 0
# positive by a negative
# negative by a negative 
# multiply floats

# --------------------------

def test_multiply_two_ints():
    assert 1 * 2 == 2

def test_multiply_identity():
    pass

def test_multiply_zero():
    pass

#DRY Principle:  don't reat yourself! 

# --------------------------
# A parametrized test function
# --------------------------

products = [
  (2, 3, 6),      # positive integers
  (1,99, 99),     # identity
  (8, 0, 0),      # zero
  (3, -4, -12),   # positive by negative
  (-5, -5, 25),   # negative by negative
  (2.5, 6.7, 16.75) #floats
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplcation(a, b, product):
  assert a * b == product