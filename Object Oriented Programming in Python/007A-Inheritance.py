# Bismillah

# inheritance allows us to inherit attributes and methods from a parent class.

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@gmail.com"

    def fullname(self):
        return f'{self.first} {self.last}' 
    # since first and last are not passed here as arguments, therefore, they must accessed at an instance level.

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

class Developer(Employee): # Devleoper is a subclass of Employee class
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # super dot init passess the arguments to the init method in Employee 
        # class for initialization of an instance of Developer class for the given arguments.
        # Employee.__init__(self, first, last, pay) # is the alternative way to super dot init.
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees): # employees contains a list of employees.
        Employee.__init__(self, first, last, pay)
        self.employees = employees # self.employees/manager_1.employees will contain the list of employees

    def add_emp(self, employee):
        self.employees.append(employee)

    def remove_emp(self, employee):
        self.employees.remove(employee) 
    
    def print_emps(self):
        for employee in self.employees: # employee = dev_1 from self.employees = [dev_1, dev_2]
            print('-->', employee.first) # dev_1.first = Ihsan. Same for dev_2.
       

# when Developer sub-class has only pass in its body.
dev_1 = Developer('Ihsan', 'Ullah', 100000, 'Python') # create object of the child class, Developer.
dev_2 = Developer('Jamal', 'Khan', 200000, 'Java')
# will first look for init method in the child class, Developer, but when it can't find init method there, then Python
# will look for it up in the inheritance chain including parent class, Employee, until it finds it and then executes 
# it.
# print(dev_1.first)
# print(dev_2.email)

# To see method resolution order and what methods and attributes the child class, developer, has inherited from the
# parent class, Empoloyee.
# print(help(Developer)) 

# print(dev_1.pay) # printed 100,000
# dev_1.apply_raise() # raise_amount is used from Employee class since Developer class yet doesn't have this attribute.
# print(dev_1.pay) # printed 104,000

# after setting raise_amount = 1.10 in the subclass, Developer.
# print(dev_1.pay) # printed 100,000
# dev_1.apply_raise() # now attribute, raise_amount, has been used from the Developer class rather Employee class.
# print(dev_1.pay) # printed 110,000

# change dev_1 above to an instance of Employee class rather than instance of Developer class.
# print(dev_1.pay) # printed 100,000
# dev_1.apply_raise() # applied raise_amount = 1.04 from Employee class since dev_1 is not instance of Employee class.
# print(dev_1.pay) # printed 104,000
# it proves that the change in raise_amount = 1.10 in Developer class from raise_amount = 1.04 in Employee class has 
# no effect on attribute (raise_amount) as well as on the methods of the Employee class.

# after pass has been replaced in Developer class with init method (constructor)
# print(dev_1.email)
# print(dev_2.prog_lang)
# first, last, pay and email are initialized through the init constructor in the parent class, Employee, and the prog
# language is initialized within the child class, Developer.

# Another child class, Manager:
manager_1 = Manager('Sue', 'Smith', 90000, [dev_1]) # dev_1 is an object itself.

# print(manager_1.first) # initialization of first name will be done through __init__ in Employee class.
# print(manager_1.fullname()) # will access the method, fullname, in Employee class.
# #print(manager_1.employees) # will print address of the meory location of object, dev_1.
# manager_1.print_emps()
# manager_1.add_emp(dev_2)
# manager_1.print_emps()
# manager_1.remove_emp(dev_1)
# manager_1.print_emps()

# some built-in useful functions:
# print(isinstance(manager_1, Manager)) # returns True since manager_1 is an instance of child class, Manager.
# print(isinstance(manager_1, Employee)) # returns True since manager_1 is also an instance of parent class, Employee.
# print(isinstance(manager_1, Developer)) # returns False since manager_1 is not an instance of class, Devloper.
# print(issubclass(Manager, Employee)) # returns True as it should.
# print(issubclass(Developer, Employee)) # return True as it should.
# print(issubclass(Manager, Developer)) # returns False as it should. 

