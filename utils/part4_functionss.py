def fun(*args,**kwargs):
    print(args)
    print(kwargs)


def display_value(x):
    print("printing x"+x)


# *args positional arguments, *pargs positional tuple , **kwargs keyword arguments or dictionaries
def func(a,**pargs):
    print(a,pargs)

# function acting as a variable
x = func

""" along with def statement, lambda expression also generates function objects without having a name. Thats why its
 called as anonymous function. also because lambda is an expression and not a statement it can appear inside the 
 list"""

def f1(x,y,z): return x+y+z
f2 = lambda x,y,z: x+y+z

"""because lambda are expressions that can be called as function objects, they
can be stored in lists and can be iteration with another list of arguments to return results"""


list_lambdas = [lambda x: x**2, lambda x:x**3,lambda x:x**4]

# they can also be treated as dictionary of values

dict_lambdas = {
    'one' : (lambda: 2*1),
    'two': (lambda: 2*2),
    'three': (lambda: 2*3),

}

# this ability basically can help to apply a function if the row contain particular value and so on

def func1(func,a,**pargs):
    func(a,**pargs)


# lambdas can also be nested inside a function that can dynamically change a function based on input

def action(x):
    return lambda y: x+y

# lambda also make it quite easier to apply a function on the sequences using map operation

list_x = [1,2,3,4,5]
list_y = [1,2,3,4,5]

list(map(lambda x: x*2, list_x))
