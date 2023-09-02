# Complete the function get_length which returns the length of any passed string, ignoring whitespace characters.
# eg. get_length('hello there!') => 11


def get_length(input_str):
    no_white_space = input_str.split(' ')
    total_length = 0
    for word in no_white_space :
        total_length += len(word)
        # print(total_length)
    return total_length


get_length('hello there!')
# tests

def test_measures_the_length_of_single_char():
    expected = 1
    result = get_length('a')

    assert result == expected

def test_measures_the_length_of_single_word():
    expected = 4
    result = get_length('tofu')

    assert result == expected

def test_ignores_white_spaces():
    expected = 22
    result = get_length('Linda McCartney sausages')

    assert result == expected

