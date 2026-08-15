name = "Sanvi"
# name[0]='p'
last_letters = name[1:]  # slicing the string to get all characters except the first one
print(last_letters)
print('p' + last_letters)  # concatenating 'p' with the sliced string

x='hello world'
x= x + (x+' its a beautiful day')  # concatenating two strings
print(x)

letter='z'
print(letter*10) # printing the letter 'z' ten times

2+3
print(2+3)  # printing the result of the addition
'2'+'3'  # this is a string concatenation, not addition
print('2'+'3')  # printing the result of string concatenation

x='hello world'
x.upper()  # converting the string to uppercase
print(x.upper())  # printing the uppercase version of the string

x.lower()  # converting the string to lowercase
print(x.lower())  # printing the lowercase version of the string

x.split()  # splitting the string into a list of words
print(x.split())  # printing the list of words obtained from splitting the string
x='hi this is a string'
print(x.split())
print(x.split('i'))  # splitting the string at every occurrence of 'i'
