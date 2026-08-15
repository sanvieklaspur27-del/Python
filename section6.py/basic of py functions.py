def say_hello():   #hello are you
    print("hello")
    print('are')
    print('you')
    say_hello()

def say_hello(name):  #hello jose
    print(f'hello{name}')
    say_hello('jose')
    print (say_hello)

def add_num(num1,num2):
    return num1+num2
    add_num(10,20)

