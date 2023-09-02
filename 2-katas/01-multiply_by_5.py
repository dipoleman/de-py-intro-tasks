# Complete the function multiply_by_5 which returns the product of the passed number with 5.
# eg. multiply_by_5(10) => 50



def multiply_by_5 (num):
    return 5*num




# tests
def test_returns_zero_when_passed_zero():
    expected = 0
    result = multiply_by_5(0)

    assert result == expected

def test_multiplies_passed_arg_by_five():
    
    assert multiply_by_5(10) == 50
    assert multiply_by_5(7) == 35







