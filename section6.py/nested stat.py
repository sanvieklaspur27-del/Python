#Nested statements and scope

x = 25
def printer():
    x=50
    return (x)
print(x)            #25
print(printer()) 

#LEGB RULE
#lambda num:num**2
#GLOBAL
name='this i a global string'
def greet():
    #ENCLOSING
    # name='sammy'
    def hello():
        #LOCAL
        # name='im local'
        print('hello'+ name)
    hello()

greet()

print(help(len))

#USING LOCAL AND GLOBAL
x=50
def func(x):
    print(f'X is {x}')
    #LOCAL REASSIGNMENT!
    x=200
    print(f'i just locally changed X to {x}') #X to 200
print(x)    
print(func(x))   #Xis 50
print(x)

x=50

def func():
    global x
    print(f'X is {x}')
    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x='new value'
    print(f'i just locally changed  global X to {x}')
print(x)  #50
print(func()) # ijust..X to new value
print(x)  #new value

x=50
def func(x):
    
    print(f'X is {x}')
    #LOCAL REASSIGNMENT ON A GLOBAL VARIABLE!
    x='new value'
    print(f'i just locally changed  global X to {x}')
    return x
print(x)
print(func(x))
print(x)




