__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string
def lent(r):
    result = []
    for i in r:
        re = sorted(i, key=lambda j: (j.lower()))
        result.append(re)
    result.sort(key=lambda i: i[0].lower())
    p = sorted(result,key=len, reverse = True)
    return p

def ana(fi):
    l = []
    for i in fi:
        if ("#" not in i and i != '\n'):
            l.append(i)
    l= [i.strip() for i in l]
    for i in l:
        re = [sorted(j.lower()) for j in l]
    li = []
    for i in range(len(re)):
        m = []
        if re[i] == "#":
            continue
        m.append(l[i])
        for j in range(i + 1, len(re)):
            if re[i] == re[j]:
                m.append(l[j])
                l[j] = "#"
                re[j] = "#"
        if m != []:
            li.append(m)
    li = [sorted(i) for i in li]
    li = lent(li)
    return li

def anagram_sort(source, destination):
    with open(source) as f:
        fi = f.readlines()
        lis = ana(fi)
    d = open(destination, "w")
    for i in lis:
         k = [d.write(j + "\n") for j in i]
    f.close()
    d.close()
    pass

def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
