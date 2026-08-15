#Useful operators
mylist=[1,2,3]
for num in range(10):    #iterating 1...to 9
 print(num)

for num in range(3,10):   # 1.....3 10 9
 print(num)

for num in range(0,10,2):   #0,2,4,6,8
 print (num)

for num in range(0,11,2):   #0,2,4,6,8,10
 print(num)

list(range(0,11,2))
print(list(range(0,11,2)))   #[0,2,6,8,10]

# indexing
index_count=0
for letter in 'abcde':
 print('At index {} the letter is {}'.format(index_count,letter))
 index_count+=1      #At index 0 the letter is a
                     # At index 1 the letter is b

#or
index_count=0
word='abcde'
for letter in word:   #a,b,c,d,e
 print(word[index_count])
 index_count += 1

 #enumerates
 word='abcde'
for item in enumerate (word): #(0,'a') (1,'b')
 print(item)

#or
word='abcde'
for index,letter in enumerate(word): 
 print(letter)
 print(index)
 print('\n')   #a0,b1,c2,d3,e4

#zipping
mylist1=[1,2,3]
mylist2=['a','b','c']
for item in zip(mylist1,mylist2):
 print(item)    #(1,'a'),(2,'b'),(3,'c')

 list(zip(mylist1,mylist2))
print (list(zip(mylist1,mylist2))) #horizontal list

#checking whether the letter is in dict
'x' in ['x','y','z']
print('x' in ['x','y','z'])  # True

2 in [1,2,3]
print(2 in [1,2,3])   #True

mylist =[10,20,30,40,100]
print(min(mylist))   #min of mylist is 10
print(max(mylist))   #max of mylist is 100

#Randonm libraray (none type)
from random import shuffle
mylist=[1,2,3,4]
shuffle(mylist)   # shuffling [2,3,4,1]
print (mylist)

#Randon integer
from random import randint
randint(0,100)           #72
print (randint(0,100))  # any random inetger

mynum=randint(0,10)
print(mynum)     #6 , saving mynum

input('Enter a number:')
result=input('Enter a number')

type(result)
print(type(result))  #str
