__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    s = "either"
    s1 = "or"
    a = sentence.find(s)
    b = sentence.find(s1)
    if s in sentence and s1 in sentence and a<b:
        result = []
        i=0
        while i < len(sentence):
            if (i==a):
                i = a+7
            elif (i==b):
                break
            else:
                result.append(sentence[i])
                i+=1
        r = "".join([str(j) for j in result])
        return (r[:-1] + ".")
    else:
        return sentence+"."
    pass


def test_prune_either_or_student():
    assert "mocktest will be on 5th." == prune_either_or("mocktest will be either on 5th or on 4th")
    assert "we could go to a movie." == prune_either_or("we could either go to a movie or a hotel")
    assert "it would be a rainy day." == prune_either_or("it would be either a rainy day or a sunny day")
    assert "you do it." == prune_either_or("you either do it or die")
    assert "hello everyone." == prune_either_or("hello everyone")
    assert "selflearning is really cool." == prune_either_or("selflearning is really cool")
    assert "blah or something either somethingelse." == prune_either_or("blah or something either somethingelse")
    pass


# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
