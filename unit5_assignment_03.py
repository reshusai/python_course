__author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    first = set(first)
    second = set(second)
    for i in first:
        if i not in second:
            return False
    else:
        return True
    pass


# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("treat","eatrt")
    assert True == are_anagrams("student","stutend")
    assert True == are_anagrams("pit", "tip") #sample test.
    assert False == are_anagrams("hello","hi")
    assert False == are_anagrams("sai","hai")


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
