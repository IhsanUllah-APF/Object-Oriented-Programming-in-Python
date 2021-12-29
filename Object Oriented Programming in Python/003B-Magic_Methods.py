# Bismillah

# __str__() and __repr__() are magic functions and methods to print information about instance/object in a meaningful
# manner.

class CustomizedInteger:
    
    def __init__(self, integer): # after constructor has done initialization, the command goes to print.
        self.integer = integer

    def __str__(self): 
        return f'Customized integer {self.integer}' # this function is invoked, it produces string and returns it to 
        # print which gets it printed as a meaningful description of the object, int1. If str() exists, then it is 
        # invoked, and repr() is ignored. str() has priority over repr().

    def __repr__(self):
        return f'Customized integer {self.integer}' # in absence of str(), this function is invoked, it produces
        # string and returns it to print which gets it printed as a meaningful description of the object, int1.


int1 = CustomizedInteger(4) # create an instance of the class, which calls constructor automatically.

# print(int1) # printing this in absence of magic functions, str() and repr() produces following output:
# "<__main__.CustomizedInteger object at 0x0000026B92C0F2E0>". It hardly indicates that CustomizedInteger object has
# address 0x0000026B92C0F2E0. This description about the object is hardly descriptive or meaningful. Thus, the magic
# functions, str() and repr(), when used produces meaningful information about the class as: "Customized integer 4",
# which is certainly more meaningful than the previous description of the object, item1. 


print(int1) # print calls magic function. String returned from the functions is printed, which is more meaningful
# description of the object, int1.

print(2 * 2) # this print does not invoke str() or repr() since it does not attempt to print information about the 
# the object of the class, int1 Thus, the magic functions, str() and repr() are only invoked by the following print
# function when object, in this case int1, is passed as an argument.


