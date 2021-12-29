# Bismillah
 
class Item:

    pay_rate = 0.8 # The pay rate after 20% discount. A class attribute, essentially a global variable, called pay_
    # rate defined and set equal to 0.8.
    # A class attribute is a global attribute which can be accessed from an object/instance level or class level. A class
    # attribute belongs to entire class including all objects by default. 

    def __init__(self, name: str, price: float, quantity = 0): 
                
        # Run validations to the received arguments.
        assert price >= 0, f'Price {price} is not equal to or greater than zero!'
        assert quantity >= 0, f'Quantity {quantity} is not equal to or greater than zero!'

        # Assignment to an object.
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self): 
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # pay_rate won't work. We have to specifically tell python to go 
        # inside class (Item.pay_rate) or inside the object, item1 (self.pay_rate) and access and use the value
        # contained in variable, pay_rate. Item.pay_rate works the same as self.pay_rate as expected. 

item1 = Item('Phone', 100, 5) 
item2 = Item('Laptop', 1000, 3)

print(Item.pay_rate) # the class attribute accessed through class, Item, and not through a specific object here.
print(item1.pay_rate) # the class attribute accessed through the object, item1, here. So, a class attribute can be
print(item2.pay_rate) # accessed and used from a class as well as from an object/instance level.
# Go inside a class and access attribute/variable, pay_rate, and print the value in it.
# Go inside object, item1, and find attribute/variable, pay_rate. It will not be found in the object itself (the
# attributes of item1 so far includes name, price and quantity and not pay_rate), so it # will be looked for in the
# class. When found as a class attribute/global variable, evaluate it to its value and print it.

# Built_in Magic Attribute, __dict__, and not magic method/function
print(Item.__dict__) # Go inside the class, Item, find its all attributes, convert them into dictionary and print them all.
print(item1.__dict__) # Go inside the object, item1, find its all attributes, convert them into dictionary and print them all.

item1.apply_discount()
print(item1.price)

# Function Overriding:
# suppose we have 30% discount for item2, laptop.It is a bad idea to change the pay_rate(discount) in the class 
# attribute/global variable because it will affect all other items as well. So, we should specify this 30% discount
# only for item2, laptop as:
item2.pay_rate = 0.7 
item2.apply_discount()
print(item2.price)
# When pay_rate is searched for item2, laptop, it will be found locally and applied or used without having a need
# to search for it in the class as a global variable or class attribute. This is kind of example of FUNCTION OVERRIDING.

