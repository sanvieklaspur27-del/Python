my_list=[1,2,3]
my_list=['a','b','c','d']

print(len(my_list))  # printing the length of the list
print(my_list[0])  # printing the first element of the list
print(my_list[1:])  # printing all elements of the list except the first 

another_list=['e' , 'f']
my_list+another_list  # concatenating two lists
print(my_list+another_list)  # printing the concatenated 

new_list=my_list+another_list  # creating a new list by concatenating two lists
print(new_list)  # printing the new concatenated list

new_list[0]='z'  # changing the first element of the new list
print(new_list)  # printing the modified new list

new_list.append('g')  # appending/adding a new element to the end of the list
print(new_list)  # printing the list after appending a new element

new_list.pop()  # removing the last element from the list
print(new_list)  # printing the list after removing the last element
new_list.pop(0)  # removing the first element from the list
print(new_list)  # printing the list after removing the first element

new_list=['a','f','d','c','e','b']
num_list=[1,5,3,4,2,6]
new_list.sort()  # sorting the list in ascending order
print(new_list)  # printing the sorted list
my_sorted_list=num_list.sort()  # sorting the list of numbers in ascending order
print(num_list)  # printing the sorted list of 
type(my_sorted_list)  # none is returned

num_list.sort()  # sorting the list of numbers in ascending order
print(num_list)  # printing the sorted list of numbers

num_list.reverse()  # reversing the order of the list
print(num_list)  # printing the reversed list of numbers