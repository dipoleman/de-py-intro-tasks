# Create the function even_odd which accepts a list of integers and returns a new list of strings
# describing whether the number in it's postion is odd or even.
# eg. even_odd([5]) => ['odd']
#     even_odd([1,30,21,4,88]) => ['odd', 'even', 'odd', 'even', 'even']

def even_odd(input):
    output = []
    for num in input:
        if num % 2 == 0:
            output.append('even')
        else:
            output.append('odd')
    return output
            

#tests
def test_returns_empty_list_when_passed_empty_list():
    expected = []
    result = even_odd([])

    assert result == expected

def test_inserts_odd_string_for_odd_number():
    expected = ['odd']
    result = even_odd([1])

    assert result == expected

def test_inserts_even_string_for_even_number():
    expected = ['even']
    result = even_odd([2])

    assert result == expected

def test_handles_multiple_numbers():
    expected = ['odd', 'even', 'odd', 'even']
    result = even_odd([1, 2, 3, 4])

    assert result == expected

