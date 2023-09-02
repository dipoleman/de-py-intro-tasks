# Create the function contains_digit which takes an integer. It should return a List of all the numbers which contain that numeral between 1-100.
# eg. contains_digit(9) = >[9, 19, 29, 39, 49, 59, 69, 79, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#     contains_digit(50) = >[50]

def contains_digit(n_int):
    n = str(n_int)
    ans = []
    for i in range(1,101):
        if n in str(i):
            ans.append(i)
    return ans

#tests

def test_evaluates_numerals_units_position():
    expected = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = contains_digit(0)

    assert result == expected

def test_evaluates_numerals_all_positions():
    expected = [9, 19, 29, 39, 49, 59, 69, 79, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    result = contains_digit(9)

    assert result == expected