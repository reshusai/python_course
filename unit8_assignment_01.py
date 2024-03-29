__author__ = 'Kalyan'

profiling_timing = '''
This involves adding sufficient time.perf_counter calls at appropriate places and then calculating difference to calculate
elapsed time.

https://docs.python.org/3/library/time.html#time.perf_counter

This is similar to print debugging, but once you have narrowed down code to a small code section by other means,
this can be very useful and precise.

Generally you will study performance as you vary the input across a range e.g. count = 10, 100, 1000, 10000

profile the 4 methods in unit8_conversion_methods.py using time.clock() in this assignment.

for each value of count, execute the method 5 times and print out the min value and the actual 5 values.
output should look like (a total of 16 lines):
numbers_string1, count = 10, min = 0.0001, actuals = [0.0001, 0.0002, 0.0001, ...]
numbers_string1, count = 100, min = 0.002, actuals = [0.002, 0.002, 0.003, ...]
....
numbers_string4, count = 10000, min = 0.1 actuals = [....]

 Why 5 times and not just once? To get more data and to avoid the effects of noise (the outliers) due to so many things happening 
 on the system (like module imports, garbage collector running etc).
 
 Note: This is a python script which can be run from command line (python.exe <script>.py) or from pycharm (Right click -> Run <script>
 and not the usual pytest tests we have been using so far.
'''

import time
import unit8_conversion_methods

# write clean code to run all the profiles in one go using loops, lists etc. Note that functions are first class objects
# in python so you can hold them in a list.
def fun():
    result = []
    for i in dir(unit8_conversion_methods):
        if type(getattr(unit8_conversion_methods,i)).__name__ == "function":
            result.append(getattr(unit8_conversion_methods,i))
    return result
def profile_perf_counter():
    value = 1
    r = fun()
    for i in r:
        value = 1
        for j in range(4):
            value *= 10
            li = []
            for k in range(5):
                i(value)
                li.append(time.clock())
            m = min(li)
            print(i.__name__,value,m,li)

# write your findings on what is the most optimal method and what you learnt in the process.
summary = '''
the process in the num_strings4 will be executed fst

'''

if __name__ == "__main__":
    profile_perf_counter()
