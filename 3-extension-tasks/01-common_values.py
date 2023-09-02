# Create the function common_values which returns a set of values present in the two passed lists.
# eg.  common_values([1, 4, 'dog'],['dog', False, 2, 1]) => {1, 'dog'}


def common_values(list1,list2):
   set1 = set(list1)
   set2 = set(list2)
   return set1.intersection(set2)

#tests
def test_returns_empty_set_for_empty_lists():
    expected = set()
    result = common_values([],[])

    assert result == expected

def test_returns_common_value_in_same_postion():
    expected = {'a'}
    result = common_values(['a'], ['a'])

    assert result == expected

def test_returns_common_value_in_different_postion():
    expected = {'a'}
    result = common_values(['a'], ['b', 'a'])

    assert result == expected

def test_returns_common_values_for_longer_lists():
    expected = {1, 'dog'}
    result = common_values([1, 4, 'dog'], ['dog', False, 2, 1])

    assert result == expected