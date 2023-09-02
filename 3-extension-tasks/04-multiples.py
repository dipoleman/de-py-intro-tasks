# Create the function multiples which accepts an integer. It should return a list of all numbers between 1-100 which are divisible by that number.
# eg. multiples(20) => [20, 40, 60, 80, 100]
# eg. multiples(75) => [75]

def multiples(num):
    output = []
    for i in range(1,101):
        if i % num == 0:
            output.append(i)
    return output


#tests
def test_responds_with_list_of_multiples():

    assert multiples(100) == [100]
    assert multiples(99) == [99]
    assert multiples(20) == [20, 40, 60, 80, 100]

