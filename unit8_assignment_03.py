__author__ = 'Kalyan'

profiling_cprofile = '''
This is the tool of choice for analyzing large programs (parallel to the debugger). The profiler adds its own overhead
but for relative comparison of time spent, it is very very useful.

References:
1. https://docs.python.org/3/library/profile.html
2. http://pysnippet.blogspot.in/2009/12/profiling-your-python-code.html

In particular, make sure you learn how to use pstats and running cProfile from command line as described in the
2nd reference using a sample program before doing this assignment.

python -m cProfile [-o output_file] [-s sort_order] myscript.py

For this assignment learn to use the cProfile and pstats modules from the command line.
1. run the cprofile and collect a stats file
2. learn to use the stats file separately.
3. bypass the stats creation and directly print the output to console.

compare the cumulative times of these methods and then calculate per call times.
'''

import unit8_conversion_methods
import cProfile
import pstats
#invoke each of the 4 methods 5 times in a loop for count=10000. Then run this in the profiler and study the output

import unit8_conversion_methods

def fun():
    result = []
    for i in dir(unit8_conversion_methods):
        if type(getattr(unit8_conversion_methods,i)).__name__ == "function":
            result.append(getattr(unit8_conversion_methods,i))
    return result

def profile_profiler():
    li = fun()
    count = 10000
    p = cProfile.Profile()
    for i in li:
        for j in range(5):
            p.enable()
            i(count)
            p.disable()
            p.print_stats()



# compare the times taken per call using this method to what you found in the previous methods.
# when would you use the profiler over other methods, what additional data did you get from the profiler easily
# that would have taken more work in other methods?

# what did you learn about cProfile and pstats?

summary = '''

'''

if __name__ == "__main__":
    profile_profiler()
