__author__ = 'Kalyan'

max_marks = 25

problem_notes ='''
Write a routine to sort the given list of numbers according to the number
of prime factors it has.

Constraints:
1. 1 and 0 are considered to have 0 factors
2. For negative numbers, the factor count of the corresponding
   positive numbers is considered for sorting
3. Numbers with more factors come before numbers with fewer factors
4. In case of a tie, bigger numbers (numerically) comes first
5. Return a new sorted list of numbers (not-inplace)
6. Refer to the testcase for an example.

Notes:
1. Use the python built in sorting functionality to get this done.
2. Write additional helper routines as required.
3. Assume that input is valid list of numbers.
'''
def check(num):
    x=2
    while(x<num):
        if(num%x==0):
            return False
        x=x+1
    return True
def nprime(prime):
    value=prime+1
    while(True):
       if (check(value)):
            return value
       value=value+1
def fact_num(number):
    for i in range(len(number)):
        if(number<0 ):
            i=0

        elif(type(number).__name__!='int'):
            raise TypeError
            raise ValueError
        else:
            factors=[]
            prime=1
            while(nprime(prime)<=number):
                k=nprime(prime)
                j=0
                while(number%k==0):
                    number=int(number/k)
                    j+=1
                if(j!=0):
                    factors.append((k,j))
                prime=k

    pass


# assume numbers is a valid list of numbers
def sort_by_factor_count(number):
    li = []
    for i in range(len(number)):
        r = fact_num(number[i])
        li.append(r)
    pass

# one basic test given, write more exhaustive tests
def test_sort_by_factor_count():
    # 10 has 2 factors [2,5] , 6 has 2 [2,3], 8 has 1 [2] and 2 has 1 [2], hence the result
    assert [10, 6, 8, 2] == sort_by_factor_count([2, 8, 6, 10])
