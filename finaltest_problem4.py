__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
A chain of words is defined as a sequence of words w1, w2, .. wn where each of the words is formed by removing exactly
one letter from the previous word. Each of the words w2, ... wn need to valid words as given in the dictionary file 
(final_words.txt)

For e.g. once -> one -> on is valid chain start with once.    

Your job for this problem is to write a routine that given a word returns the longest chain of words starting with 
a given word. [valid words are words in the given file - final_words.txt ].  

If multiple chains are possible, pick the one that has words which are earlier in the alphabet ordering.

For e.g meat -> met -> me and meat -> eat -> at are valid longest chains of length 3 starting with meat. 
If these are the only 2 longest chains return [meat, eat, at] as eat comes before met in the alphabet ordering.

Notes:
1. Raise TypeError if word is not a string
2. Return a list of words including the original word (all in smaller case even if original is mixed case)
3. If the word has no chains just return the word in the list (chain of length 1).
4. Use the open_input_file helper routine given to open the file. The current directory will not be your folder 
   and you will not find the file if you do not do this.
5. Do not read the file multiple times in your implementation (once per invocation is fine, though in general if 
you write this as a cli tool, you will load once and run the queries multiple times)!
6. DO NOT SUBMIT the words file, we will add it at our end.
'''

import os
import inspect

# helper routines...
def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir


def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)


# Important USE the open_input_file routine given above to open the "final_words.txt".
def get_longest_chain(word):
    pass


def test_get_longest_chain():
    assert ["small", "mall", "all"]== get_longest_chain("small")