# Bismillah

# __repr__() and __str__() are used to print more meaningful output. There are other dunder methods for addition,
# subtraction, finding length etc.


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@gmail.com"

    def fullname(self):
        return f'{self.first} {self.last}' 
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employe('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return int(self.pay) + int(other.pay) 
        # int written otherwise the pays are assumed to be strings and 50006000 is returned as they are cancaded.

    def __len__(self):
        return len(self.fullname()) # = len(emp_1.fullname()). emp_1 is instance of Employee. So, the method 
        # fullname() will be search in Employee class and will be called for its instance, emp_1. (emp_1.fullname())
        # will return Corey Schafer to the method len() which will return 13 to the print() from where __len__() has
        # been called.


emp_1 = Employee('Corey', 'Schafer', '50000') # emp_1 is the instance/object of class, Employee.
emp_2 = Employee('Test', 'User', '60000')
# print(emp_1) # it will print memoray location of the instance, emp_1.

# without __str__()
# print(emp_1) 
# it will print first name, last name and pay of the instance, emp_1, rather than memory location of the instance.
# the __repr__() is called from print() which returns first name, last name and pay of the instance, emp_1.

# with __repr__() and __str__()
# print(emp_1)
# __str__() is called and the content returned by __str__() is printed. __repr__() is not called.

# if we want to call __repr() when __str__() is also present, then we should specifically call __repr__() as:
# print(emp_1.__repr__())
# similarly, __str__() can also be called as:
# print(emp_1.__str__())

# other dunder methods
# print(1 + 2) # it automatically calls int.__add__(int x, int y) method.
# print(int.__add__(1, 2))
# both gives the same result, 3, as it should.

# print('a' + 'b')
# print(str.__add__('a', 'b'))
# both gives the same result, ab.

# create another instance of Employee class, emp_2.
# without __add__() method defined:
# print(emp_1 + emp_2) # will give error since Python doesn't know how to add two instances.

# now define __add__() method above.
# print(emp_1 + emp_2) # + sign calls the __add__() method.

# length dunder method:

# print(len('test'))
# print('test'.__len__())
# both give the same result, 4, which is the length of the string, test.

# before dunder len():
# print(emp_1.__len__()) # it will give error that the instance of class Employee, emp_1, has no attribute __len__().

# define our own dunder length method above and then use it in the following
print(emp_1.__len__()) # prints 13 as it should.

