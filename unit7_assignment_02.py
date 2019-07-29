__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""
import signal
import sys

def vowco(p):
    a = p.split()
    t = ["a","e","i","o","u"]
    for i in a:
        co = 0
        for j in i:
            if i[0]==i[0].capitalize():
                co += 6
            if j not in t:
                i = i[1:] + i[:1]
            if j in t:
                i = i + "ay"
                break
        if "," in i:
            m = i.index(",")
            i = i[:m] + i[m + 1:]
            i = i + ","
        if "." in i:
            m = i.index(".")
            i = i[:m] + i[m + 1:]
            i = i + "."
        if co!=0:
            i = i.capitalize()
        print(i)

if __name__ == "__main__":
    #sys.exit(main())
    try:
        while True:
            vowco(input())
    except KeyboardInterrupt:
        print("bye")
        sys.exit(0)
