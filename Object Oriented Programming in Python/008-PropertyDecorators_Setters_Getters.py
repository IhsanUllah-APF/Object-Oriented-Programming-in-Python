# Bismillah

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property # will allow us to access method, email(), like attribute without ().
    def email(self):
        return f'{self.first}.{self.last}.@gmail.com'

    @property # will allow us to access method, fullname(), like attribute without ().
    def fullname(self):
        return f'{self.first} {self.last}'
    @fullname.setter # note that fullname has been used as a property and then used the same for setter.
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        return f'{self.first} {self.last}'
    
    @fullname.deleter
    def fullname(self):
        print('Delete the fullname')
        self.first = None
        self.last = None



emp_1 = Employee('John', 'Smith')

# emp_1.first = 'Jim'

# print(emp_1.first) # printed john as expected.
# print(emp_1.email) # printed john.smith@gmail.com as expected.
# print(emp_1.fullname()) # printed john smith as expected.

# now change the first name above
# print(emp_1.first) # printed jim as expected
# print(emp_1.email) # printed john.smith@gmail.com as UNEXPECTED
# print(emp_1.fullname()) # printed Jim Smith as expected.
# changing first name from john to jim changes the first name attribute of object, emp_1, from john to jim. 
# changing first name from john to jim does not re-run __init__() so the email already set when __init__() was run
# when emp_1 was created remains the same.
# fullname() is a method and when called takes the first name, which is now jim, and last name which is smith and 
# returns both jim smith. 

# like fullname(), we can make a method above which will give an email with updated first and last names.
# print(emp_1.first)
# print(emp_1.email()) # now everyone using our class, Employee, have to access email using method, email(), rather
# # than accessing email as attribute of emp_1. Thus, everyone has to put () after email in this print function.
# print(emp_1.fullname())
# now everything has been printed as it should. But the problem is everyone using our class, Employee, has to add
# () in the second print statement above which we do not want. for this purpose, we will use property decorator, which
# will let us access the email as attribute though it is a method of the class.

#print(emp_1.email) # note that we don't have to use () now since the property decorator makes us able to access
# email now as attribute though it is a method.

# setters now:
# print(emp_1.fullname()) # will print the full name, John Smith without using an setters.

# set the property and setter above now.
# emp_1.fullname = 'Ihsan Ullah' # will call the method fullname in a setter above without typing (). The setter will
# split Ihsan and Ullah, and save Ihsan in firt and Ullah in the last and will return Ihsan Ullah as full name. The
# won't serve any purpose though. Without return we can print the same output 'Ihsan Ullah' as full name.
# print(emp_1.fullname) # will call the method fullname in property above without typing () which will return 'Ihsan 
# Ullah' as the full name to the print, which will get it printed.
# print(emp_1.first) # will print Ihsan as the first name
# print(emp_1.email) # will print Ihsan.Ullah@gmail.com as the email address. So everything changed from John Smith
# to Ihsan Ullah through setter and property.

# deleter to let us say delete full name of emp_1.
del emp_1.fullname
print(emp_1.first) # printed None
print(emp_1.last) # printed None
print(emp_1.fullname) # printed None None
