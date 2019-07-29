__author__ = 'Kalyan'

max_marks = 20

notes = '''
This is the counterpart to the encrypt routine that you wrote in problem 3. 

You are given the encrypted string, the original key used to encrypt the original string.

Your job is to reconstruct the original string.

Notes:
1. raise TypeError if text is not a str or key is not EncryptKey
2. raise ValueError if the grid is invalid (ie) cannot accomodate the text  or if rows/cols are <= 0 
3. returns the original string (remove the padding chars).
4. You can assume that the original string does not contain the padding chars
5. see the definitions for Corner and EncryptKey in mock1common.py

'''

from mock1common import EncryptKey, Corner

def decrypt(encrypted_text, key):
    pass

# a basic test is given, write your own tests based on constraints.
def test_decrypt():
    assert "how are you?" == decrypt("ao***?urhow y e", EncryptKey(3, 5, Corner.TOP_RIGHT))