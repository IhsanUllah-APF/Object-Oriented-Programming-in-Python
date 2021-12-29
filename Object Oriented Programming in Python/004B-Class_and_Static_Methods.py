# Bismillah

class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

        Employee.num_of_employees = +1

    # regular method takes the instance as the first argument. It will change the instance attribute only for that
    # instance.
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # class method takes the class, cls, as the first argument. It will change the class attribute for the class and
    # all the instances even if called at instance level.
    @classmethod
    def set_raise_amount(cls, amount):
        Employee.raise_amount = amount

    # using class method as an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') # parse the string here now.
        return cls(first, last, pay) 
        # cls contains Employee, the class name, so this is calling the constructor which will create an instance
        # and return it.

    # static methods do not automatically take an instance or class as the first argument. They are like isolated
    # functions but are included in a class because they have some logical connection with a class such as if a 
    # particular date was a workday may have logical connection with the Employee class.
    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6: # in Python 0 = Monday and 6 = Sunday with all other dates in
            return f'The date is a weekend'            # between.
        else:
            return f'The date is a week day'
    # such method should be made a static method which never needs to be called at instance or class level.




emp_str_1 = 'John-Doe-70000'        


emp1 = Employee('Ihsan', 'Ullah', 100000)
emp2 = Employee('Jamal', 'Khan', 200000)

# before calling the class method, set_raise_amount
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# printed 1.04 for all as it should.

# now call the class method at the class level.
Employee.set_raise_amount(1.05) # Employee passed as an argument for cls.

# after calling the class method.
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# printed 1.05 for all as it should.

# now call the class method at instance level.
emp1.set_raise_amount(1.10) 
# emp1 passed as an argument for cls. No error given. It means class method like class
# attribute can be called at instance level.

# after calling the class method at instance level.
# print(Employee.raise_amount) # printed 1.1 unexpected
# print(emp1.raise_amount)     # printed 1.1 expected
# print(emp2.raise_amount)     # printed 1.1 unexpected
# a class method can be called at the instance level but it will change the value in relevant class attribute (raise_
# amount) for the class and all the instances and not only for the instance at which level it has been called. 

# using class method as an alternative constructor.

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

#parsing the string
# first, last, pay = emp_str_1.split('-') # saves John, Doe, and 70000 in first, last, and pay, respectively.

# creating an instance, new_emp_1, using init method as an alternative constructor.
# new_emp_1 = Employee(first, last, pay) 
# print(new_emp_1.email)
# print(new_emp_1.pay)
# this may be too much work. So, let's automate it using a class method.

# call the classmethod, from_string, to create an isntance, new_emp_1, from the given string.
new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1) # returns the instance, new_emp_1 address in memory as expected.
# print(new_emp_1.first)
# print(new_emp_1.last)
# print(new_emp_1.email)
# print(new_emp_1.pay)

########### Changing the class attribute at class level as well as instance level #########

# # access class attribute, raise_amount, at the class and instance levels.
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# # all printed 1.04

# # access the class attribute at instance level and change it for that instance.
emp1.raise_amount = 1.10

# # print same as above.
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# # the class attribute, raise_amount, changed only for the instance, emp1, from 1.04 to 1.10.

# # before applying the raise, the salaries were:
# print(emp1.pay) # printed = 100,000
# print(emp2.pay) # printed = 200,000

# # apply the raise to both the instances.
emp1.apply_raise()
emp2.apply_raise()

# # after applying the raise, the salaries are:
# print(emp1.pay) # raise applied correctly. Printed = 110,000 after 10% raise.
# print(emp2.pay) # raise applied correctly. Printed = 208,000 after 4% raise.

# calling a static method
import datetime # note that a package or library can be imported anywhere in the program.
my_date = datetime.date(2016, 7, 11) 
# datetime is either a class or instance and date is a method in that class or isntance. 
#print(my_date) # printed 2016-07-10
print(Employee.is_workday(my_date)) # calling a static method, is_workday, in Employee class.




