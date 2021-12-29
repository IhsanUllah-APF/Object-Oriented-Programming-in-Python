# Bismillah

# Regular methods: Received 'self' as an argument and are accessed at the instance level.

# Class methods: Received 'cls' as an argument and are accessed at the class level.

# Static methods: Do not require 'self' or 'cls' as an argument. They behave like isolated functions. 

# Different methods (regular, class, static) are used to alter the behaviour/functionality of a method.

class Employee:
    num_of_employees = 0 # a class variable and can be accessed at the instance or class level. It should measure
    # such a trait that does not vary from an instance to instance.
    raise_amount = 1.04 # also a class variable.

    def __init__(self, first, last, pay): # regular method
        self.first = first
        self.last = last
        self.email = first + '.' + last + 'gmail.com' # note that email doesn't exist in arguments. Also, note that
        # only dot and gmail.com are enclosed in '' and + is not enclosed in string.
        self.pay = pay

        Employee.num_of_employees = +1 # the class variable accessed at the class level.

    def fullname(self):
        return f'{self.first} {self.last}' 

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    # only raise_amount will give error due to lack of specifying where to look for this attribute.
    
    @classmethod
    def set_raise_amount(cls, amount): # note that a class method can take arguments other than cls as well.
        cls.raise_amount = amount # set the class variable, raise_amount, equal to the amount received as argument.


# create instances, emp1 and emp2, of the class Employee.
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(Employee.raise_amount) # accessing class attribute at class level.
print(emp1.raise_amount) # accessing class attribute at the instance, emp1, level.
print(emp2.raise_amount) # accessing class attribute at the instance, emp2, level.
# since the class attribute, raise_amount, is a variable and initally set to 1.04 and has not been modified yet,
#therefore, in all three cases, it prints its value, 1.04.

# call the class method now.
Employee.set_raise_amount(1.05) # the class, Employee, is passed as argument automatically for cls.
# the method, set_raise_amount, will update the value in the class attribute, raise_amount, from 1.04 to 1.05. 
# calling the classmethod at class level. It can be called at the instance, emp1, level as well.

# repeat the above 3 print statements.
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
# prints 1.05 in all 3 cases as it should.







################## This work belongs to class and instance attributes/variables ###############################
# print the first, last and full name of the instance, emp1.
# print(emp1.first) # the instance attribute (it will vary for each employee) accessed at the instance level.
# print(emp1.last) # the instance attribute accessed at the instance level.
# print(emp1.fullname()) # regular function accessed at instance level.

# print the number of employees accessing the class attribute at the instance, emp1, and class level.
# print(emp1.num_of_employees) # class attribute, since it doesn't vary from one employee to another, accessed at 
# the instance level
# print(Employee.num_of_employees) # class attribute accessed at class level.

# Summary: Instance attribute/variable should be the one that varies from one instance of a class to another instance.
# It can be accessed at the instance level.
# Class attribute/variable should be such that it does not vary from one instance of a class to another instance. It
# can be accessed at both class and instance level. When called at instance level, first the attribute is searched
# among the instance attributes. If not found, then it is searched in the class attributes and found there.

# print the instance, emp1, and class, Employee, attributes.
# print(dir(emp1)) # the class attributes are also listed among the instance attributes.
# print(dir(Employee)) # function, fullname, and variables, num_of_employees and raise_amount, are included among
# the class attributes.

# call the method, apply_raise().
# emp1.apply_raise()
# print(emp1.pay)

################ class and instance attributes/variable ends here ##############################################

