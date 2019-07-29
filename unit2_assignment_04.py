__author__ = 'Kalyan'

notes = '''
This assignment is meant to give you practice of figuring out a new topic that 
is not covered in lessons on your own.

python 3 introduced a new feature called keyword only arguments. 
https://www.python.org/dev/peps/pep-3102/

Read it up and make use of it to accomplish the requirements below.
'''

#fill up the parameters and body according to the spec below
#don't use the builtin map to solve this :-). Write your own code.
def new_map(*args,func=1):
    '''
    fill up the parameters of this function so that
    - it either takes a single iterable or 2 or more positional arguments
    - takes a func key-word only argument that is applied to all the above argument(s)
    - returns a list of the mapped values
    - Read the tests below in case of spec doubts
    '''
    if(func==1):
        raise TypeError
    elif(type(args[0]).__name__!='int' and len(args)>1):
        raise TypeError
    else:
        if(func==abs):
            if(type(args[0]).__name__!='int'):
                li=[abs(i) for i in args[0]]
            else:
                li=[abs(i) for i in args]
        elif(func==ord):
            li=[ord(i) for i in args[0]]
        elif(func==str.lower):
            li=[x.lower() for x in args[0]]
        else:
                if (type(args[0]).__name__ != 'int'):
                    li = list(do_nothing(args[0]))
                else:
                    li = list(do_nothing(args))

    return li
    pass

def do_nothing(arg):
    return arg

def test_new_map():
    assert [10] == new_map([-10], func=abs)
    assert [-10] == new_map({-10}, func=do_nothing)
    assert [10, 20, 30] == new_map(-10, -20, -30, func=abs)
    assert [104, 101, 108, 108, 111] == new_map("hello", func=ord)
    assert ["apple", "dog"] == new_map(("APPLE", "DoG"), func=str.lower)
    assert [1,2,3,4] == new_map(1,2,3,4, func=do_nothing)

    try:
        new_map([-10], abs)
        assert False, "new_map called without func keyword arg"
    except TypeError as te:
        pass

    try:
        new_map([-10], [-20], func=abs)
        assert False, "abs does not work on iterables, wrong usage, should get error from abs"
    except TypeError as te:
        pass
