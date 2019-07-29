__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys

def lent(r):
    res = []
    for i in r:
        re = sorted(i, key=lambda j: (j.lower()))
        res.append(re)
    res.sort(key=lambda i: i[0].lower())
    p = sorted(res,key=len, reverse = True)
    return p

def ana(f):
    l = []
    for i in f:
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

if __name__ == "__main__":
    pass
    #sys.exit(main())
    source = input()
    destination = source.split(".")[0] + "-results.txt"
    anagram_sort(source, destination)

