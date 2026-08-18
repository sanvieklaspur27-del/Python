# *args (returns tuples)
#arguments and keyword arguments

def myfunc(a,b):
    #Returns 5% of the sum of a and b
    return sum((a,b))*0.05
print(myfunc(40,60))  # 5

def myfunc(*args):
    return sum(args)*0.05
print(myfunc(40,60,100,100,100))

def myfunc(*args):
    print(args)
    print(myfunc)

def myfunc(*args):
    for item in args:
        print(item)
        print(myfunc(40,60))

#**Kwargs (returns dict)

def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is{}'.format(kwargs['fruit']))
    else:
        print('i didnot find fruit')
        myfunc(fruit='apple',veggie='lettuce')
        print(myfunc) # my fruit of choice is apple

#combination
def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
    myfunc(10,20,30,fruits='orange',food='eggs',animal='dog')
    print(myfunc)

    