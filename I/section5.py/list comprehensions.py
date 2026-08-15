#list comprehensions 
mystring= 'hello'
mylist=[]
for letter in mystring:
    mylist.append(letter)
print(mylist)   #['h'.'e','l','l','o']

#or
mylist=[letter for letter in mystring]
print(mylist)

mylist=[x for x in 'word'] #x is any number
print(mylist)    #['w','o','r','d']

mylist=[x for x in range(0,11) if x%2==0] #0,2,4,8,10
print (mylist)     #[12345678910]

celcius=[0,4,16,40,100]
fahrenheit=[((9/5)*temp+32)for temp in celcius]
print(fahrenheit)

#or
fahrenheit=[]
for temp in celcius:
 fahrenheit.append(((9/5)*temp+32))
print (fahrenheit)

#usage of if and else statments
resultS=[[x] if x%2==0 else 'ODD'for x in range(0,11)]
print(result)

mylist=[]

for x in [2,4,6]:
 for y in [100,200,300]:
    mylist.append(x*y)
print (mylist)