__author__ = 'Kalyan'

from placeholders import *


profiling_timeit = '''
Python also gives a helpful timeit module that can be used for benchmarking a given piece of code

Reading material:
 http://docs.python.org/3/library/timeit.html
 http://stackoverflow.com/questions/8220801/how-to-use-timeit-correctly
 http://www.dreamincode.net/forums/topic/288071-timeit-module/

Try out on sample code snippets from above links on your own before you get to the assignment.

Generally you will study performance as you vary the input across a range e.g. count = 10, 100, 1000, 10000

profile the 4 methods in unit8_conversion_methods.py using timeit in this assignment.

for each value of count, execute the method 5 times using timeit and print out the min value and the actual 5 values.
output should look like (a total of 16 lines):
numbers_string1, count = 10, min = 0.0001, actuals = [0.0001, 0.0002, 0.0001, ...]
numbers_string1, count = 100, min = 0.002, actuals = [0.002, 0.002, 0.003, ...]
....
numbers_string4, count = 10000, min = 0.1 actuals = [....]

'''
import unit8_conversion_methods
import timeit
def fun():
    result = []
    for i in dir(unit8_conversion_methods):
        if type(getattr(unit8_conversion_methods,i)).__name__ == "function":
            result.append(getattr(unit8_conversion_methods,i))
    return result

def profile_timeit():
    value = 1
    r = fun()
    print(r)
    for i in r:
        value = 1
        for j in range(4):
            value *= 10
            li = []
            for k in range(5):
                li.append(timeit.timeit(i(value), number=100))
            m = min(li)
            print(i.__name__, value, m, li)


# write your findings on what you learnt about timeit, measuring perf and how the results here compare to
# values in assignment1
summary = '''
i dont understand whats happening whether it is taking less time or more?

'''

if __name__ == "__main__":
    profile_timeit()
