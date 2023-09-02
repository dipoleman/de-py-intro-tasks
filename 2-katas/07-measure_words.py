# Create the function measure_words which takes a string of words separated by
# commas. It should return a dictionary which records the length of each word.
# Each property should be of the form str: int, where the key is in lowercase.
# You can assume the string will not contain duplicate words.
# eg. measure_words('Ficus, Alocasia, Begonia') => {'ficus': 5, 'alocasia': 8, 'begonia':7}


def measure_words(input_str):
    if len(input_str) == 0:
        return {}
    output_dict = {}
    my_list = input_str.split(', ')
    # print(my_list)
    for word in my_list:
        output_dict[word.lower()] = len(word)
        # print(output_dict)
    return output_dict

# measure_words('Ficus, Alocasia, Begonia')

# measure_words('')

#tests
def test_returns_empty_dict_when_passed_empty_str():
    expected = {}
    result = measure_words('')

    assert result == expected

def test_assigns_property_for_single_word():
    expected = {'hello': 5}
    result = measure_words('hello')

    assert result == expected

def test_assigns_property_for_multiple_words():
    expected = {'multiple': 8, 'words': 5, 'are': 3, 'fun': 3}
    result = measure_words('multiple, words, are, fun')

    assert result == expected
