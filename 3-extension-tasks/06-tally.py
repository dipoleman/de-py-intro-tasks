# Create the function tally which when given a list, creates at dictionary which counts the occurences of each item.

# eg. tally(['dog', 'pineapple', 'pineapple', 'furby' 'pineapple']) => {'dog: 1, 'pineapple': 3, 'furby':1}


def tally(input):
    output = {}
    for item in input:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1
    return output


#tests
def test_returns_empty_dict_when_passed_empty_list():
    expected = {}
    result = tally([])

    assert result == expected

def test_assigns_property_for_single_item():
    expected = {'dog': 1}
    result = tally(['dog'])

    assert result == expected

def test_assigns_properties_for_multiple_items():
    expected = {'dog': 1, 'cat':1}
    result = tally(['dog', 'cat'])

    assert result == expected


def test_increments_count_for_multiple_occurences():
    expected = {'dog': 1, 'cat': 3}
    result = tally(['dog', 'cat', 'cat', 'cat'])

    assert result == expected

