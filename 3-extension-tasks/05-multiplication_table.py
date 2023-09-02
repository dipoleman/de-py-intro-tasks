# Create the function multiplication_table. It should accept an integer and generate a dictionary representing its multiplication table up to 5.
# The key should be a tuple representing the two numbers being multiplied, the value should be product of those two numbers.
# eg. multiplication_table(5) => {(1, 5): 5, (2, 5): 10, (3, 5): 15, (4, 5):20, (5, 5): 25}




def multiplication_table(num):
    output = {}
    for i in range(1,6):
        output[(i,num)] = i * num
    return output


#test
def test_one_times_table():
    expected = {(1, 1): 1, (2, 1): 2, (3, 1): 3, (4, 1): 4, (5, 1): 5}
    result = multiplication_table(1)

    assert result == expected

def test_five_times_table():
    expected = {(1, 5): 5, (2, 5): 10, (3, 5): 15, (4, 5):20, (5, 5): 25}
    result = multiplication_table(5)

    assert result == expected
