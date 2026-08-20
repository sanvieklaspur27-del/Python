class Dog():
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self,breed,name):
            #Attributes
            #We take in the argument
            #Assign it using self.attribute_name
            self.breed=breed
            self.name=name
           


     #OPERATIONS/ACTIONS------> Methods
    def bark(self,number): 
          print("WOOF! My name is {} and the number is {}" .format(self.name,number))  

my_dog=Dog('Lab','Sam')   
print(my_dog.species)    #mammmal    
print(my_dog.name)   #sam
print(my_dog.bark(10)) #WOOF! My name is Sam and the number is 10



class Circle():
      #CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):
          self.radius = radius
          self.area = radius*radius*Circle.pi  #or self.pi

    #METHOD
    def get_circumference(self):
          return self.radius * Circle.pi * 2  #or self.pi

my_circle=Circle(30)
print(my_circle.pi)  #3.14
print(my_circle.radius) #30
print(my_circle.area)  #2826.0
print(my_circle.get_circumference())  #188.4


