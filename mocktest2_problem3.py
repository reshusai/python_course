__author__ = 'Kalyan'

max_marks = 30

problem_notes ='''
This is same as the problem in mock1 with additional constraints on implementation.

This problem deals with a custom encryption/decryption scheme that works as follows. 

Given a string like "how are you?" and m * n grid. The characters of the string are filled 
into the grid row wise top to bottom. So for 3 * 5 you get

h o w _ a
r e _ y o
u ? * * *

In the above example _ is shown visually where there is a space character. Unfilled cells are filled with *'s

The encrypted string is found by starting at a specified corner and going clockwise in 
a decreasing spiral till all the cells are covered. So if corner is top right you get "ao***?urhow y e"

I want you to code this as a decomposition given below. Each of the routines will be independently tested 
and scored. 

You are free to define any additional helper routines that you want.

Notes:
1. raise TypeError if text is not a str or key is not EncryptKey
2. raise ValueError if the grid cannot accomodate the text  or if rows/cols are <= 0 
3. returns the encrypted string as specified above.
4. see the definitions for Corner and EncryptKey in mock2common.py
'''

from mock2common import EncryptKey, Corner

#returns the m x n grid of # chars as a list of lists (each row is a list) with the characters as specified in the example.
def get_grid(text, key):
    li = []; k = 0;l1 = []
    k1 = key[0]*key[1]
    if (len(text) < k1):
        w = k1 - len(text)
        text = text + "*"*w
    for i in range(key[0]):
        l = []
        for j in range(key[1]):
            l.append(text[k])
            k += 1
        li.append(l)
    l1 = key[2](li)
    pass

# define this as a generator function that successively returns the cells as (x,y) coordinates in the traversal
# specified by the key
def get_path(key):
    pass

# calls the helper routines get_grid and get_path and gets the encryption done.
def encrypt(text, key):
    li = []; k = 0;l1 = []
    k1 = key[0]*key[1]
    if (len(text) < k1):
        w = k1 - len(text)
        text = text + "*"*w
    for i in range(key[0]):
        l = []
        for j in range(key[1]):
            l.append(text[k])
            k += 1
        li.append(l)
    pass

# basic tests are given, write your own tests based on constraints.
def test_get_grid():
    assert [['h', 'o', 'w', '*', '*']] == get_grid("how", EncryptKey(1, 5, Corner.TOP_RIGHT))

def test_get_path():
    assert [(0,4), (0,3), (0,2), (0,1), (0,0)] == list(get_path(EncryptKey(1, 5, Corner.TOP_RIGHT)))

def test_encrypt():
    assert "**woh" == encrypt("how", EncryptKey(1, 5, Corner.TOP_RIGHT))
