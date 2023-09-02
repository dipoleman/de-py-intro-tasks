# Create the function contains_repeats and returns true if the passed string contains repeat characters, otherwise it returns false.
# eg. contains_repeats('apple') => True
#     contains_repeats('pear') => False


def contains_repeats(input):

    for i in range(1,len(input)):
        if input[i]==input[i-1]:
            return True

    return False


# tests
def test_returns_false_for_single_character():
    expected = False
    result = contains_repeats('a')

    assert result == expected


def test_returns_false_for_unique_characters():
    expected = False
    result = contains_repeats('abcde')

    assert result == expected


def test_detects_multiple_characters():
    expected = True
    result = contains_repeats('aabccdde')

    assert result == expected
