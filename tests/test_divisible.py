from  stuff.is_divisible import is_divisible;

def test_is_divisible():
    assert is_divisible(3,2,2) == False
    assert is_divisible(3,3,4) == False
    assert is_divisible(12,3,4) == True
    assert is_divisible(8,3,4) == False