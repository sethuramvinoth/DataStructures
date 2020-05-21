class MyClass:
    "Description of the Class Comes here!!!"
    a = 10;
    def func(self):
        print('Hi')

print(MyClass.func);
print(MyClass.a);
print(MyClass.__doc__);

# whenever an object calls its method, the object itself is passed as the first argument. So, ob.func() translates into MyClass.func(ob).

# In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument
# list that is created by inserting the method's object before the first argument.

# Creating Objects
class ClassTwo:
    "Class with object"
    a = 5;
    def func(self):
        print('Called by Object')

ob = ClassTwo()
print(ob.a)
print(ob.func())

#Using the Constructors
class Employee:
    "Class using Constructors"
    def __init__(self,id,name): #__init__()gets called whenever a new object of that class is instantiated.
        self.name = name;       #Class functions that begins with double underscore (__) are called special functions as they have special meaning.
        self.id = id;

    def display(self):
        print('This is ',self.name,'with ID',self.id);


emp1 = Employee(100,'Employee_1');
emp1.display();
emp2 = Employee(200,'Employee_2');
emp2.salary=2000
print(emp2.salary)


#Deleting Attributes and Objects

del emp2.salary
del emp2          #On the command del emp2 this binding is removed and the name emp2 is deleted from the corresponding namespace
# emp2.display(); The object however continues to exist in memory and if no other name is bound to it, it is later automatically destroyed.
