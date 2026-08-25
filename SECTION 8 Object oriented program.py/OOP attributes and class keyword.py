mylist=[1,2,3]
myset=set()
print(type(myset))  #set
print(type(mylist))  #list

class Sample():  #created a sample class
    pass

my_sample=Sample()
print(type(my_sample))  #__main__.Sample

class Dog():

    def __init__(self,breed,name,spots):
        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed=breed
        self.name=name
        #Expect boolean True/False
        self.spots=spots

my_dog=Dog(breed='Lab' ,name='Sammy' ,spots=False)
print(type(my_dog))  #__main__.Dog
print(my_dog.breed)  #Lab
print(my_dog.name)   #Sammy
print(my_dog.spots)  #False 


class Dog():

    def __init__(self,mybreed):
        self.breed=mybreed
my_dog=Dog(mybreed='Huskie')
print(type(my_dog))  
print(my_dog.breed)  #Huskie


