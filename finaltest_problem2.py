__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
A palindrome is a word which spells the same from both ends (case-insensitive).  

If a word is not a palindrome, you can make a palindrome out of it by adding letters to either ends of the word.

Your goal is to make a palindrome of the minimum length.

For e.g.  cat is not a palindrome, you can add letters at the ends to make palidromes like catac (ending), cattac (ending), 
taccat (beginning), tacat (beginning), acattaca (both ends). However, of all this the minimum length ones are catac and tacat.
  
Notes:

1. If word is not a str, raise TypeError
2. empty string is considered to be a palindrome.
3. if multiple palindromes of same length are possible, return the one earlier in alphabetical ordering (catac in 
   the example above, keep it case insensitive)
4. Only small letters should be added. The casing of original letters should be unchanged.
5. Write your own tests and test thoroughly.
'''

# returns the min length palidrome defined by the criteria given above.
import string
def make_palindrome(word):
    w = ""
    s = ""
    if(type(word).__name__ != "str"):
        raise TypeError
    elif(word==""):
        return ""
    else:
        if(len(word)%2==0):
            w = word[:len(word)//2]
            s = word[len(word)//2:]
            if(w==s):
                return word
            else:
                r = word + w[::-1].lower()
                re = word[:0:-1].lower() + word
                if(r[0]>re[0]):
                    return re
                else:
                    return r
        else:
            r = word + word[-2::-1].lower()
            re = word[:0:-1].lower()+word
            if(r[0]>re[0]):
                return re
            else:
                return r
    pass


def test_make_palindrome():
    assert "cATac" == make_palindrome("cAT")
    assert "potop" == make_palindrome("pot")
    assert "cAttac" == make_palindrome("cAtt")
    assert "catac" == make_palindrome("tac")
