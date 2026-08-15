#.format() method is used to format strings in Python. It allows you to insert values into a string using placeholders.
print('this is a string{}'.format(' inserted'))  # using the format method to insert a string into another string

print( 'The {} {} {}'.format('fox', 'brown', 'quick'))  # using the format method to insert multiple values into a 
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))  # using the format method with positional arguments to insert values in a specific 
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))  # using the format method with the same positional argument multiple 

print('the {q} {b} {f}'.format(f='fox', b='brown', q='quick'))  # using the format method with keyword arguments to insert values into a 

#float formating
result = 100/777
print(result)
print('the result was {}'.format(result))  # using the format method to insert a variable into a string
print('the result was {r:10.3f}'.format(r=result))  # using the format method to format a float to 3 decimal 

#f strings
name = 'Sanvi'
print(f'Hello, my name is {name}')  # using an f-string to insert a variable into a string
name = 'sanvi' 
age=19
print(f'{name} is {age} years old')  # using an f-string to insert multiple variables into a string
''