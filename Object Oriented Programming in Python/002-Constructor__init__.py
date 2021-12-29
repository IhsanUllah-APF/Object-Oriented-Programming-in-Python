class Item:

    def __init__(self, name: str, price: float, quantity = 0): 
        # name and price must be string and float, respectively. quantitiy default
        #  = 0 so quanity is already marked to be an integer.
        
        # Run validations to the received arguments.
        assert price >= 0, f'Price {price} is not equal to or greater than zero!'
        # to ensure that negative prices are not entered, otherwise, the error typed
        # in the string will be given. f prints value of price given in {}.
        assert quantity >= 0, f'Quantity {quantity} is not equal to or greater than zero!'

        # Assignment to an object.
        self.name = name
        # item1, the object, when created will automatically call this constructor.
        # item1 itself is passed as an argument for self. The body of constructor
        # outlines the instructions to be executed by this method/function. The first
        # isntruction says, go into self, that means the object item1, and put in its
        # field / member variable, name, the value contained in 'name' as an argument
        # above in the function.
        self.price = price
        self.quantity = quantity
# magic method/constructor automatically called when instance is created.
# Python itself passess the instance itself as a first argument.

    def calculate_total_price(self): # x, y deleted as arguments.
        # return x * y  # commented out after deletion of x and y.
        return self.price * self.quantity 

item1 = Item('Phone', 100, 5) # create an object/instance of class Item.
#item1.name = 'Phone' # no need for this assignment now after the constructor. 
#item1.price = 100 # this way assignment is less efficient.
#item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item('Laptop', 1000, 3)
# item2.name = 'Laptop'
#item2.price = 1000
#item2.quantity = 3
# print(item2.calculate_total_price(item2.price, item2.quantity))
item2.has_numpad = False # unique attribute of a particular object should be 
# assigned outside the constructor.

print(item1.name) # it will print the name of object, item1, through constructor.
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

print(item2.has_numpad)

#print(item1.calculate_total_price(100, 5)) # Or, alternatively,
print(item1.calculate_total_price()) # no need for passing price(x) and quantity
# (y) arguments now since it has been taken care in the function itself.
print(item2.calculate_total_price())

