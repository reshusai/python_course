__author__ = 'Kalyan'

notes = '''
Implement a left binary search and write exhaustive tests for the same. Left binary search returns the index of left most
element when a search key repeats. For e.g if input is [1,2,3,3,4,4,5] and I search 3, it should return 2 as index 2 is
the left most occurance of 3.

In [1,1,1,1,1,1,1,1], I search for 1, you should return 0.

Note that we are looking for a binary search => we want not more than log(N) lookups, so a solution that involves finding
a random 1 and then doing a linear scan to the left is not a solution :).

- input is an indexable, value is any object.
- return -1 if not found or index of 1st occurance if found.
'''


def left_binary_search(input, value):
    l = 0
    m = 0
    h = len(input)-1
    if(input[l]==value):
        return -1
    else:
        while (l<=h):
            m = (l+h)//2
            if (input[m] < value):
                l = m+1
            elif (input[m] > value):
                h = m-1
            else:
                return m
                break
        else:
            return -1
    pass

# write your own exhaustive tests :)
def test_left_binary_search_student():
    assert 2 == left_binary_search([1,2,3,4,4,5,5], 3)
    assert -1 == left_binary_search([5,6,7,8,9,10], 5)
    assert -1 == left_binary_search([5,6,7,8,9,10], 11)
    assert 2 == left_binary_search([2,3,5,7,11,13,17], 5)
    assert -1 == left_binary_search([1,3,5,7,9,11], 2)
    pass


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_left_binary_search_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_left_binary_search(left_binary_search)
